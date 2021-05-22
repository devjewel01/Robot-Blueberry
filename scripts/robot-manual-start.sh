#!/bin/bash

sudo systemctl stop robot.service
/home/pi/env/bin/python -u /home/pi/Robot-Blueberry/src/main.py --project_id 'test-e557a' --device_model_id 'test-e557a-robot-x5kmax'