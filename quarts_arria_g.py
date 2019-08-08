import math
import os
import re
import csv

batch_folder='D:\\Arch_Benchmark\\Hunter_Wang\\04_oc_usbhostslave\\arri_batch'
top_module='usbhostslave_wrapper'
device_prefix='arria'

case_size_list=30,33,36,39,41,44
case_fmax_list=300,310,320,330,340,350,360,370,380

buf='Core_Number,Target_Fmax,Target_Period,Real_WNS,Real_Fmax,LUT,Total_LUT,LUT%,REG,EBR,Total_EBR,EBR%,syn_runtime,syn_runtime(cpu),syn_Memory,PAR_runtime,PAR_runtime(cpu),PAR_Memory\n'
for case_size in case_size_list:
    for case_fmax in case_fmax_list:
        case_period=1000/float(case_fmax)
        case_period=("%.3f" %case_period)
        #print case_period
        buf=buf+str(case_size)
        buf=buf+','
        buf=buf+str(case_fmax)
        buf=buf+','
        buf=buf+str(case_period
        buf=buf+','
        #buf=buf+'\n'
        os.chdir(batch_folder)
        #os.getcwd() print the path
        proj_name=device_prefix+'_'+str(case_size)+'_'+str(case_fmax)
        os.chdir(proj_name+'\\'+'output_files')
        print '\n'
        print "design unit:",case_size
        print "target Fmax:",case_fmax
        #print buf
        fit_report_file_name=top_module
        fit_report_file_name=fit_report_file_name+'.fit.summary'
        #tsp_report_file_name=top_module
        #tsp_report_file_name=tsp_report_file_name+'_timing_summary_placed.rpt'
        sta_report_file_name=top_module
        sta_report_file_name=sta_report_file_name+'.sta.summary'
        time_report_file_name=top_module
        time_report_file_name=time_report_file_name+'.flow.rpt'
        
####################tsp report##############################

####################end tsp report##########################

####################tsr report##############################
        with open(sta_report_file_name,'r') as rb:
            lineNum=1
            matchline=-1
            for line in rb:
                if line.find("Type  : Slow 900mV 100C Model Setup")>=0:
                    matchline=lineNum+1
                    #print line
                    #print lineNum
                if lineNum==matchline:
                    print line
                    #Slack : 0.459
                    WNS_flag = re.compile("""Slack\s+:\s+([\d\.]+)""", re.X)
                    WNS_buf1=WNS_flag.search(line)
                    if WNS_buf1:
                        WNS=WNS_buf1.group(1)         
                        print("%s" %(WNS))
                lineNum+=1
            Real_WNS=float(WNS)
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
            for line in fb:
                if line.find("Logic utilization")>=0:
                    print line
                    # Logic utilization (in ALMs) : 36,140 / 61,510 ( 59 % )
                    lut_flag = re.compile("""Logic\s+utilization\s+\(in\s+ALMs\)
                                             \s+:\s+(\d+),(\d+)
                                             \s+\/\s+(\d+),(\d+)
                                             \s+\(\s+([\d\.]+)\s+%\s+\)
                                             """, re.X)
                    lut_buf1=lut_flag.search(line)
                    if lut_buf1:
                        LUT_1, LUT_2, LUT_Available_1, LUT_Available_2, LUT_Util=lut_buf1.group(1), lut_buf1.group(2), lut_buf1.group(3), lut_buf1.group(4), lut_buf1.group(5)
                        LUT=LUT_1+LUT_2
                        LUT_Available=LUT_Available_1+LUT_Available_2
                        print("%s,%s,%s" %(LUT, LUT_Available, LUT_Util))
                if line.find("Total registers")>=0:
                    print line
                    # Total registers : 64843
                    reg_flag = re.compile("""Total\s+registers\s+:\s+([\d\.]+)""", re.X)
                    reg_buf1=reg_flag.search(line)
                    if reg_buf1:
                        REG=reg_buf1.group(1)
                        print("%s" %(REG))
                if line.find("Total RAM Blocks")>=0:
                    print line
                    # Total RAM Blocks : 300 / 440 ( 68 % )
                    ram_flag = re.compile("""Total\s+RAM\s+Blocks
                                             \s+:\s+([\d\.]+)
                                             \s+\/\s+([\d\.]+)
                                             \s+\(\s+([\d\.]+)\s+%\s+\)
                                             """, re.X)
                    ram_buf1=ram_flag.search(line)
                    if ram_buf1:
                        RAM, RAM_Available, RAM_Util=ram_buf1.group(1), ram_buf1.group(2), ram_buf1.group(3)
                        print("%s,%s,%s" %(RAM, RAM_Available, RAM_Util))
            buf=buf+','+LUT+','+LUT_Available+','+LUT_Util
            buf=buf+','+REG
            buf=buf+','+RAM+','+RAM_Available+','+RAM_Util
####################end fit report##############################

#print buf               

####################time report#################################
        with open(time_report_file_name,'r') as time_report:
            linenum=1
            matchline_syn=-1
            matchline_par=-1
            for line in time_report:
                if line.find("; Flow Elapsed Time")>=0:
                    matchline_syn=linenum+4
                    matchline_par=linenum+5
                    print line
                if linenum==matchline_syn:
                    print line
                    # ; Analysis & Synthesis ; 00:02:26     ; 2.0                     ; 1750 MB             ; 00:01:32               ;
                    syn_time_flag=re.compile(""";\s+Analysis\s+\&\s+Synthesis\s+;
                                                \s+(\d+):(\d+):(\d+)
                                                \s+;\s+([\d\.]+)
                                                \s+;\s+([\d\.]+)\s+MB
                                                \s+;\s+(\d+):(\d+):(\d+)
                                                \s+;
                                                """, re.X)
                    syn_buf1=syn_time_flag.search(line)
                    if syn_buf1:
                        h11, m11, s11, Average_Processors_Used_syn, Peak_Memory_syn, h12, m12, s12 = syn_buf1.group(1), syn_buf1.group(2), syn_buf1.group(3), syn_buf1.group(4), syn_buf1.group(5), syn_buf1.group(6), syn_buf1.group(7), syn_buf1.group(8)
                        print("%s:%s:%s,%s,%s,%s:%s:%s" %(h11, m11, s11, Average_Processors_Used_syn, Peak_Memory_syn, h12, m12, s12))
                if linenum==matchline_par:
                    print line
                    # ; Fitter               ; 00:11:57     ; 1.3                     ; 8399 MB             ; 00:39:26               ;
                    par_time_flag=re.compile(""";\s+Fitter\s+;
                                                \s+(\d+):(\d+):(\d+)
                                                \s+;\s+([\d\.]+)
                                                \s+;\s+([\d\.]+)\s+MB
                                                \s+;\s+(\d+):(\d+):(\d+)
                                                \s+;
                                                """, re.X)
                    par_buf1=par_time_flag.search(line)
                    if par_buf1:
                        h21, m21, s21, Average_Processors_Used_par, Peak_Memory_par, h22, m22, s22 = par_buf1.group(1), par_buf1.group(2), par_buf1.group(3), par_buf1.group(4), par_buf1.group(5), par_buf1.group(6), par_buf1.group(7), par_buf1.group(8)
                        print("%s:%s:%s,%s,%s,%s:%s:%s" %(h21, m21, s21, Average_Processors_Used_par, Peak_Memory_par, h22, m22, s22))
                linenum+=1
            buf=buf+','+str(h11)+':'+str(m11)+':'+str(s11)+','+str(h12)+':'+str(m12)+':'+str(s12)+','+str(Peak_Memory_syn)
            buf=buf+','+str(h21)+':'+str(m21)+':'+str(s21)+','+str(h22)+':'+str(m22)+':'+str(s22)+','+str(Peak_Memory_par)
            buf=buf+'\n'
####################time report#################################                     
print buf

os.chdir(batch_folder)
with open("test.csv",'w') as f:
    f.write(buf)
    print("write_done")