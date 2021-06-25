#!/usr/bin/env python

import smbus
import time
import math
from talk import say
import RPi.GPIO as GPIO
import os
import yaml

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
with open('{}/src/configuration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
    sensor = yaml.load(conf, Loader=yaml.FullLoader)
    
gas  = sensor['Sensor']['gas']
fire = sensor['Sensor']['fire']
smoke = sensor['Sensor']['smoke']
ldr  = sensor['Sensor']['smoke']

GPIO.setmode(GPIO.BCM)
GPIO.setup(fire, GPIO.IN)
GPIO.setup(gas, GPIO.IN)
GPIO.setup(smoke, GPIO.IN)
GPIO.setup(ldr, GPIO.IN)

class mpu6050:
    GRAVITIY_MS2 = 9.80665
    address = None
    bus = None

    ACCEL_SCALE_MODIFIER_2G = 16384.0
    ACCEL_SCALE_MODIFIER_4G = 8192.0
    ACCEL_SCALE_MODIFIER_8G = 4096.0
    ACCEL_SCALE_MODIFIER_16G = 2048.0

    GYRO_SCALE_MODIFIER_250DEG = 131.0
    GYRO_SCALE_MODIFIER_500DEG = 65.5
    GYRO_SCALE_MODIFIER_1000DEG = 32.8
    GYRO_SCALE_MODIFIER_2000DEG = 16.4

    ACCEL_RANGE_2G = 0x00
    ACCEL_RANGE_4G = 0x08
    ACCEL_RANGE_8G = 0x10
    ACCEL_RANGE_16G = 0x18

    GYRO_RANGE_250DEG = 0x00
    GYRO_RANGE_500DEG = 0x08
    GYRO_RANGE_1000DEG = 0x10
    GYRO_RANGE_2000DEG = 0x18

    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C

    ACCEL_XOUT0 = 0x3B
    ACCEL_YOUT0 = 0x3D
    ACCEL_ZOUT0 = 0x3F

    TEMP_OUT0 = 0x41

    GYRO_XOUT0 = 0x43
    GYRO_YOUT0 = 0x45
    GYRO_ZOUT0 = 0x47

    ACCEL_CONFIG = 0x1C
    GYRO_CONFIG = 0x1B

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)

        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)


    def read_i2c_word(self, register):
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    def get_temp(self):
        raw_temp = self.read_i2c_word(self.TEMP_OUT0)
        actual_temp = (raw_temp / 340.0) + 36.53

        return actual_temp

    def set_accel_range(self, accel_range):
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, 0x00)

        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, accel_range)

    def read_accel_range(self, raw = False):
        raw_data = self.bus.read_byte_data(self.address, self.ACCEL_CONFIG)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == self.ACCEL_RANGE_2G:
                return 2
            elif raw_data == self.ACCEL_RANGE_4G:
                return 4
            elif raw_data == self.ACCEL_RANGE_8G:
                return 8
            elif raw_data == self.ACCEL_RANGE_16G:
                return 16
            else:
                return -1

    def get_accel_data(self, g = False):
        
        x = self.read_i2c_word(self.ACCEL_XOUT0)
        y = self.read_i2c_word(self.ACCEL_YOUT0)
        z = self.read_i2c_word(self.ACCEL_ZOUT0)

        accel_scale_modifier = None
        accel_range = self.read_accel_range(True)

        if accel_range == self.ACCEL_RANGE_2G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G
        elif accel_range == self.ACCEL_RANGE_4G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_4G
        elif accel_range == self.ACCEL_RANGE_8G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_8G
        elif accel_range == self.ACCEL_RANGE_16G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_16G
        else:
            print("Unkown range - accel_scale_modifier set to self.ACCEL_SCALE_MODIFIER_2G")
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G

        x = x / accel_scale_modifier
        y = y / accel_scale_modifier
        z = z / accel_scale_modifier

        if g is True:
            return {'x': x, 'y': y, 'z': z}
        elif g is False:
            x = x * self.GRAVITIY_MS2
            y = y * self.GRAVITIY_MS2
            z = z * self.GRAVITIY_MS2
            return {'x': x, 'y': y, 'z': z}

    def set_gyro_range(self, gyro_range):
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, 0x00)

        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, gyro_range)

    def read_gyro_range(self, raw = False):
        raw_data = self.bus.read_byte_data(self.address, self.GYRO_CONFIG)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == self.GYRO_RANGE_250DEG:
                return 250
            elif raw_data == self.GYRO_RANGE_500DEG:
                return 500
            elif raw_data == self.GYRO_RANGE_1000DEG:
                return 1000
            elif raw_data == self.GYRO_RANGE_2000DEG:
                return 2000
            else:
                return -1

    def get_gyro_data(self):
        x = self.read_i2c_word(self.GYRO_XOUT0)
        y = self.read_i2c_word(self.GYRO_YOUT0)
        z = self.read_i2c_word(self.GYRO_ZOUT0)

        gyro_scale_modifier = None
        gyro_range = self.read_gyro_range(True)

        if gyro_range == self.GYRO_RANGE_250DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG
        elif gyro_range == self.GYRO_RANGE_500DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_500DEG
        elif gyro_range == self.GYRO_RANGE_1000DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_1000DEG
        elif gyro_range == self.GYRO_RANGE_2000DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_2000DEG
        else:
            print("Unkown range - gyro_scale_modifier set to self.GYRO_SCALE_MODIFIER_250DEG")
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG
            
        x = x / gyro_scale_modifier
        y = y / gyro_scale_modifier
        z = z / gyro_scale_modifier

        return {'x': x, 'y': y, 'z': z}

    def get_all_data(self):
        temp = self.get_temp()
        accel = self.get_accel_data()
        gyro = self.get_gyro_data()
        
        return [accel, gyro, temp]
        
def sensorOn():
    print("Sensor active")
    with open('{}/src/configuration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        sensor = yaml.load(conf, Loader=yaml.FullLoader)
        sensor['Sensor']['status'] = 'on'
        with open('{}/src/configuration.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
            yaml.dump(sensor,conf)
    say('activated  sensor')
    mpu = mpu6050(0x68)
    print(mpu.get_temp())
    for i in range(5):
        accel_data = mpu.get_accel_data()
        global Ax, Ay, Az
        Ax = accel_data['x']
        Ay = accel_data['y']
        Az = accel_data['z']
    print("Exact position :")
    print("X = ", Ax, "\t\tY = ", Ay, "\t\tZ = ", Az)
    loop()
    
    
def loop():
    with open('{}/src/configuration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        sensor = yaml.load(conf, Loader=yaml.FullLoader)
        if(sensor['Sensor']['status'] == 'off'):
            return
        Fire = GPIO.input(fire)
        Gas = GPIO.input(gas)
        Smoke = GPIO.input(smoke)
        Ldr   = GPIO.input(ldr)
        
        mpu = mpu6050(0x68)
        accel_data = mpu.get_accel_data()
        Cx = accel_data['x']
        Cy = accel_data['y']
        Cz = accel_data['z']
        print("X = ", Cx, "\t\tY = ", Cy, "\t\tZ = ", Cy)

        x = abs(Cx-Ax)
        y = abs(Cy-Ay)
        z = abs(Cz-Az)

        if Fire == 0: 
            print("Something is not okay")
        if Gas == 0 :
            print("Something is not okay")
            say("gas, gas, please check, there are gas leaked")
        if Smoke == 0:
            print("Something is not okay")
            say("there are smoke, smoke is injuried to health")
        if Ldr == 0:
            print("Something is not okay")
            say("There are everything dark, I am afraid")
        if(x>2.5  or  y>2.5  or  z>2.5):
            say("please save me, make me strait")
            
        time.sleep(2)
    loop()
    

def sensorOff():
    print("Stor sensor")
    with open('{}/src/configuration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        sensor = yaml.load(conf, Loader=yaml.FullLoader)
        sensor['Sensor']['status'] = 'off'
        with open('{}/src/configuration.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
            yaml.dump(sensor,conf)
    say('deactivated sensor')


