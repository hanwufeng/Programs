#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
 
 
"""
file: Sub_Client.py
date: 20171111
author: S_L_zheng
function: Subscribe Topic.
"""
 
 
import paho.mqtt.client as mqtt
import Get_para
 
DeviceName = "YourDeviceName"
DeviceSecret = "YourDeviceSecret "
ProductKey = "YourProductKey "
 
 
res = Get_para.Get_para(PK=ProductKey, DN=DeviceName, DS=DeviceSecret)
paras = res.get_para()
client_id = paras[0]
username = paras[1]
password = paras[2]
 
strBroker = ProductKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
port = 1883
 
topic = ProductKey+'/'+DeviceName+'/'+'data'
 
 
def on_connect(mqttc, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    mqttc.subscribe(topic)
 
 
def on_message(mqttc, userdata, msg):
    msgpayload = str(msg.payload, encoding='utf-8')
    print(msgpayload)
 
 
def on_subscribe(mqttc, userdata, mid, granted_qos):
    print('on_subscribe')
 
 
def on_publish(mqttc, userdata, mid):
    print('on_publish')
 
 
if __name__ == '__main__':
    mqttc = mqtt.Client(client_id)
    mqttc.username_pw_set(username, password)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_subscribe = on_subscribe
    mqttc.on_publish = on_publish
    mqttc.connect(strBroker, port, 120)
    mqttc.loop_forever()
 
