#-*- coding: utf-8 -*-


__author__ = 'wangfangfang'

'''


kc_vp_down="kc_vp_down"

f=open("E:\\file\\testtest.txt")

f_line=f.readline()

while f_line:
    print f_line

    f_line=f.readline()

f.close()
'''

'''
import re

text=open("E:\\pyfile\\2017-6-13task_log_xp.log").read()

num=re.findall(r"\bkc_vp_down=(\d+)",text)

print (num)

sum_num=[int(n) for n in num]

print("Sum is %d"%sum(sum_num))
'''


import re
import xlwt
'''
text=open("E:\\pyfile\\11.txt").read()
print (text)

num=re.findall(r"\bdownload_time:(\d+)",text)

print (num)

sum_num=[int(n) for n in num]

print("Sum is %d"%sum(sum_num))
'''
'''
text=open("C:\\p2plog\\p2p_0.log").read()

num=re.findall(r"\bdownload_time:(\d+)",text)

print (num)

sum_num=[int(n) for n in num]

print("Sum is %d"%sum(sum_num))
'''


def getvalue(road,test_str):
 workbook = xlwt.Workbook()
 sheet = workbook.add_sheet('shuju')
 #with open("E:\\pyfile\\2017-6-13task_log_xp.log",'rb') as text:
 with open(road,'rb') as text:
    #print ("a",text.readline())
    sum_all=0
    num=0
    i=0
    for line in text.readlines():
        #print ("b",line)
        sline=str(line)
        #print ("c",sline)
        #dltime=re.findall(r"\bkc_vp_time=(\d+)",sline)
        dltime=re.findall(test_str,sline)
        if len(dltime)!=0:
          #print ("a",dltime)
          dltime_list=[int(n) for n in dltime]
          #print ("bbb",dltime_list)
          print (dltime_list[0])

          sheet.write(i,0,label = dltime_list[0])

          list_sum=sum(dltime_list)
          #print ("单行的和为：",list_sum)
          sum_all+=list_sum
          num+=1
          i=i+1
 l=i
 print ("sum_all:",sum_all)
 sheet.write(l+1,0,label = sum_all)
 print ("num:",num)
 sheet.write(l+2,0,label = num)
 print ("average value:",sum_all/num)
 sheet.write(l+3,0,label = sum_all/num)
 workbook.save('Excel11.xls')



road1="C:\\p2plog\\p2p_0.log"
#正则表达式匹配字段download_time:，并读出该字段的值
test_strr=r"\bdownload_time:(\d+)"
getvalue(road1,test_strr)
