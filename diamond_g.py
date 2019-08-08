import math
import os
import re
import csv

batch_folder='D:\\Arch_Benchmark\\Hunter_Wang\\04_oc_usbhostslave\\ecp5_batch'
top_module='usbhostslave_wrapper'
device_prefix='ecp5'

case_size_list=16,19,22,25,28
case_fmax_list=160,170,180,190,200

buf='Core_Number,Target_Fmax,Target_Period,Real_Fmax,LUT,Total_LUT,LUT%,REG,Total_REG,REG%,EBR,Total_EBR,EBR%,Slice,Total_Slice,Slice%,PIO,Total_PIO,PIO%,syn_runtime(cpu),syn_runtime(real),syn_Memory,MAP_runtime,MAP_runtime(cpu),MAP_Memory\n'
for case_size in case_size_list:
    for case_fmax in case_fmax_list:
        case_period=1000/float(case_fmax)
        case_period=("%.3f" %case_period)
        #print case_period
        buf=buf+str(case_size)
        buf=buf+','
        buf=buf+str(case_fmax)
        buf=buf+','
        buf=buf+str(case_period)
        buf=buf+','
        #buf=buf+'\n'
        os.chdir(batch_folder)
        #os.getcwd() print the path
        proj_name=device_prefix+'_'+str(case_size)+'_'+str(case_fmax)
        os.chdir(proj_name+'\\'+'impl1')

        print '\n'
        print "design unit:",case_size
        print "target Fmax:",case_fmax
        #print buf
        fit_report_file_name=proj_name
        fit_report_file_name=fit_report_file_name+'_impl1.mrp'
        tsp_report_file_name=proj_name
        tsp_report_file_name=tsp_report_file_name+'_impl1.twr'
        #Syn_time_report_file_name=proj_name
        #Syn_time_report_file_name=tsr_report_file_name+'_impl1_compiler.srr'
        Map_report_file_name=proj_name
        Map_report_file_name=Map_report_file_name+'_impl1.srr'

####################tsp report##############################
        with open(tsp_report_file_name,'r') as tb:
            lineNum=1
            matchline=-1
            for line in tb:
                if line.find("Preference                  |   Constraint|       Actual|Levels")>=0:
                    matchline=lineNum+6
                    #print line
                    #print lineNum
                if lineNum==matchline:
                    print line
                    # MHz ;           |  160.000 MHz|  186.185 MHz|   2
                    tsp_flag = re.compile("""MHz\s+;
                                            \s+\|\s+([\d\.]+)\s+MHz
                                            \|\s+([\d\.]+)\s+MHz
                                            \|\s+(\d+) """, re.X)
                    tsp_buf1=tsp_flag.search(line)
                    if tsp_buf1:
                        freq_targ, freq_real, logic_level=tsp_buf1.group(1), tsp_buf1.group(2), tsp_buf1.group(3)
                        print("%s,%s,%s" %(freq_targ, freq_real, logic_level))
                lineNum+=1
            buf=buf+freq_real

####################end tsp report##########################

####################fit report##############################
        with open(fit_report_file_name,'r') as fb:
            for line in fb:
                if line.find("Number of LUT4s:")>=0:
                    print line
                    #   Number of LUT4s:        46992 out of 83640 (56%)
                    lut_flag = re.compile("""\s+Number\s+of\s+LUT4s:
                                            \s+(\d+)\s+out\s+of
                                            \s+(\d+)
                                            \s+\((\d+)%\)
                                            """, re.X)
                    lut_buf1=lut_flag.search(line)
                    if lut_buf1:
                        LUT, LUT_Available, LUT_Util=lut_buf1.group(1), lut_buf1.group(2), lut_buf1.group(3)
                        print("%s,%s,%s" %(LUT, LUT_Available, LUT_Util))

                if line.find("Number of registers:")>=0:
                    print line
                    #   Number of registers:  32704 out of 84735 (39%)
                    reg_flag = re.compile("""\s+Number\s+of\s+registers:
                                            \s+(\d+)\s+out\s+of
                                            \s+(\d+)
                                            \s+\((\d+)%\)
                                            """, re.X)
                    reg_buf1=reg_flag.search(line)
                    if reg_buf1:
                        REG, REG_Available, REG_Util=reg_buf1.group(1), reg_buf1.group(2), reg_buf1.group(3)        
                        print("%s,%s,%s" %(REG, REG_Available, REG_Util))

                if line.find("Number of block RAMs:")>=0:
                    print line
                    #   Number of block RAMs:  0 out of 208 (0%)
                    ram_flag = re.compile("""\s+Number\s+of\s+block\s+RAMs:
                                             \s+(\d+)\s+out\s+of
                                             \s+(\d+)
                                             \s+\((\d+)%\)
                                             """, re.X)
                    ram_buf1=ram_flag.search(line)
                    if ram_buf1:
                        RAM, RAM_Available, RAM_Util=ram_buf1.group(1), ram_buf1.group(2), ram_buf1.group(3)
                        print("%s,%s,%s" %(RAM, RAM_Available, RAM_Util))

                if line.find("Number of SLICEs:")>=0:
                    print line
                    #   Number of SLICEs:     32678 out of 41820 (78%)
                    clb_flag = re.compile("""\s+Number\s+of\s+SLICEs:
                                            \s+(\d+)\s+out\s+of
                                            \s+(\d+)
                                            \s+\((\d+)%\)
                                            """, re.X)
                    clb_buf1=clb_flag.search(line)
                    if clb_buf1:
                        CLB, CLB_Available, CLB_Util=clb_buf1.group(1), clb_buf1.group(2), clb_buf1.group(3)
                        print("%s,%s,%s" %(CLB, CLB_Available, CLB_Util))

                if line.find("Number of PIO sites used:")>=0:
                    print line
                    #     Number of PIO sites used: 36 out of 365 (10%)
                    IO_flag = re.compile("""\s+Number\s+of\s+PIO\s+sites\s+used:
                                            \s+(\d+)\s+out\s+of
                                            \s+(\d+)
                                            \s+\((\d+)%\)
                                            """, re.X)
                    IO_buf1=IO_flag.search(line)
                    if IO_buf1:
                        IO, IO_Available, IO_Util=IO_buf1.group(1), IO_buf1.group(2), IO_buf1.group(3)
                        print("%s,%s,%s" %(IO, IO_Available, IO_Util))

            buf=buf+','+LUT+','+LUT_Available+','+LUT_Util
            buf=buf+','+REG+','+REG_Available+','+REG_Util
            buf=buf+','+RAM+','+RAM_Available+','+RAM_Util
            buf=buf+','+CLB+','+CLB_Available+','+CLB_Util
            buf=buf+','+IO+','+IO_Available+','+IO_Util
            #print buf
####################end fit report##############################
#print buf               
####################Syn_time report#################################
        with open(fit_report_file_name,'r') as runme:
            for line in runme:
                if line.find("Total CPU Time:")>=0:
                    print line
                    #      Total CPU Time: 1 mins 49 secs
                    syn_flag1 = re.compile("""\s+Total\s+CPU\s+Time:
                                              \s+(\d+)\s+mins
                                              \s+(\d+)\s+secs
                                              """, re.X)
                    syn_buf1=syn_flag1.search(line)
                    if syn_buf1:
                        m11,s11=syn_buf1.group(1), syn_buf1.group(2)
                        print("00:%s:%s," %(m11,s11))

                if line.find("Total REAL Time:")>=0:
                    print line
                    #  Total REAL Time: 2 mins 5 secs
                    syn_flag2 = re.compile("""\s+Total\s+REAL\s+Time:
                                              \s+(\d+)\s+mins
                                              \s+(\d+)\s+secs
                                              """, re.X)
                    syn_buf2=syn_flag2.search(line)
                    if syn_buf2:
                        m12,s12=syn_buf2.group(1), syn_buf2.group(2)
                        print("00:%s:%s," %(m12,s12))

                if line.find("Peak Memory Usage:")>=0:
                    print line
                    # Peak Memory Usage: 726 MB
                    syn_flag3 = re.compile("""\s+Peak\s+Memory\s+Usage:
                                              \s+(\d+)\s+MB
                                              """, re.X)
                    syn_buf3=syn_flag3.search(line)
                    if syn_buf3:
                        syn_Memory=syn_buf3.group(1)
                        print("%sMB," %(syn_Memory))
            buf=buf+','+'00:'+m11+':'+s11+','+'00:'+m12+':'+s12+','+syn_Memory
#################### end synth_time report ##########################              

#################### MAP report ##############################                             
        with open(Map_report_file_name,'r') as time_report:
            lineNum_map=1
            matchline_map=-1
            for line in time_report:
                if line.find("Mapper successful!")>=0:
                    matchline_map=lineNum_map+2
                    #print line
                    #print lineNum
                if lineNum_map==matchline_map:
                    print line
                    # At Mapper Exit (Real Time elapsed 0h:05m:04s; CPU Time elapsed 0h:04m:28s; Memory used current: 147MB peak: 534MB)
                    map_flag = re.compile("""At\s+Mapper\s+Exit\s+\(Real\s+Time\s+elapsed\s+(\d+)h:(\d+)m:(\d+)s
                                             ;\s+CPU\s+Time\s+elapsed\s+(\d+)h:(\d+)m:(\d+)s;
                                             \s+Memory\s+used\s+current:\s+(\d+)MB
                                             \s+peak:\s+(\d+)MB\)                    
                                             """, re.X)
                    mapp_buf1=map_flag.search(line)
                    if mapp_buf1:
                        h21, m21, s21, h22, m22, s22, Map_Memory, Map_Memory_peak = mapp_buf1.group(1), mapp_buf1.group(2), mapp_buf1.group(3), mapp_buf1.group(4), mapp_buf1.group(5), mapp_buf1.group(6), mapp_buf1.group(7), mapp_buf1.group(8)
                        print("%s:%s:%s,%s:%s:%s,%s,%s" %(h21, m21, s21, h22, m22, s22, Map_Memory, Map_Memory_peak))
                lineNum_map+=1
            buf=buf+','+str(h21)+':'+str(m21)+':'+str(s21)+','+str(h22)+':'+str(m22)+':'+str(s22)+','+str(Map_Memory_peak)
            buf=buf+'\n'        
####################end PAR report##########################
#print buf

os.chdir(batch_folder)
with open("test.csv",'w') as f:
    f.write(buf)
    print("write_done")