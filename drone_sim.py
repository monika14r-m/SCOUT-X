import socket
import json
import time

HOST = "127.0.0.1"
PORT = 5000

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))

lat = 12.9716
lon = 77.5946
altitude = 0
battery = 100

while True:
  data = {
    "gps": {"lat":lat,"lon":lon},
    "altitude":altitude,
    "battery": battery
  }
sock.sendall((json.dumps(data)+"\n").encode())

#simulate changes
lat += 0.0001
lon +=0.0001
altitude += 1
battery -= 0.1

time.sleep(1)
