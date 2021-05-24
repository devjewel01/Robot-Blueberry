
# Robot Blueberry

## **It is Raspberry Pi based Humanoid Robot** using [GassistPi](https://github.com/shivasiddharth/GassistPi)

<!--lint ignore double-link-->
<img src="https://i.imgur.com/qI1Jfyl.gif" align="right" width="60%" />

<br/>

## It's made by team [robosouls](https://www.facebook.com/robosouls):

| Name               | Post               | Email                         |  
| ------------------ | ---------          | ----------------------------- |
| [**Shanjit Mondal**](https://www.facebook.com/shanjit.mondol.50) | [Circuit  & Mechanical Designer](https://github.com/shanjit11) | shanjitmondal11@gmail.com       | 
| [**Jewel Nath**](https://www.facebook.com/dev.jewel.5/)     | [Programmer](https://github.com/devjewel01)       | devjewel.cou.ict10@gmail.com  |  
| [**Mestu Paul**](https://www.facebook.com/mestu.paul.812)     | [Programmer](https://github.com/Mestu-Paul)       |paulmestu@gmail.com            |   


<!--lint ignore double-link-->
<img src="Store/gif/robothand.gif" align="right" width="30%" />


## Here we used:
1. **Raspberry Pi** as a cpu of our robot
2. **Servo Motors** for various hand's move
3. **DC Motos** for runing
4. **Ultrasonic Sensors** for count distance
5. **LED** for indicators
6. **LCD Display** for showing message
7. **Aluminium** sheet, **Aluminum** angle, **SS** for making robot body
8. **Makeup Mannequin** as a robot face

<!--lint ignore double-link-->
<img src="Store/gif/pushup.gif" align="right" width="30%" />

<br />


## It's able to -
* Take a cammand and replay accrding to command
* Hand's UP
* Hand Shake
* Salute
* Go forward and backword
* Turn left and right


<!--lint ignore double-link-->
<img align="right" src="https://i.imgur.com/BzOnbkS.gif" />


## Programming Language and tools we used - 
| Python | C++ |  Bash | Terminal | Raspberry Pi |  Arduino |
| ------ | ----| ------| -------- | ------------ | --------- |
|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bash/bash.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/raspberry-pi/raspberry-pi.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/arduino/arduino.png" />|

<br />
<br />

## Servo Motor Position Block Diagram:
<img width="60%"  src="Store/pic/2021-05-23_1511451.png">

### Servo Initial positions:
 
|servo no | connection | position   | Limitation | Direction           | Description |  
| ------- | ---------- | ---------- | -----------|  -------            | ---------   |
|  1      | gpio-40(21)|    0       |         35 | Front/Back          |
|  2      | i2c-0      |   90       |        180 | Right/Left          |
|  3      | i2c-1      |    0       |        180 | Up/Down(Right/Left) |
|  4      | i2c-2      |  180       |        180 | Up/Down(Right/Left) |
|  5      | i2c-3      |    0       |          0 | Up/Down(Front/Back) |
|  6      | i2c-4      |  170       |          0 | Up/Down(Front/Back) |
|  7      | i2c-5      |  170       |        180 | Right/Left          |
|  8      | i2c-6      |    0       |        180 | Right/Left          |
|  9      | i2c-7      |  180       |        180 | Up/Down(Front/Back) |
| 10      | i2c-8      |    0       |        180 | Up/Down(Front/Back) |
| 11      | i2c-9      |   60       |        180 | Right/Left          |
| 12      | i2c-10     |  150       |        180 | Right/Left          |
| 13      | i2c-11     |    0       |        180 | Open/Close          |
| 14      | i2c-12     |    0       |        180 | Open/Close          |
| 15      | i2c-13     |    0       |        180 | Open/Close          |
| 16      | i2c-14     |    0       |        180 | Open/Close          |
| 17      | i2c-15     |    0       |        180 | Open/Close          |
| 18      | gpio-19(10)|    0       |        180 | Open/Close          |
| 19      | gpio-21(9) |    0       |        180 | Open/Close          |
| 20      | gpio-22(25)|    0       |        180 | Open/Close          |
| 21      | gpio-23(11)|    0       |        180 | Open/Close          |
| 22      | gpio-24(8) |    0       |        180 | Open/Close          |

### DC motor connection:

| Leg      |  Enable Pin | Front Pin  | Back Pin |
| -------  | ---------   | ---------- | -------- |
| Right    | 13(27)      |  35(19)    |  36(16)  | 
| Left     | 15(22)      |  37(26)    |  38(20)  |

### salute

>start.

| pin | degree  |
| --- | ------  |
| 7	  |    0    |
| 3   |	  180   |
| 7	  |    80   |
| 5	  |    60   |

>normal

| pin | degree |
| --- | ------ |
| 7	  |  180   |
| 3   |	   0   |
| 5	  |  170   |

<br/>
<br/>

### Hug 

> start

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
| 7    |  0      |  8	|  180   |
| 3    | 90	     |      |   90   |
| 1	   | 50      |	2	|  150   |
| 7    | 50	     |  8	|  130   |
| 5	   | 90	     |  6   |   90   |

>stop

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
|7     |  180    |	8   |	  0  |
|3     |    0    |	4   |	180  |
|1     |   20	 |  2   |	160  |
|5     |  170    |	6   |   10   |

<br/>
<br/>

### hand_shake 

>start

| pin |	degree |
| ----| ----   |
| 3	  | 60     |
| 7	  |140     |

>shake

```python
for i in range(0, 10):
    if i&1:
        pin 7 = 155
    else:
        pin 7 = 125
    sleep(0.02)
```

>normal
 
| pin |	degree |
| ----| ----   |
| 7	  | 180    |
| 3	  |   0    |

<br/>
<br/>

### hand's_up.py  

>start

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
|8  | 180  |   7 |	0  |
|2	|  40  |   1 | 140 |
|4	|  90  |   3 |	90 |
|8	| 130  |   7 |  70 |

>stop

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
|8  |   0  |	7 |	180 |
|4  | 180  |	3 |	0   |
|2  | 160  |	1 |	20  |




<br/>
<br/>



