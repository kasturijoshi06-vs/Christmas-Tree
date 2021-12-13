import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    message = json.loads(message.decode("utf-8"))
    print("Received request: " + str(message))
    if message["game_start"] == "True":
       print("received")
	    # Send reply back to client
       socket.send(b"Started")

