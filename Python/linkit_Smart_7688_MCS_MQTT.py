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
#	 pip install httplib2 
#
# *********************************************************************

import paho.mqtt.client as mqtt
import time
import sys  
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

# *********************************************************************
# MQTT Config

deviceId = "D7fDOASh"
deviceKey = "eqGDzbxWsKyJqkl7"
dataChnId1 = "Humidity"
dataChnId2 = "Temperature"
MQTT_SERVER = "mqtt.mcs.mediatek.com"
MQTT_PORT = 1883
MQTT_ALIVE = 60
MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId1
MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId2
# *********************************************************************

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE)	

while True:
    h0 = value.get("Humidity")
    t0 = value.get("Temperature")
    payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":h0}}]}
    mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
    payload = {"datapoints":[{"dataChnId":"Temperature","values":{"value":t0}}]}
    mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
    time.sleep(1)