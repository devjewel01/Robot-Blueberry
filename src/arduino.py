#!/usr/bin/env python3
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

def get_command(command):
    command += "\n"
    ser.write(command.encode('utf-8'))



