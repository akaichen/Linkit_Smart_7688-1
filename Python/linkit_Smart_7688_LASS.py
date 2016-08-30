# **************************************************************************************************************************
# Version:     2016.06.30 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + Websocket Python + WoT
# **************************************************************************************************************************
# 
# 1. update opkg & install wget & disable bridge
# 	 opkg update
# 	 opkg install wget
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#
# 2. install mqtt & httplib
#	 pip install paho-mqtt
#    pip install httplib2
#
# **************************************************************************************************************************

import time
import sys  
import websocket
import socket
import datetime
import paho.mqtt.client as mqtt
import ssl
import os
import httplib, urllib

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

connflag = False

# **************************************************************************************************************************
# Ref: https://www.mathworks.com/help/thingspeak/update-channel-feed.html
#
# POST https://api.thingspeak.com/update.json
# api_key = R4P5W2047WSYO8S8
# field1 = 19
# **************************************************************************************************************************

ApiKey = "R4P5W2047WSYO8S8"

################################################################
# Please configure the following settings for your environment

MQTT_SERVER = "gpssensor.ddns.net"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC = "LASS/Test/PM25"
#MQTT_TOPIC = "DeveloperTest"
#MQTT_TOPIC = "LASS/Test/#"

################################################################

# http://nrl.iis.sinica.edu.tw/LASS/show.php?device_id=Temperature_1024

ver_format=3
fmt_opt=1
app="LinkItSmart7688-Archer"
ver_app="0.0.3"
device_id="Archer_Temp_Humi_Dust"
device="LinkItSmart7688Duo"
tick=0
datestr="2016-08-30"
timestr="15:50:01"
gps_fix=0
gps_num=0
gps_alt=0
gps_lat=25.0336762
gps_lon=121.5404092

#msg example


packstr = "PPP25|ver_format=%i|fmt_opt=%i|app=%s|ver_app=%s|device_id=%s|device=%s" % (ver_format,fmt_opt,app,ver_app,device_id,device)
packstr_fix = "|tick=%i|date=%s|time=%s|gps_fix=%i|gps_num=%i|gps_alt=%i|gps_lat=%f|gps_lon=%f" % (tick,datestr,timestr,gps_fix,gps_num,gps_alt,gps_lat,gps_lon)
print "%s%s" %(packstr,packstr_fix)

connflag = False

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )
    client.subscribe(MQTT_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_start()	

while True:
    d0 = value.get("d")
    h0 = value.get("h")
    t0 = value.get("t")
    print "Dust: " + d0
    print "Humi: " + h0
    print "Temp: " + t0

    packstr_sensor="|s-t0==%s|s-h0=%s|s-d0=%s" %(t0,h0,d0)
    payload = packstr + packstr_fix + packstr_sensor

    print "send payload: " + payload

    if connflag == True:
        print "packstr_sensor: " + packstr_sensor
        mqtt_client.publish(MQTT_TOPIC, payload, qos=1)
    else:
        print("waiting for connection...")
    time.sleep(1)