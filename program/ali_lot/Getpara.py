#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
 
 
"""
file: Get_para.py
date: 20171111
author: S_L_zheng
function: return client_id, username, password.
"""
 
import time
import hmac
import hashlib
import math
 
 
class Get_para(object):
 
    def __init__(self, PK, DN, DS):
        self.ProductKey = PK
        self.DeviceName = DN
        self.DeviceSecret = DS
 
    def get_para(self):
        ProductKey = self.ProductKey
        ClientId = self.DeviceName
        DeviceName = self.DeviceName
        DeviceSecret = self.DeviceSecret
 
        signmethod = "hmacsha1"
        us = math.modf(time.time())[0]
        ms = int(round(us * 1000))
        timestamp = str(ms)
        data = "".join(("clientId", ClientId, "deviceName", DeviceName,
                        "productKey", ProductKey, "timestamp", timestamp))
 
        ret = hmac.new(bytes(DeviceSecret, encoding='utf-8'),
                       bytes(data, encoding='utf-8'),
                       hashlib.sha1).hexdigest()
        sign = ret
 
        client_id = "".join((ClientId,
                             "|securemode=3",
                             ",signmethod=", signmethod,
                             ",timestamp=", timestamp,
                             "|"))
        username = "".join((DeviceName, "&", ProductKey))
        password = sign
        return client_id, username, password
 
if __name__ == '__main__':
	instance = Get_para(PK='YurProductKey', DN='YourDeviceName', DS='YourDeviceSecret')
	client_id, username, password = instance.get_para()
	print('client_id:',client_id)
	print('username:', username)
	print('password:', password)
	 
