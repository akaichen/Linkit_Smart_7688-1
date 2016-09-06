# *********************************************************************
# Version:     2016.09.06
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + MCS
# *********************************************************************
# 
# 1. update opkg & install wget & disable bridge
# 	 opkg update
# 	 opkg install wget
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#
# 2. install httplib
#	 pip install paho-mqtt
#
# *********************************************************************

import paho.mqtt.client as mqtt
import re
import httplib, urllib
import socket
import sys
import time

deviceId = "D7fDOASh"
deviceKey = "eqGDzbxWsKyJqkl7"
MQTT_SERVER = "mqtt.mcs.mediatek.com"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC = "mcs/" + deviceId + "/" + deviceKey + "/+"

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print("mqtt payload=%s" %(msg.payload))

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)
mqtt_client.loop_forever()