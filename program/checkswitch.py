import pexpect
import sys
import datetime
import pymssql
import os

today=datetime.date.today().strftime('%Y%m%d')
path = "/root/xunjian/"+today
os.mkdir(path,777)#创建目录

def Switch(name,ip,passwd):
    try:#try except 防止有一个命令错误，导致程序不能进行，其实不加也可以，如果有命令没输出，下一个代码也会报错。
        name1="---- More ----"#模拟交换机出现的翻页提示
        child=pexpect.spawn('telnet %s'%ip)
        fout=open('/root/xunjian/'+today+'/'+'%s-%s.txt'%(name,ip),'wb+')
        child.logfile = fout
        child.expect('login:')#提示用户登录，输入帐号，交换机不同，有所不同。
        child.sendline("admin")
        child.expect('(?i)ssword:')#提示输入密码
        child.sendline("%s"%passwd)            
        child.expect('<%s>'%name)
        child.sendline("display cpu-usage")#查看cpu状态
        child.expect('<%s>'%name)
        child.sendline("display memory")#查看内存状态
        child.expect('<%s>'%name)
        child.sendline("display  environment")#运行温度
        child.expect('<%s>'%name)
        child.sendline("display fan")#风扇状态，一般输出都有2个
        child.expect('<%s>'%name)
        child.sendline("display power")#电源状态
        child.expect('<%s>'%name)
        child.sendline("display ip routing-table")#路由表
        for i in range(10):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("display interface brief")#端口状态
                break
        for i in range(10):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("dis  version")#版本，为了看运行时间
                break
        for i in range(10):
            index = child.expect([name1,'<%s>'%name])
            if ( index == 0 ):
                child.send(" ")
            else:
                child.sendline("display log")#日志，日志较多，循环100个空格，怕输出不全。
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

host = 'x.x.x.x'#连接数据库，抓取数据库内的信息，交换机的名字、ip、密码
user = 'sa'
pwd = 'xxxx'
db = 'MAC'
conn = pymssql.connect(host=host,user=user,password=pwd,database=db,timeout=1,login_timeout=1,charset="utf8")
cur = conn.cursor()
sqls ="select * from [dbo].[F5HJSwitch]"
cur.execute(sqls)
listall = cur.fetchall()#SQl输出内容导成列表
for line in listall:
    Switch(line[1],line[2],line[3])
conn.commit()
conn.close()

