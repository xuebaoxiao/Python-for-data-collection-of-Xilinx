import math
import os
import re
import csv

batch_folder='D:\\Hunter_Wang\\01_oc_avr_hp_cm4\\Hunter_test_1000k_1'
top_module='avr_hp_cm4_wrapper'
device_prefix='kintu'

case_size_list=270,320,370
case_fmax_list=320,340,360,380,400

buf='Core_Number,Target_Fmax,Target_Period,WNS_Place,Fmax_place,Real_WNS,Real_Fmax,LUT,Total_LUT,LUT%,REG,Total_REG,REG%,EBR,Total_EBR,EBR%,Slice,Total_Slice,Slice%,syn_runtime,syn_Memory,Placer_cpu,placer_elasped,elasped(P)_vs_cpu%,Placer_Memory,Router_cpu,Router_elasped,elasped(R)_vs_cpu%,Router_Memory\n'

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
        os.chdir(proj_name+'\\'+proj_name+'.'+'runs\impl_1')
        print '\n'
        print "design unit:",case_size
        print "target Fmax:",case_fmax
        #print buf
        fit_report_file_name=top_module
        fit_report_file_name=fit_report_file_name+'_utilization_placed.rpt'
        tsp_report_file_name=top_module
        tsp_report_file_name=tsp_report_file_name+'_timing_summary_placed.rpt'
        tsr_report_file_name=top_module
        tsr_report_file_name=tsr_report_file_name+'_timing_summary_routed.rpt'
        time_report_file_name=top_module
        time_report_file_name=time_report_file_name+'.vdi'
####################tsp report##############################
        with open(tsp_report_file_name,'r') as tb:
            lineNum=1
            matchline=-1
            for line in tb:
                if line.find("| Design Timing Summary")>=0:
                    matchline=lineNum+6
                    #print line
                    #print lineNum
                if lineNum<=matchline:
                    #print line
                    tsp=line
                lineNum+=1
            tspa=tsp.split()
            WNS_Place=float(tspa[0])
            Fmax_place=1000/(float(case_period)-WNS_Place)
            Fmax_place=("%.3f" %Fmax_place)
            buf=buf+str(WNS_Place)
            buf=buf+','
            buf=buf+str(Fmax_place)
            buf=buf+','
            #buf=buf+'\n'
            #print buf
####################end tsp report##########################

####################tsr report##############################
        with open(tsr_report_file_name,'r') as rb:
            lineNum=1
            matchline=-1
            for line in rb:
                if line.find("| Design Timing Summary")>=0:
                    matchline=lineNum+6
                    #print line
                    #print lineNum
                if lineNum<=matchline:
                    #print line
                    tsr=line
                lineNum+=
            tsra=tsr.split()
            Real_WNS=float(tsra[0])
            real_fmax=1000/(float(case_period)-Real_WNS)
            real_fmax=("%.3f" %real_fmax)
            buf=buf+str(Real_WNS)
            buf=buf+','
            buf=buf+str(real_fmax)
            #buf=buf+'\n'
#print buf
####################end tsr report##########################

####################fit report##############################
        with open(fit_report_file_name,'r') as fb:
            lineNum_fit=1
            matchline_lut=-1
            matchline_clb=-1
            for line in fb:
                if line.find("Utilization Design Information")>=0:
                    matchline_lut=lineNum_fit+27
                    matchline_clb=lineNum_fit+32
                    print line
                if lineNum_fit==matchline_lut:
                    print line
                    #| CLB LUTs       | 270940 |     0 |    331680 | 81.69 |
                    lut_flag = re.compile("""\|\s+CLB\s+LUTs\s+
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|
                                             """, re.X)
                    lut_buf1=lut_flag.search(line)
                    if lut_buf1:
                        LUT, LUT_Available, LUT_Util=lut_buf1.group(1), lut_buf1.group(3), lut_buf1.group(4)
                        print("%s,%s,%s" %(LUT, LUT_Available, LUT_Util))
                                  
                #if line.find("| CLB Registers              | ")>=0:
                if lineNum_fit==matchline_clb:
                    print line
                    #| CLB Registers              | 212128 |     0 |    663360 | 31.98 |
                    reg_flag = re.compile("""\|\s+CLB\s+Registers\s+
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|
                                             """, re.X)
                    reg_buf1=reg_flag.search(line)
                    if reg_buf1:
                        REG, REG_Available, REG_Util=reg_buf1.group(1), reg_buf1.group(3), reg_buf1.group(4)        
                        print("%s,%s,%s" %(REG, REG_Available, REG_Util))
                lineNum_fit+=1                              
                if line.find("|   RAMB18       |")>=0:
                    print line
                    #|   RAMB18       |    0 |     0 |      2160 |  0.00 |
                    ram_flag = re.compile("""\|\s+RAMB18\s+
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|
                                             """, re.X)
                    ram_buf1=ram_flag.search(line)
                    if ram_buf1:
                        RAM, RAM_Available, RAM_Util=ram_buf1.group(1), ram_buf1.group(3), ram_buf1.group(4)
                        print("%s,%s,%s" %(RAM, RAM_Available, RAM_Util))                               
                if line.find("| CLB                |")>=0:
                    print line
                    #| CLB                |  41185 |     0 |     41460 | 99.34 |
                    clb_flag = re.compile("""\|\s+CLB\s+
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|\s+([\d\.]+)
                                             \s+\|
                                             """, re.X)
                    clb_buf1=clb_flag.search(line)
                    if clb_buf1:
                        CLB, CLB_Available, CLB_Util=clb_buf1.group(1), clb_buf1.group(3), clb_buf1.group(4)
                        print("%s,%s,%s" %(CLB, CLB_Available, CLB_Util))                                  
            buf=buf+','+LUT+','+LUT_Available+','+LUT_Util
            buf=buf+','+REG+','+REG_Available+','+REG_Util
            buf=buf+','+RAM+','+RAM_Available+','+RAM_Util
            buf=buf+','+CLB+','+CLB_Available+','+CLB_Util
            #buf=buf+'\n'
####################end fit report##############################
#print buf               
####################synth report################################
        os.chdir(batch_folder)
        os.chdir(proj_name+'\\'+proj_name+'.'+'runs\\synth_1')
        with open('runme.log','r') as runme:
            for line in runme:
                if line.find("Synthesis Optimization Complete")>=0:       
                    print line
                    # Synthesis Optimization Complete : Time (s): cpu = 00:08:08 ; elapsed = 00:08:16 . Memory (MB): peak = 3378.555 ; gain = 3038.496
                    syn_flag = re.compile("""Synthesis\s+Optimization\s+Complete
                                             \s+:\s+Time\s+\(s\):\s+cpu\s+=\s+(\S+)
                                             \s+;\s+elapsed\s+=\s+(\S+)
                                             \s+\.\s+Memory\s+\(MB\):\s+peak\s+=\s+([\d\.]+)
                                             \s+;\s+gain\s+=\s+([\d\.]+)                      
                                             """, re.X)
                    syn_buf1=syn_flag.search(line)
                    if syn_buf1:
                        syn_cpu_time, syn_elapsed_time, Mem_peak, Mem_gain = syn_buf1.group(1), syn_buf1.group(2), syn_buf1.group(3), syn_buf1.group(4)
                        print("%s,%s,%s,%s" %(syn_cpu_time, syn_elapsed_time, Mem_peak, Mem_gain))
            buf=buf+','+syn_cpu_time+','+Mem_peak
#print buf                              
#################### end synth report ##########################             

#################### PAR report ##############################                       
        os.chdir(batch_folder)
        os.chdir(proj_name+'\\'+proj_name+'.'+'runs\impl_1')
        with open(time_report_file_name,'r') as time_report:
            for line in time_report:
                if line.find("place_design: Time")>=0:
                    print line
                    # place_design: Time (s): cpu = 00:39:29 ; elapsed = 00:40:55 . Memory (MB): peak = 7166.836 ; gain = 3564.883
                    place_flag = re.compile("""place_design:\s+Time\s+\(s\):\s+cpu\s+=\s+(\d+):(\d+):(\d+)
                                               \s+;\s+elapsed\s+=\s+(\d+):(\d+):(\d+)
                                               \s+\.\s+Memory\s+\(MB\):\s+peak\s+=\s+([\d\.]+)
                                               \s+;\s+gain\s+=\s+([\d\.]+)                      
                                               """, re.X)
                    place_buf1=place_flag.search(line)
                    if place_buf1:
                        h11, m11, s11, h12, m12, s12, Place_Memory, ex1 = place_buf1.group(1), place_buf1.group(2), place_buf1.group(3), place_buf1.group(4), place_buf1.group(5), place_buf1.group(6), place_buf1.group(7), place_buf1.group(8)
                        print("%s:%s:%s,%s:%s:%s,%s,%s" %(h11, m11, s11, h12, m12, s12, Place_Memory, ex1))
                        e1 = 3600*int(h12)+60*int(m12)+int(s12)
                        c1 = 3600*int(h11)+60*int(m11)+int(s11)
                        e1=float(e1)
                        c1=float(c1)
                        elaspedPvscpu = 100*(e1-c1)/c1
                        ePvsc=("%.3f" %elaspedPvscpu)
                        print ePvsc

                if line.find("route_design: Time")>=0:
                    print line
                    # route_design: Time (s): cpu = 00:33:20 ; elapsed = 00:34:06 . Memory (MB): peak = 9216.605 ; gain = 2049.770
                    route_flag = re.compile("""route_design:\s+Time\s+\(s\):\s+cpu\s+=\s+(\d+):(\d+):(\d+)
                                               \s+;\s+elapsed\s+=\s+(\d+):(\d+):(\d+)
                                               \s+\.\s+Memory\s+\(MB\):\s+peak\s+=\s+([\d\.]+)
                                               \s+;\s+gain\s+=\s+([\d\.]+)                      
                                              """, re.X)
                    route_buf1=route_flag.search(line)
                    if route_buf1:
                        h21, m21, s21, h22, m22, s22, Route_Memory, ex2 = route_buf1.group(1), route_buf1.group(2), route_buf1.group(3), route_buf1.group(4), route_buf1.group(5), route_buf1.group(6), route_buf1.group(7), route_buf1.group(8)
                        print("%s:%s:%s,%s:%s:%s,%s,%s" %(h21, m21, s21, h22, m22, s22, Route_Memory, ex2))
                        e2 = 3600*int(h22)+60*int(m22)+int(s22)
                        c2 = 3600*int(h21)+60*int(m21)+int(s21)
                        e2=float(e2)
                        c2=float(c2)
                        elaspedRvscpu = 100*(e2-c2)/c2
                        eRvsc=("%.3f" %elaspedRvscpu)
                        print eRvsc   
        buf=buf+','+str(h11)+':'+str(m11)+':'+str(s11)+','+str(h12)+':'+str(m12)+':'+str(s12)+','+str(ePvsc)+','+str(Place_Memory)
        buf=buf+','+str(h21)+':'+str(m21)+':'+str(s21)+','+str(h22)+':'+str(m22)+':'+str(s22)+','+str(eRvsc)+','+str(Route_Memory)
        buf=buf+'\n'     
####################end PAR report##########################
#print buf

os.chdir(batch_folder)
table_name=device_prefix+'_'+top_module+'_'+'report.csv'
with open(table_name,'w') as f:
    f.write(buf)
    print("write_done")