import http.client, urllib.request, urllib.parse, urllib.error
import time
from gps_api import *
import serial

ser = serial.Serial("/dev/serial0")  
ser.baudrate = 9600 
ser.timeout = 0.5
sleep = 2 

key = 'CSJVYD1KP011U57J'  
msgdata = Message() 

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
