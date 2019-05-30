import pymssql
import xlwt
import datetime
from xlwt import *

today=datetime.date.today().strftime('%Y%m%d')
txt='F51FA-HJ-S5560X-x.x.x.x.txt'#���豸��������Ϣ����������ѭ�������еģ���Ϊ��Щ�豸��������ո�ȡ�
file = open('/root/xunjian/'+today+'/'+txt,'r+')

listlist=file.readlines()#��ȡ�ĵ���ÿһ�У����б��������˫��Դ�����⣬ֱ�� for line in file.readlines():
i=1
for line in listlist:#��ȡ�б�ÿһ�У���Ϊ������Դ�����������Ϣ��һ����ֻ��ƥ��ؼ��ֺ������һ���ַ�����ʵ�����Ρ�

    if '1       Normal' in line:
        power11=line[8:15].rstrip()#�豸״̬������ƥ��ؼ��֣�Ȼ���ȡ�������ַ�����������Ҫ���Լ��Ρ�
        print(power11)#ȷ��������Լ���Ҫ���ַ�����
    if 'Uptime is' in line:#����ʱ��
        time11=line[-33:].rstrip()
        print(time11)
    if 'hotspot' in line:
        environment11=line[17:21].rstrip()#�����¶�
        print(environment11)
    if 'Fan 1:' in line:
        fana11=listlist[i+1][-8:].rstrip()#��Դ״̬��ƥ��ؼ��֣���ȡ��һ�е��ַ���
        print(fana11)
    if 'Fan 2:' in line:
        fanb11=listlist[i+1][-8:].rstrip()#��Դ״̬��ƥ��ؼ��֣���ȡ��һ�е��ַ���
        print(fanb11)
    if 'in last 5 minutes' in line:
        cpu11=line[6:10].rstrip()#cpuʹ����
        print(cpu11)
    if 'Mem:' in line:
        memory11=line[-7:].rstrip()#�ڴ�
        print(memory11)
    if 'To_F5-Core-S12508_Ten-G1' in line:#�˿�
        briefa11=line[20:30].rstrip()
        print(briefa11)
    if 'To_F5-Core-S12508_Ten-G2' in line:
        briefb11=line[20:30].rstrip()
        print(briefb11)
    if 'Current messages:' in line:#��־��Ŀ
        log11=line[-5:].rstrip()
        print(log11)
    if 'Routes' in line:
        routingtable11=line[-5:].rstrip()#·����Ŀ
        print(routingtable11)
    i += 1

workbook = xlwt.Workbook()#�������

style = XFStyle()#��ʼ����ʽ������ʽ�����˵�Ԫ�񱳾���ɫ�͵�Ԫ��߿��������ԡ�
pattern = Pattern()
pattern.pattern = Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = Style.colour_map['blue'] #���õ�Ԫ�񱳾�ɫΪ��ɫ
style.pattern = pattern
borders = xlwt.Borders()#���ñ��ı߿�1��Ĭ��ʵ�ߺ�ɫ��
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
style.borders = borders


style1 = XFStyle()#ֻ�б߿�
borders = xlwt.Borders()
borders.left = 1
#borders.left = xlwt.Borders.THIN
borders.right = 1
borders.top = 1
borders.bottom = 1
style1.borders = borders

style3 = XFStyle()#��ʼ����ʽ�����߿�ͱ�����ݾ��С�
borders = xlwt.Borders()
borders.left = 1
#borders.left = xlwt.Borders.THIN
borders.right = 1
borders.top = 1
borders.bottom = 1
style3.borders = borders
al = xlwt.Alignment()
al.horz = 0x02      # ����ˮƽ����
al.vert = 0x01      # ���ô�ֱ����
style3.alignment = al

F51FSwitch = workbook.add_sheet('F51FSwitch',cell_overwrite_ok=True)#��������ĳһ��ҳ

first_col=F51FSwitch.col(0)#����0��1��2��3�е��п�
sec_col=F51FSwitch.col(1)
thr_col=F51FSwitch.col(2)
for_col=F51FSwitch.col(3)
first_col.width=150*25
sec_col.width=100*25
thr_col.width=120*25
for_col.width=320*25

F51FSwitch.write_merge(1,11,0,0,'QCMC-F5-1FA',style3)#�ϲ���Ԫ��(1,11Ϊ��1��11�� 0,0Ϊ��0��0)����������
#F51FSwitch.write_merge(1,10,0,1,'QCMC-F3-1FA')#�ϲ�0��1�У�1��10��
F51FSwitch.write_merge(1,11,1,1,'10.20.5.1',style3)#���style3����ʽ��ֻ����дһ�������Գ�ʼ����ʽ��ʱ�����������Ӷ�����ԡ�
F51FSwitch.write(0,0,'�豸����',style)
F51FSwitch.write(0,1,'�����ַ',style)
F51FSwitch.write(0,2,'�����',style)
F51FSwitch.write(0,3,'�����',style)
F51FSwitch.write(1,2,'�豸״̬',style1)
F51FSwitch.write(2,2,'����ʱ��',style1)
F51FSwitch.write(3,2,'�����¶�',style1)
F51FSwitch.write(4,2,'����A״̬',style1)
F51FSwitch.write(5,2,'����B״̬',style1)
F51FSwitch.write(6,2,'CPUʹ����',style1)
F51FSwitch.write(7,2,'�ڴ�ʹ����',style1)
F51FSwitch.write(8,2,'�ۺϿ�A',style1)
F51FSwitch.write(9,2,'�ۺϿ�B',style1)
F51FSwitch.write(10,2,'��־��Ŀ',style1)
F51FSwitch.write(11,2,'·����Ŀ',style1)
F51FSwitch.write(1,3,power11,style1)#���ץȡ���ַ�������Ӧ�ı��
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

print ('����excel�ļ���ɣ�')
workbook.save('/root/xunjian/%sF5Switchxunjian.xls'%today)