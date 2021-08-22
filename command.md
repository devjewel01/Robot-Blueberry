Connect robot with a **wifi router**

then find the IP address of robot.

Now you can work with **VNC** or **SSH** 

#### Work with VNC
open vnc viwer and connet the robot using IP address.

wih a vnc viewer you can see the raspberry PI graphical interface.

you can use it like a computer easily.

#### Work with SSH
using SSH, you can work with a **Terminal** 

or **Putty Server**(for windows).


```bash
ssh pi@<raspberry pi IP>
```
example : 
```bash
ssh pi@192.168.43.25
```
*here 192.168.43.25 is IP address*

after conneting using ssh you controll the robot using commad line.

#### If robot doesn't start talking after Power On
```bash
  sudo systemctl stop robot.service
  sudo systemctl start robot.service
```
Or, you can start the code manually 
```bash
/home/pi/env/bin/python -u /home/pi/Robot-Blueberry/src/main.py --project_id 'test-e557a' --device_model_id 'test-e557a-robot-x5kmax'
```

#### for update the Robot OS
```bash
sudo apt update
sudo apt dist-upgrade -y
```

