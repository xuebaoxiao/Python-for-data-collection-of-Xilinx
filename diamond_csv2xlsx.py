###########csv2xlsx###########

import csv
import xlsxwriter
def csv_to_xlsx():
    with open('test.csv', 'r') as f:
        read = csv.reader(f)
        #workbook   = xlsxwriter.Workbook('filename.xlsx')
        workbook = xlsxwriter.Workbook('ecp5_oc_usbhostslave.xlsx')
        #worksheet2 = workbook.add_worksheet('sheetname')
        sheet = workbook.add_worksheet('sheetname')
        l = 0
        for line in (read):
            print(line)
            r = 0
            for i in (line):
                print(i)
                if ( l==0 or r==17 or r==19 or r==20 or r==22 or r==23 ):
                    sheet.write(l, r, i)
                elif (r==0 or r==1 or r==4 or r==5 or r==6 or r==7 or r==8 or r==9 or r==10 or r==11 or r==12 or r==13 or r==14 or r==15 or r==16 or r==17 or r==18 or r==21 or r==24):
                    sheet.write(l, r, int(i))
                else:
                    sheet.write(l,r,float(i)) 
                r = r + 1
            l = l + 1
        workbook.close()
if __name__ == '__main__':
    csv_to_xlsx()