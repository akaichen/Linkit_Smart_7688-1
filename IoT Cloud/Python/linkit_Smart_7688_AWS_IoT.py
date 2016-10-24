# **************************************************************************************************************************
# Version:     2016.06.30 
# Author:      Archer Huang
# License:     MIT
# Description: Linkit Smart 7688 Duo + Arduino Code + Bridge + AWS
# **************************************************************************************************************************
# 
# 1. update opkg & install wget & disable bridge
# 	 opkg update
# 	 opkg install wget
# 	 uci set yunbridge.config.disabled=0
# 	 uci commit
#
# 2. install setuptools
#	 curl https://bootstrap.pypa.io/ez_setup.py -k -o - | python
#
# 3. install six
# 	 wget --no-check-certificate https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz
# 	 tar zxvf six-1.10.0.tar.gz
#	 cd six-1.10.0
#	 python setup.py install
#
# 4. install Websocket
#	 wget --no-check-certificate https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz
#	 tar zxvf websocket_client-0.32.0.tar.gz
#	 cd websocket_client-0.32.0
#	 python setup.py install
#
# **************************************************************************************************************************

import time
import sys  
import websocket
import socket
import datetime
import paho.mqtt.client as paho
import ssl
import os
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = "a2h61tdmtpgw89.iot.ap-southeast-1.amazonaws.com"
awsport = 8883
clientId = "sensorData"
thingName = "sensorData"
caPath = "./root-CA.crt"
certPath = "./76cb8e72f9-certificate.pem.crt"
keyPath = "./76cb8e72f9-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while True:
	celsius = value.get("h")
	print "%d degrees Celsius" % float(celsius)
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	if connflag == True:
		mqttc.publish("temperature", json.dumps({"time": date, "temperature": celsius}), qos=1)
	else:
		print("waiting for connection...")
	time.sleep(1)
	