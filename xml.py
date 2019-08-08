################sty_03.py

#############初步提取xml数据

import xml.etree.ElementTree as ET
tree = ET.parse('C:\Users\hwang10\Desktop\usb_funct.xml')
root = tree.getroot()
for i in root.iter('Design'):
#buf=str(root.tag)+'\n'
    buf='Design:'+str(i.attrib)+'\n'+'\n'
for i in root.findall("./Design/View/Module/Signal"):
    buf=buf+'Signal'+str(i.attrib)+'\n'
    #print buf
    for b in i.findall("./Driver"):
        buf=buf+'Driver:'+str(b.text)+'\n'
        #print buf
    for c in i.findall("./Load"):
        buf=buf+'Load:'+str(c.text)+'\n'
    buf=buf+'\n'
print buf
with open('test.txt','w') as f:
    f.write(buf)
        #print c.text
 

###########simp_01.py

##################精简数据

import re
buf=''
with open('test.txt','r') as slice_:
    for line in slice_:
        if line.find("SLICE_")>=0:
            #print line
            m=re.search('SLICE_(\w+).*',line)
            #print m.group()
            buf=buf+str(m.group())+'\n'
print buf
with open('test_01.txt','w') as f:
    f.write(buf)

 
#################x.py

#####################排序

import re

d = dict()
p = re.compile("_(\d+)(\..+)")
line_list = list()
with open("test_01.txt") as ob:
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
with open('test_02.txt','w') as f:
    f.write(buf)
 

 

#################2csv_01.py

################提取到csv表格里

import re
buf_tital='Slice_NUM,A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0\n'
buf_num='0'
buf=''
#buf=buf_num
#A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='','','','','','','','','','','','','','','','','','','','',''

with open('test_02.txt','r') as wb:
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
            else:
                Q0='1'
            #elif(NUM.group(2)=='Q0'):
                #Q0='1'
        else:
            buf=buf+buf_num+','+A1+','+B1+','+C1+','+D1+','+A0+','+B0+','+C0+','+D0+','+SEL+','+DI1+','+M1+','+CLK+','+LSR+','+CE+','+DI0+','+M0+','+F1+','+OFX0+','+F0+','+Q1+','+Q0+'\n'
            #A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
            A1,B1,C1,D1,A0,B0,C0,D0,SEL,DI1,M1,CLK,LSR,CE,DI0,M0,F1,OFX0,F0,Q1,Q0='','','','','','','','','','','','','','','','','','','','',''
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
            else:
                Q0='1'
            buf_num=str(NUM.group(1))
    print buf
buf=buf_tital+buf
with open("test.csv",'w') as f:
    f.write(buf)
    print("write_done")