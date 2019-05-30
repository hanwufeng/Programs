# -*- coding: utf-8 -*-
#!/usr/bin/env python
import paramiko
import time
import getpass
 
username = input("nxp84216:")
password = getpass.getpass("M!dmnm3825s:")
 
f = open("iplist.txt","r")
for line in f.readlines():
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password)
        print("Sucessfully login to "), ip
        command = ssh_client.invoke_shell()
        command.send("enable\n")
        command.send("c#andphp\n")
        command.send("copy running ftp:\n")
        command.send("192.168.1.5\n")
        command.send (ip + "config.text\n")  #//这里不要设置交换机命令exit退出，否则会出现问题，这里掉过一个坑。
        time.sleep(1)
        output = command.recv(65535)
        print (output)
f.close()
ssh_client.close
