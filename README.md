# SCOUT-X
Secure Commands and Operations for UAV Telemetry - eXtended
SCOUT-X is a real-time anti-hijacking security framework designed specifically to protect unmanned aerial vehicles (UAVs) from unauthorized control takeover

Modern drones rely on wireless communication between the ground control station and the flight controller for navigation and mission execution. While communication channels may use encryption, the drone’s control layer remains vulnerable to command injection, replay attacks, spoofed control sources, and abnormal command bursts

SCOUT-X introduces a control-layer security engine that intercepts and validates all incoming flight commands before execution. The system enforces authenticated command integrity, analyzes behavioral flight patterns in real time, and activates automatic mitigation mechanisms such as safe-hover or return-to-home when hijacking attempts are detected

By shifting protection from network-level monitoring to runtime control enforcement, SCOUT-X enhances drone resilience against remote takeover attacks

## Drone Simulation

The drone simulation module is used to replicate real drone behavior without physical hardware.

It generates live telemetry data such as GPS coordinates, altitude, and battery levels, and streams it to the ground control system. This allows testing of communication and system behavior in a controlled environment.

The simulation helps validate data flow and system responses before deploying on an actual drone.

### How to Run
1. Run ground_control.py  
2. Run drone_sim.py  

### Sample Output
{"gps": {"lat": 12.9717, "lon": 77.5947}, "altitude": 10, "battery": 99.5}
