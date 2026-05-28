#!/bin/bash

echo "Checking camera feed topic..."

ros2 topic list | grep camera

echo ""
echo "Displaying camera topic information..."

ros2 topic info /camera/image

echo ""
echo "Camera feed validation complete."
