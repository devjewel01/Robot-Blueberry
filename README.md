# Robot Blueberry
<details>
    <summary>
        <strong style="font-size:300%;">
            Index
        </strong>
    </summary>
 <a href="#Robot_blueberry">Introduction</a></br>
 <a href="#Device">Here we used</a></br>
 <a href="#features">Features</a></br>
 <a href="#languageTools">Language and Tools</a></br>
 <a href="#Diageam">Position Block Diagram</a></br>
 <a href="#servoInitialization">Servo Inital Position</a></br>
 <a href="#DCMotorConnection">DC motor connection:</a></br>
 <a href="#ServoMove">Servo Move</a></br>
 <a href="#servoInitialization">Servo Inital Position</a></br>
 <a href="#Acknowledge">Acknowledge</a></br>
</details>
<p id="Robot_blueberry"></p>

## **It is Raspberry Pi based Humanoid Robot**

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


<h3 id="Device">Here we used:</h3>

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

<h1 id="features">Features:</h1>

* Take a cammand and replay accrding to command
* Hand's UP
* Hand Shake
* Salute
* Go forward and backword
* Turn left and right


<!--lint ignore double-link-->
<img align="right" src="https://i.imgur.com/BzOnbkS.gif" />


<h1 id="languageTools">Programming Language and tools we used - </h1>

| Python | C++ |  Bash | Terminal | Raspberry Pi |  Arduino |
| ------ | ----| ------| -------- | ------------ | --------- |
|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bash/bash.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/raspberry-pi/raspberry-pi.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/arduino/arduino.png" />|

<br />
<br />

<h1 id="Diageam">Servo Motor Position Block Diagram:</h1>

<img width="60%"  src="Store/pic/2021-05-23_1511451.png">
<details>
    <summary>
        <strong id="servoInitialization">Servo Initial positions:</strong>
    </summary>
 
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

</details>
<details>
    <summary>
        <strong id="DCMotorConnection">DC motor connection:</strong>
    </summary>


| Leg      |  Enable Pin | Front Pin  | Back Pin |
| -------  | ---------   | ---------- | -------- |
| Right    | 13(27)      |  35(19)    |  36(16)  | 
| Left     | 15(22)      |  37(26)    |  38(20)  |

</details>
<h3 id="ServoMove">Servo Move:</h3>
<details>
    <summary>Salute</summary>

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

</details>
<details>
    <summary>Hug</summary>

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
</details>

<details>
    <summary>Hand Shake</summary>

>start

| pin |	degree |
| ----| ----   |
| 3	  | 60     |
| 7	  |140     |

>shake

| pin |	degree |
| ----| ----   |
| 7	  | 155    |
| 7	  | 125    |
 
** 10 times change**

>normal
 
| pin |	degree |
| ----| ----   |
| 7	  | 180    |
| 3	  |   0    |

<br/>
<br/>

</details>
<details>
    <summary>
        Hand's Up
    </summary>

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

</details>

<br/>


<h3 id="Acknowledge"> Acknowledge</h3>

 * [Shivasiddharth](https://github.com/shivasiddharth)
 * [Picovoice](https://github.com/Picovoice)
 * [Simon Monk](https://github.com/simonmonk)
 * [StackOverflow](https://stackoverflow.com/questions/tagged/raspberry-pi)
