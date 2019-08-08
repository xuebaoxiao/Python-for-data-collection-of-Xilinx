#########1_3,1_4都可以把.ncl文件的信息初步提取出来

 
#########1_3
import re
buf=''
with open('dump.ncl','r') as wb:
    for line in wb:
        if line.find("/SLICE_")>=0:
            #print line
            #("multiple[0].inst_top/perfcounters/SLICE_34", F1),
            m=re.compile("/SLICE_(\w+)\"\,\s+(\w+)")
            try:
                m1=m.search(str(line))
                m2=str(m1.group(1))+'.'+str(m1.group(2))
            #print m1.group(1)
                print m2
                buf=buf+'SLICE_'+str(m1.group(1))+'.'+str(m1.group(2))+'\n'
            #buf=buf+str(m.group())+'\n'
            except AttributeError:
                pass
            #continue

print buf
with open('test.txt','w') as f:
    f.write(buf)

 

 
#########1_4


import re
p = re.compile(r'/SLICE_(\d+)",\s+(\w+)')
buf='0'
with open("dump.ncl") as ob:
    for line in ob:
        m = p.search(line)
        if m:
            print "{}.{}".format(m.group(1), m.group(2))
            buf=buf+'SLICE_'+str(m.group(1))+'.'+str(m.group(2))+'\n'
print buf
#with open('test_1.txt','w') as f:
    #f.write(buf)

######################x.py用于排序

import re

d = dict()
p = re.compile("_(\d+)(\..+)")
line_list = list()
with open("test.txt") as ob:
    for line in ob:
        line = line.strip()
        if not line:
            continue
        line_list.append(line)
    #reverse=True  or False
my_list = sorted(line_list, key=lambda x: int(p.search(x).group(1)),reverse=False)
buf=''
for item in my_list:
    #print item
    buf=buf+item+'\n'
print buf   
with open('test_01.txt','w') as f:
    f.write(buf)


#########################2csv_01.py用于提取数据到csv表格里

 

import re
buf_tital='Slice_NUM,A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0,FXB,FXA,QFX1,QFX0,FCO,WDO0,WDO1,WDO2,WDO3,WADO0,WADO1,WADO2,WADO3,WRE,WCK\n'
buf_num='0'
buf=''
#buf=buf_num
#A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0,FXB,FXA,QFX1,QFX0,FCO,WDO0,WDO1,WDO2,WDO3,WADO0,WADO1,WADO2,WADO3,WRE,WCK='','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''

with open('test_01.txt','r') as wb:
#A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    for line in wb:
    #A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
        NUM=re.search("_(\d+)\.(.+)",line)
        print NUM.group(1)
        if (str(NUM.group(1))==buf_num):
            if(NUM.group(2)=='A1'):
                A1='1'
            elif(NUM.group(2)=='B1'):
                B1='1'
            elif(NUM.group(2)=='C1'):
                C1='1'
            elif(NUM.group(2)=='D1'):
                D1='1'
            elif(NUM.group(2)=='A0'):
                A0='1'
            elif(NUM.group(2)=='B0'):
                B0='1'
            elif(NUM.group(2)=='C0'):
                C0='1'
            elif(NUM.group(2)=='D0'):
                D0='1'
            elif(NUM.group(2)=='SEL'):
                SEL='1'
            elif(NUM.group(2)=='DI1'):
                DI1='1'
            elif(NUM.group(2)=='M1'):
                M1='1'
            elif(NUM.group(2)=='CLK'):
                CLK='1'
            elif(NUM.group(2)=='LSR'):
                LSR='1'
            elif(NUM.group(2)=='CE'):
                CE='1'
            elif(NUM.group(2)=='DI0'):
                DI0='1'
            elif(NUM.group(2)=='M0'):
                M0='1'
            elif(NUM.group(2)=='F1'):
                F1='1'
            elif(NUM.group(2)=='OFX0'):
                OFX0='1'
            elif(NUM.group(2)=='F0'):
                F0='1'
            elif(NUM.group(2)=='Q1'):
                Q1='1'
            elif(NUM.group(2)=='Q0'):
                Q0='1'
            elif(NUM.group(2)=='FXB'):
                FXB='1'
            elif(NUM.group(2)=='FXA'):
                FXA='1'
            elif(NUM.group(2)=='QFX1'):
                QFX1='1'
            elif(NUM.group(2)=='QFX0'):
                QFX0='1'
            elif(NUM.group(2)=='FCO'):
                FCO='1'
            elif(NUM.group(2)=='WDO0'):
                WDO0='1'
            elif(NUM.group(2)=='WDO1'):
                WDO1='1'
            elif(NUM.group(2)=='WDO2'):
                WDO2='1'
            elif(NUM.group(2)=='WDO3'):
                WDO3='1'
            elif(NUM.group(2)=='WADO0'):
                WADO0='1'
            elif(NUM.group(2)=='WADO1'):
                WADO1='1'
            elif(NUM.group(2)=='WADO2'):
                WADO2='1'
            elif(NUM.group(2)=='WADO3'):
                WADO3='1'
            elif(NUM.group(2)=='WRE'):
                WRE='1'
            else:
            #elif(NUM.group(2)=='WCK'):
                WCK='1'
            #elif(NUM.group(2)=='Q0'):
                #Q0='1'
        else:
            buf=buf+buf_num+','+A1+','+B1+','+C1+','+D1+','+A0+','+B0+','+C0+','+D0+','+SEL+','+DI1+','+M1+','+CLK+','+LSR+','+CE+','+DI0+','+M0+','+F1+','+OFX0+','+F0+','+Q1+','+Q0+','+FXB+','+FXA+','+QFX1+','+QFX0+','+FCO+','+WDO0+','+WDO1+','+WDO2+','+WDO3+','+WADO0+','+WADO1+','+WADO2+','+WADO3+','+WRE+','+WCK+'\n'
            #A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
            A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0,FXB,FXA,QFX1,QFX0,FCO,WDO0,WDO1,WDO2,WDO3,WADO0,WADO1,WADO2,WADO3,WRE,WCK='','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''
            if(NUM.group(2)=='A1'):
                A1='1'
            elif(NUM.group(2)=='B1'):
                B1='1'
            elif(NUM.group(2)=='C1'):
                C1='1'
            elif(NUM.group(2)=='D1'):
                D1='1'
            elif(NUM.group(2)=='A0'):
                A0='1'
            elif(NUM.group(2)=='B0'):
                B0='1'
            elif(NUM.group(2)=='C0'):
                C0='1'
            elif(NUM.group(2)=='D0'):
                D0='1'
            elif(NUM.group(2)=='SEL'):
                SEL='1'
            elif(NUM.group(2)=='DI1'):
                DI1='1'
            elif(NUM.group(2)=='M1'):
                M1='1'
            elif(NUM.group(2)=='CLK'):
                CLK='1'
            elif(NUM.group(2)=='LSR'):
                LSR='1'
            elif(NUM.group(2)=='CE'):
                CE='1'
            elif(NUM.group(2)=='DI0'):
                DI0='1'
            elif(NUM.group(2)=='M0'):
                M0='1'
            elif(NUM.group(2)=='F1'):
                F1='1'
            elif(NUM.group(2)=='OFX0'):
                OFX0='1'
            elif(NUM.group(2)=='F0'):
                F0='1'
            elif(NUM.group(2)=='Q1'):
                Q1='1'
            elif(NUM.group(2)=='Q0'):
                Q0='1'
            elif(NUM.group(2)=='FXB'):
                FXB='1'
            elif(NUM.group(2)=='FXA'):
                FXA='1'
            elif(NUM.group(2)=='QFX1'):
                QFX1='1'
            elif(NUM.group(2)=='QFX0'):
                QFX0='1'
            elif(NUM.group(2)=='FCO'):
                FCO='1'
            elif(NUM.group(2)=='WDO0'):
                WDO0='1'
            elif(NUM.group(2)=='WDO1'):
                WDO1='1'
            elif(NUM.group(2)=='WDO2'):
                WDO2='1'
            elif(NUM.group(2)=='WDO3'):
                WDO3='1'
            elif(NUM.group(2)=='WADO0'):
                WADO0='1'
            elif(NUM.group(2)=='WADO1'):
                WADO1='1'
            elif(NUM.group(2)=='WADO2'):
                WADO2='1'
            elif(NUM.group(2)=='WADO3'):
                WADO3='1'
            elif(NUM.group(2)=='WRE'):
                WRE='1'
            else:
            #elif(NUM.group(2)=='WCK'):
                WCK='1'
            buf_num=str(NUM.group(1))
    print buf
buf=buf_tital+buf
with open("test.csv",'w') as f:
    f.write(buf)
    print("write_done")