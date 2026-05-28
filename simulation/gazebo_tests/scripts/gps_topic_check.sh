#!/bin/bash

echo "Checking GPS topic availability..."

ros2 topic list | grep gps

echo ""
echo "Streaming GPS telemetry..."
echo "Press CTRL+C to stop"

ros2 topic echo /gps/fix
