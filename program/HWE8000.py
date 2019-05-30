#!/usr/bin/env python

import pexpect

import sys

import datetime

 

d1=datetime.datetime.now()

d3=d1+datetime.timedelta(days=-1)

tdy=d3.strftime('%b %d')

today=datetime.date.today().strftime('%Y%m%d')

 

tt=tdy.split()

if int(tt[-1]) < 10:

  tdy=tdy.replace('0',' ')

 

ip=str(sys.argv[1])

passwd=str(sys.argv[2])

password=str(sys.argv[3])

 

child=pexpect.spawn('ssh 用户名@%s'%ip)

fout=file('/usr/sh/shell/linux/xunjian/'+today+'/01DMZ-E8000E.txt','w')

child.logfile = fout

child.expect('(?i)ssword:')

child.sendline("%s"%passwd)

child.expect('(?i)E8000E-1>')

child.sendline("su")

child.expect("(?i)assword:")

child.sendline("%s"%password)

child.expect("(?i)E8000E-1>")

child.sendline("dis device | ex Normal")

child.expect("(?i)E8000E-1>")

child.sendline("dis version")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis temperature")

child.expect("(?i)E8000E-1>")

child.sendline("dir")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis memory-usage")

child.expect("(?i)E8000E-1>")

child.sendline("dis hrp state")

child.expect("(?i)E8000E-1>")

child.sendline("dis firewall session table")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis ip routing-table protocol static")

child.expect("(?i)E8000E-1>")

child.sendline("dis int brief | in up")

child.expect("(?i)E8000E-1>")

child.sendline("dis acl 3004")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis acl 3005")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis acl 3006")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis acl 3007")

index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

if ( index == 0 ):

  child.send("a")

child.expect("(?i)E8000E-1>")

child.sendline("dis alarm all")

child.expect("(?i)E8000E-1>")

child.sendline("dis logbuffer | in %s"%tdy)

for i in range(20):

  index = child.expect(["(?i)---- More ----","(?i)E8000E-1>"])

  if ( index == 0 ):

    child.send(" ")

  else:

    child.sendline("q")

    break
