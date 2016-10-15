# ws://140.92.26.45:8000/object/56fa911c36b24acd62000058/viewer

import websocket

websocket.enableTrace(True)
#ws = websocket.create_connection("ws://wot.city/object/57615d8a54242e1f2a000ee5/viewer")
ws = websocket.create_connection("ws://192.168.1.122:8000/object/56fa911c36b24acd62000058/viewer")

while True:
	result = ws.recv()
	print "Received '%s'" % result