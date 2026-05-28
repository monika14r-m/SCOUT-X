#!/bin/bash
echo "Checking GPS topic..."
rostopic echo /gps/fix
