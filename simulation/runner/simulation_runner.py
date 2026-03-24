from simulation.telemetry.telemetry_engine import TelemetryEngine
import socket,json, time

engine = TelemetryEngine()

HOST = "127.0.0.1"
PORT = 9999

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True :
  data = engine.update()
  sock.sendto(json.dumps(data).encode(),(HOST,PORT))
  print("[SIMULATION]",data)
  time.sleep(1)
