import pexpect
import sys
import datetime
import pymssql
import os

today=datetime.date.today().strftime('%Y%m%d')
path = "/root/xunjian/"+today
os.mkdir(path,777)#����Ŀ¼

def Switch(name,ip,passwd):
    try:#try except ��ֹ��һ��������󣬵��³����ܽ��У���ʵ����Ҳ���ԣ����������û�������һ������Ҳ�ᱨ��
        name1="---- More ----"#ģ�⽻�������ֵķ�ҳ��ʾ
        child=pexpect.spawn('telnet %s'%ip)
        fout=open('/root/xunjian/'+today+'/'+'%s-%s.txt'%(name,ip),'wb+')
        child.logfile = fout
        child.expect('login:')#��ʾ�û���¼�������ʺţ���������ͬ��������ͬ��
        child.sendline("admin")
        child.expect('(?i)ssword:')#��ʾ��������
        child.sendline("%s"%passwd)            
        child.expect('<%s>'%name)
        child.sendline("display cpu-usage")#�鿴cpu״̬
        child.expect('<%s>'%name)
        child.sendline("display memory")#�鿴�ڴ�״̬
        child.expect('<%s>'%name)
        child.sendline("display  environment")#�����¶�
        child.expect('<%s>'%name)
        child.sendline("display fan")#����״̬��һ���������2��
        child.expect('<%s>'%name)
        child.sendline("display power")#��Դ״̬
        child.expect('<%s>'%name)
        child.sendline("display ip routing-table")#·�ɱ�
        for i in range(10):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("display interface brief")#�˿�״̬
                break
        for i in range(10):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("dis  version")#�汾��Ϊ�˿�����ʱ��
                break
        for i in range(10):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("display log")#��־����־�϶࣬ѭ��100���ո��������ȫ��
                break                  
        for i in range(100):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("quit")
                break
    except:
        pass

host = 'x.x.x.x'#�������ݿ⣬ץȡ���ݿ��ڵ���Ϣ�������������֡�ip������
user = 'sa'
pwd = 'xxxx'
db = 'MAC'
conn = pymssql.connect(host=host,user=user,password=pwd,database=db,timeout=1,login_timeout=1,charset="utf8")
cur = conn.cursor()
sqls ="select * from [dbo].[F5HJSwitch]"
cur.execute(sqls)
listall = cur.fetchall()#SQl������ݵ����б�
for line in listall:
    Switch(line[1],line[2],line[3])
conn.commit()
conn.close()

