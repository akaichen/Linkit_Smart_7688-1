#!/usr/bin/python

import pyupm_grove as grove
import websocket
import datetime
import time

temp = grove.GroveTemp(0)
print temp.name()

websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/57cad2809453b2446f0007de/send")

while True:
    celsius = temp.value()
    print "%d degrees Celsius," % (celsius)

    t = time.time();
    date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
    
    vals = "{\"date\":\""+date+"\",\"temperature\":"+ str(celsius)+"}"
    ws.send(vals);
    time.sleep(1);
   
    