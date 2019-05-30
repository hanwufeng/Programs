# -*- coding: utf-8 -*-
#!/usr/bin/env python
import ciscolib
 
def main():
    PASSWORD="Getinpsg2"  #//测试环境
    USERNAME="admin"
    ENABLE_PWD="SWEternal1"
 
    for ip in open('sw3560.txt').readlines():
        ip = ip.strip()
 
        if USERNAME != "":
            switch = ciscolib.Device(ip, PASSWORD, USERNAME, ENABLE_PWD)
        else:
            switch = ciscolib.Device(ip, PASSWORD, enable_password=ENABLE_PWD)
 
        try:
            switch.connect()
            print("Logged into %s,Successful" % ip)
        except ciscolib.AuthenticationError as e:
            print("Couldn't connect to %s: %s" % (ip, e.value))
            continue
        except Exception as e:
            print("Couldn't connect to %s: %s" % (ip, str(e)))
            continue
 
        switch.enable(ENABLE_PWD)
        switch.cmd("enable")
        switch.cmd("c#andphp\n")
        switch.cmd("show run:")
        switch.cmd("wr")
        switch.cmd(ip + "config.text")  #//自动变化配置文件名称
        switch.disconnect()
 
if __name__ == '__main__':
    main()
