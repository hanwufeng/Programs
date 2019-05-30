import pymssql
import xlwt
import datetime
from xlwt import *

today=datetime.date.today().strftime('%Y%m%d')
txt='F51FA-HJ-S5560X-x.x.x.x.txt'#打开设备的配置信息，不建议用循环打开所有的，因为有些设备的输出会多空格等。
file = open('/root/xunjian/'+today+'/'+txt,'r+')

listlist=file.readlines()#读取文档的每一行，至列表，如果不是双电源的问题，直接 for line in file.readlines():
i=1
for line in listlist:#读取列表每一行，因为两个电源的所有输出信息都一样，只能匹配关键字后输出下一行字符串，实属无奈。

    if '1       Normal' in line:
        power11=line[8:15].rstrip()#设备状态，都是匹配关键字，然后截取本来的字符串输出，这个要多试几次。
        print(power11)#确认输出是自己想要的字符串。
    if 'Uptime is' in line:#运行时间
        time11=line[-33:].rstrip()
        print(time11)
    if 'hotspot' in line:
        environment11=line[17:21].rstrip()#运行温度
        print(environment11)
    if 'Fan 1:' in line:
        fana11=listlist[i+1][-8:].rstrip()#电源状态，匹配关键字，截取下一行的字符串
        print(fana11)
    if 'Fan 2:' in line:
        fanb11=listlist[i+1][-8:].rstrip()#电源状态，匹配关键字，截取下一行的字符串
        print(fanb11)
    if 'in last 5 minutes' in line:
        cpu11=line[6:10].rstrip()#cpu使用率
        print(cpu11)
    if 'Mem:' in line:
        memory11=line[-7:].rstrip()#内存
        print(memory11)
    if 'To_F5-Core-S12508_Ten-G1' in line:#端口
        briefa11=line[20:30].rstrip()
        print(briefa11)
    if 'To_F5-Core-S12508_Ten-G2' in line:
        briefb11=line[20:30].rstrip()
        print(briefb11)
    if 'Current messages:' in line:#日志条目
        log11=line[-5:].rstrip()
        print(log11)
    if 'Routes' in line:
        routingtable11=line[-5:].rstrip()#路由条目
        print(routingtable11)
    i += 1

workbook = xlwt.Workbook()#创建表格

style = XFStyle()#初始化样式，此样式包含了单元格背景颜色和单元格边框两个属性。
pattern = Pattern()
pattern.pattern = Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = Style.colour_map['blue'] #设置单元格背景色为蓝色
style.pattern = pattern
borders = xlwt.Borders()#设置表格的边框，1是默认实线黑色。
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
style.borders = borders


style1 = XFStyle()#只有边框
borders = xlwt.Borders()
borders.left = 1
#borders.left = xlwt.Borders.THIN
borders.right = 1
borders.top = 1
borders.bottom = 1
style1.borders = borders

style3 = XFStyle()#初始化样式，带边框和表格内容居中。
borders = xlwt.Borders()
borders.left = 1
#borders.left = xlwt.Borders.THIN
borders.right = 1
borders.top = 1
borders.bottom = 1
style3.borders = borders
al = xlwt.Alignment()
al.horz = 0x02      # 设置水平居中
al.vert = 0x01      # 设置垂直居中
style3.alignment = al

F51FSwitch = workbook.add_sheet('F51FSwitch',cell_overwrite_ok=True)#创建表格的某一分页

first_col=F51FSwitch.col(0)#设置0、1、2、3列的列宽
sec_col=F51FSwitch.col(1)
thr_col=F51FSwitch.col(2)
for_col=F51FSwitch.col(3)
first_col.width=150*25
sec_col.width=100*25
thr_col.width=120*25
for_col.width=320*25

F51FSwitch.write_merge(1,11,0,0,'QCMC-F5-1FA',style3)#合并单元格(1,11为行1到11行 0,0为列0到0)，填入内容
#F51FSwitch.write_merge(1,10,0,1,'QCMC-F3-1FA')#合并0到1列，1到10行
F51FSwitch.write_merge(1,11,1,1,'10.20.5.1',style3)#添加style3的样式，只能填写一个，所以初始化样式的时候根据需求添加多个属性。
F51FSwitch.write(0,0,'设备名称',style)
F51FSwitch.write(0,1,'管理地址',style)
F51FSwitch.write(0,2,'检查项',style)
F51FSwitch.write(0,3,'检查结果',style)
F51FSwitch.write(1,2,'设备状态',style1)
F51FSwitch.write(2,2,'运行时间',style1)
F51FSwitch.write(3,2,'运行温度',style1)
F51FSwitch.write(4,2,'风扇A状态',style1)
F51FSwitch.write(5,2,'风扇B状态',style1)
F51FSwitch.write(6,2,'CPU使用率',style1)
F51FSwitch.write(7,2,'内存使用率',style1)
F51FSwitch.write(8,2,'聚合口A',style1)
F51FSwitch.write(9,2,'聚合口B',style1)
F51FSwitch.write(10,2,'日志条目',style1)
F51FSwitch.write(11,2,'路由条目',style1)
F51FSwitch.write(1,3,power11,style1)#添加抓取的字符串到相应的表格
F51FSwitch.write(2,3,time11,style1)
F51FSwitch.write(3,3,environment11,style1)
F51FSwitch.write(4,3,fana11,style1)
F51FSwitch.write(5,3,fanb11,style1)
F51FSwitch.write(6,3,cpu11,style1)
F51FSwitch.write(7,3,memory11,style1)
F51FSwitch.write(8,3,briefa11,style1)
F51FSwitch.write(9,3,briefb11,style1)
F51FSwitch.write(10,3,log11,style1)
F51FSwitch.write(11,3,routingtable11,style1)

print ('创建excel文件完成！')
workbook.save('/root/xunjian/%sF5Switchxunjian.xls'%today)
