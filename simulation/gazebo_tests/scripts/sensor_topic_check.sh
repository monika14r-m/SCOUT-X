#!/bin/bash

echo "Checking active ROS2 sensor topics..."

ros2 topic list

echo ""
echo "Checking IMU topic..."
ros2 topic info /imu

echo ""
echo "Checking camera topic..."
ros2 topic info /camera/image

echo ""
echo "Checking LiDAR topic..."
ros2 topic info /scan
