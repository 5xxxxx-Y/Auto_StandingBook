from hashlib import new
from types import new_class
import pandas as pd
from sqlalchemy import false, true
import chardet
import re



print("===============================开始咯===============================")
#这里的1和22，就是1号到22号

new_all_211304=false
new_all_211309=false
new_all_181304=false
cla211304_1=[]
cla211309_1=[]
cla181304_1=[]
fashao=[]
d_max_2=28
d_max_3=10
d_max_4=30
d_max_5=31
d_max_6=30
d_max_7=6
temp_m=0
temp_d1=0
temp_d2=0
first_3=0
first_4=0
first_5=0
first_6=0
first_7=0
for m1 in range(6,8):
    m2=m1
    if(m1==3):
        d_max=d_max_3
    if(m1==4):
        d_max=d_max_4
    if(m1==5):
        d_max=d_max_5
        d_min=27
    if(m1==6):
        d_max=d_max_6
        d_min=22
    if(m1==7):
        d_max=d_max_7
        d_min=0
    for d1 in range(d_min,d_max):
        cc=0
        tt=0
        ct_211304=0
        ct_211309=0
        ct_181304=0
        tt_211304=0
        tt_211309=0
        tt_181304=0
        d2=d1+1
        if(d1==0 and m1==3):
            temp_m=m1
            m1=m1-1
            temp_d1=d1
            d1=d_max_2
            first_3=1
        if(d1==0 and m1==4):
            temp_m=m1
            m1=m1-1
            temp_d1=d1
            d1=d_max_3
            first_4=1
        if(d1==0 and m1==5):
            temp_m=m1
            m1=m1-1
            temp_d1=d1
            d1=d_max_4
            first_5=1
        if(d1==0 and m1==6):
            temp_m=m1
            m1=m1-1
            temp_d1=d1
            d1=d_max_5
            first_6=1
        if(d1==0 and m1==7):
            temp_m=m1
            m1=m1-1
            temp_d1=d1
            d1=d_max_6
            first_7=1
        new_all=false
        temp_all=false
        #这里是你存放文件的目录
        path_1 = r"C:/Users/5x/Desktop/文件/猪的台账/2022"+str(m1).zfill(2)+str(d1).zfill(2)+"（艺术）五邑大学学生健康.xlsx"
        path_2 = r"C:/Users/5x/Desktop/文件/猪的台账/2022"+str(m2).zfill(2)+str(d2).zfill(2)+"（艺术）五邑大学学生健康.xlsx"
        new_day=str(m2).zfill(2)+"月"+str(d2).zfill(2)+"号"
        print("\n"+"[+]"+new_day,end=' ')
        data_1_1=pd.read_excel(path_1)
        
        data_2_2=pd.read_excel(path_2)
        max_column_1=data_1_1.shape[0]
        max_column_2=data_2_2.shape[0]
        data_1 = pd.DataFrame(data_1_1)#读取数据,设置None可以生成一个字典，字典中的key值即为sheet名字，此时不用使用DataFram，会报错
        data_2 = pd.DataFrame(data_2_2)
        
        all_result_1=data_1['定位信息']
        all_result_2=data_2['定位信息']
        
        #result_1 = data_1['']#获取列内容
        #result_2 = data_2[3:5]
        class_1=data_1['班级']
        class_2=data_2['班级']
        name_1=data_1['姓名']
        name_2=data_2['姓名']
        temp=data_2['本日您是否有发烧症状（体温37.3℃以上）']
        # print("│───────────────────────────────────────────────────────────│")
        # print("│────────────────正在筛选离市及发烧de同学───────────────────│")
        print("正在筛选离市及发烧de同学",end=' ')
        for i in range(0,max_column_1):
            for j in range(0,max_column_2):
                #print(name_1[i]+','+chardet.detect(name_1[i])+','+name_2[j]+chardet.detect(name_2[j]))
                if(name_1[i]==name_2[j]):
                    #print(name_1[i]+','+name_2[j])
                    #找离市
                    if(re.findall("省([\u4e00-\u9fa5][\u4e00-\u9fa5][\u4e00-\u9fa5])",all_result_1[i])!=re.findall("省([\u4e00-\u9fa5][\u4e00-\u9fa5][\u4e00-\u9fa5])",all_result_2[j])):
                        #print(re.findall("省([\u4e00-\u9fa5][\u4e00-\u9fa5][\u4e00-\u9fa5])",all_result_1[i])re.findall("省([\u4e00-\u9fa5][\u4e00-\u9fa5][\u4e00-\u9fa5])",all_result_2[i]))
                        #print(all_result_1[i][3:5])
                        #！！！！班名在这里修改
                        if((class_2[j]==211304) or (class_2[j]==211309) or (class_2[j]==181304)):
                            if(class_1[i]==class_2[j]):
                                new_all=true
                                new_data="离开{}到{}".format(all_result_1[i][0:9],all_result_2[j][0:9])
                                new_people=name_2[j]
                                new_classes=class_2[j]
                                if(class_2[j]==211304):
                                    new_all_211304=true
                                    ct_211304=1
                                    cla211304_1.append(new_day)
                                    cla211304_1.append(new_people)
                                    cla211304_1.append(new_data)
                                # if(ct_211304==0 and tt_211304==0):
                                #     tt_211304=1
                                #     cla211304_1.append(new_day)
                                #     cla211304_1.append("没没没")
                                #     cla211304_1.append("没没没没没没没没没没没没没没没没没没没没没")
                                if(class_2[j]==211309):
                                    new_all_211309=true
                                    ct_211309=1
                                    cla211309_1.append(new_day)
                                    cla211309_1.append(new_people)
                                    cla211309_1.append(new_data)
                                # if(ct_211309==0 and tt_211309==0):
                                #     tt_211309=1
                                #     cla211309_1.append(new_day)
                                #     cla211309_1.append("没没没")
                                #     cla211309_1.append("没没没没没没没没没没没没没没没没没没没没没")
                                if(class_2[j]==181304):
                                    new_all_181304=true
                                    ct_181304=1
                                    cla181304_1.append(new_day)
                                    cla181304_1.append(new_people)
                                    cla181304_1.append(new_data)
                                # if(ct_181304==0 and tt_181304==0):
                                #     tt_181304=1
                                #     cla181304_1.append(new_day)
                                #     cla181304_1.append("没没没")
                                #     cla181304_1.append("没没没没没没没没没没没没没没没没没没没没没")
                    #找发烧
                    #！！！！！这里也要改班名
                    if(temp[j]=='是' and (class_2[j]==211304 or class_2[j]==211309 or class_2[j]==181304)):
                        fashao.append(new_day)
                        fashao.append(class_2[j])
                        fashao.append(name_2[j])
                        
                        print("！！！！！！",class_2[j],"de",name_2[j]+"发烧！！！！！！",end='')
                        temp_all=true
                    #break
        if(temp_all==false):
            print("当日没有发烧de同学",end=' ')
            # print("│───────────────────────────────────────────────────────────│")
            # print("---------------------当日没有发烧de同学----------------------")
        if(new_all==false):
            print("当日没有离市de同学",end=' ')
        #     print("│───────────────────────────────────────────────────────────│")
        #     print("---------------------当日没有离市de同学----------------------")
        else:
            if(ct_181304==1):
                print("181304有离市",end=' ')
            if(ct_211304==1):
                print("211304有离市",end=' ')
            if(ct_211309==1):
                print("211309有离市",end=' ')
        #d2=temp_d2
        if(d1>d2):
            m1=temp_m
            d1=0
print('')
if(temp_all==true):
    z=0
    for i in fashao:
        if(z%3==0):
            print('')
        print(i,end=' ')
        z+=1

#if(new_all_211304==true):
print("")
print("")
if(1):
    print("211304")
    j=0
    #print("│───────────────────────────────────────────────────────────│")
    #print("│",end='')
    for i in cla211304_1:
        if(j%3==0 and j!=0):
            print("")
            #print("│")
            print("─────────────────────────────────────────────────────────────")
            #print("│──────────────────────────────────────────────────│")
            #print("│",end='')        
        j+=1
        print(i,end=' ')
    #print("│")
    #print("│───────────────────────────────────────────────────────────│\n")
print("")
print("")
if(1):
    print("211309")
    j=0
    #print("│───────────────────────────────────────────────────────────│")
    #print("│",end='')
    for i in cla211309_1:
        if(j%3==0 and j!=0):
            print("")
            #print("│")
            print("─────────────────────────────────────────────────────────────")
            #print("│──────────────────────────────────────────────────│")
            #print("│",end='')        
        j+=1
        print(i,end=' ')
    #print("│")
    #print("│───────────────────────────────────────────────────────────│\n")
print("")
print("")
if(1):
    print("181304")
    j=0
    #print("│───────────────────────────────────────────────────────────│")
    #print("│",end='')
    for i in cla181304_1:
        if(j%3==0 and j!=0):
            print("")
            #print("│")
            print("─────────────────────────────────────────────────────────────")
            #print("│──────────────────────────────────────────────────│")
            #print("│",end='')        
        j+=1
        print(i,end=' ')
    #print("│")
    #print("│───────────────────────────────────────────────────────────│\n")
print("\n")
print("==============================结束啦啦啦==============================")
# def write():
#     df = pd.read_excel(r"C:/Users/Y/OneDrive/桌面/猪的台账/艺术设计学院（部）"+str(new_classes)+"班学生寒假期间健康台账")
#     df_ok=df.set_index('姓名',inplace=True)
#     df.at['{}'.format(new_people),'{}'.format()]=new_data

   