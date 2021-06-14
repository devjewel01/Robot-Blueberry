import threading
import pynmea2
import sys
import http.client, urllib.request, urllib.parse, urllib.error
import time
import serial

ser = serial.Serial("/dev/serial0")  
ser.baudrate = 9600 
ser.timeout = 0.5
sleep = 2 

class Message:
    def __init__(self):
        self.msg =''

        
key = 'CSJVYD1KP011U57J' 
msgdata = Message() 

def get_gps_data(serial, dmesg):
    print("Initializing GPS\n")
    while True:
        strRead = serial.readline()
        if sys.version_info[0] == 3:
            strRead = strRead.decode("utf-8","ignore")
            if strRead[0:6] == '$GPGGA':
                dmesg.msg = pynmea2.parse(strRead)
        else:
            if strRead.find('GGA') > 0:
                dmesg.msg = pynmea2.parse(strRead)


def start_gps_receiver(serial, dmesg):
    t2 = threading.Thread(target=get_gps_data, args=(serial, dmesg))
    t2.start()
    print("GPS Receiver started")


def ready_gps_receiver(msg):
    print("Please wait fixing GPS .....")
    dmesg = msg.msg
    while(dmesg.gps_qual != 1):
        pass
    print("GPS Fix available")


def get_latitude(msg):
    dmesg = msg.msg
    return dmesg.latitude


def get_longitude(msg):
    dmesg = msg.msg
    return dmesg.longitude


def upload_cloud():
    temp = get_latitude(msgdata)
    temp1 = get_longitude(msgdata)
    params = urllib.parse.urlencode({'field1': temp,'field2': temp1, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept" : "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(("Lat:",temp))
        print(("Long:",temp1))
        print((response.status, response.reason))
        conn.close()
    except KeyboardInterrupt:
         print("Connection Failed")       
               
             
if __name__ == "__main__":
    start_gps_receiver(ser, msgdata)
    time.sleep(2)
    ready_gps_receiver(msgdata)
    while True:
        upload_cloud()
        time.sleep(sleep)
