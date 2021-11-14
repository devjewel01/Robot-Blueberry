# Robot Blueberry


## Index

[<img src="Store/gif/tata.gif" align="right" width="60%"  />](https://youtu.be/5AGnB9Y9vIk)

 <a href="#Robot_blueberry">Introduction</a></br>
 <a href="#Device">Component and Device</a></br>
 <a href="#features">Features</a></br>
 <a href="#languageTools">Language and Tools</a></br>
 <a href="#Diageam">Block diagram</a></br>
 <a href="#servoInitialization">Servo configuration</a></br>
 <a href="#DCMotorConnection">DC motor configuration</a></br>
 <a href="#sensorConfig">Sensor Configuration</a></br>
 <a href="#ServoMove">Servo Movement record</a></br>
 <a href="#memory">Memories</a></br>
 <a href="#Acknowledge">Acknowledge</a></br>


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


<h2 id="Device">Component and Device</h2>

1. **Raspberry Pi** microprocessor
2. **Arduino** microcontroller
3. **Servo Motors** 
4. **DC Motors** 
5. **Ultrasonic Sensors** 
6. **LCD Display** 
7. **Gas sensor** 
8. **Smoke sensor**
9.  **Fire sensor**
10. **Gyroscope sensor**
11. **Gps Tracker** 
12. **LED matrix cube**

<!--lint ignore double-link-->
<img src="Store/gif/pushup.gif" align="right" width="30%" />

<br />

<h2 id="features">Features:</h2>

* Take a command and replay accrding to command
* Hand's UP
* Hand Shake
* Salute
* Go forward and backword
* Turn left and right
* Bye Bye
* Auto move mode
* Expression while talking
* Hug
* Move at any direction
* Touch own body parts
* active sensor and read value and give the output


<!--lint ignore double-link-->
<img align="right" src="https://i.imgur.com/BzOnbkS.gif" />


<h2 id="languageTools">Programming Language and tools we used - </h2>

| Python | C++ |  Bash | Terminal | Raspberry Pi |  Arduino |
| ------ | ----| ------| -------- | ------------ | --------- |
|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bash/bash.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/raspberry-pi/raspberry-pi.png" />|<img align="left"  width="46px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/arduino/arduino.png" />|

<br />
<br />

<h2 id="Diageam">Block Diagram:</h2>

<img width="60%"  src="Store/pic/2021-05-23_1511451.png">


<h2 id="servoInitialization">Servo Configuration</h2>
    
 
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

<details>
    <summary>
        <strong  id="DCMotorConnection">DC motor configuration</strong>
    </summary>


| Leg      |  Enable Pin | Front Pin  | Back Pin |
| -------  | ---------   | ---------- | -------- |
| Right    | 13(27)      |  35(19)    |  36(16)  | 
| Left     | 15(22)      |  37(26)    |  38(20)  |

</details>


<details>
    <summary>
        <strong  id="sensorConfig">Sensor configuration</strong>
    </summary>


| Sensor   |  Pin        | 
| -------  | ---------   | 
| Gas      |   4          |  
| Smoke    |    7         |  
| Fire     |     13        |  
| Ldr      |     21      |  
| Gyroscope|       I2C      |  
|Ultrasonic|      echo:11, trigger:8       |  

</details>

<h2 id="ServoMove">Servo Move Record:</h2>

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
 
**10 times change**

>normal
 
| pin |	degree |
| ----| ----   |
| 7	  | 180    |
| 3	  |   0    |

</details>

<details>
    <summary> Hand's Up </summary>

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


<h2 id="memory">Memories</h2>
<details>
    <summary>
        <strong>Photos:</strong>
    </summary>
    <img src="Store/pic/DSC_0205.JPG" width="50%"/>
    <img src="Store/pic/DSC_0213.JPG" width="50%"/>
    <img src="Store/pic/DSC_0229.JPG" width="50%"/>
    <img src="Store/pic/DSC_0217.JPG" width="50%"/>

</details>

<details>
    <summary>
        <strong>Videos:</strong>
    </summary>

[<img src="Store/gif/intro.gif" />](https://youtu.be/NaSFW2tjuGQ)
[<img src="Store/gif/salute.gif" />](https://youtu.be/5AGnB9Y9vIk)

</details>


<details>
    <summary>
        <strong >News:</strong>
    </summary>
    
* [shadow news](https://www.shadow.com.bd/?p=28267)
* [MCJ news](https://www.facebook.com/mcjnews/posts/1613278385545042)
* [Cumillar Zamin](https://cumillarzamin.com/?p=90403)
* [Somoy Journal](https://somoyjournal.com/news-post/4072/%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F-'%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87%E0%A6%B0%E0%A6%BF'-%E0%A6%AC%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%B2%E0%A7%87%E0%A6%A8-%E0%A6%95%E0%A7%81%E0%A6%AE%E0%A6%BF%E0%A6%B2%E0%A7%8D%E0%A6%B2%E0%A6%BE-%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%AC%E0%A6%AC%E0%A6%BF%E0%A6%A6%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B2%E0%A7%9F%E0%A7%87%E0%A6%B0-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80%E0%A6%B0%E0%A6%BE)
* [Ekusher Alo](https://ekusheralo24.com/archives/274120)
* [Dainik Joy Bangla](https://dainikjoybanglabd.com/2021/07/08/%E0%A6%86%E0%A6%97%E0%A7%81%E0%A6%A8-%E0%A6%B2%E0%A6%BE%E0%A6%97%E0%A6%B2%E0%A7%87-%E0%A6%B8%E0%A6%A4%E0%A6%B0%E0%A7%8D%E0%A6%95%E0%A6%AC%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A4%E0%A6%BE-%E0%A6%A6/)
* [Our Bangladesh](https://news.ourbangladeshbd.com/29995/)
* [Deshchitro](https://deshchitro.com/details/5143)
* [Our TimeBD](https://www.ourtimebd.com/beta/1robot-blueberry-to-collect-covid-19-sample/)
* [Bangla Jagoran](https://banglarjagoron.com/archives/17925)
* [EI News](https://www.einews24.com/%E0%A6%B8%E0%A6%BE%E0%A6%B0%E0%A6%BE%E0%A6%A6%E0%A7%87%E0%A6%B6%E0%A7%87/37451/23/)
* [Bangladesh Bulletin](https://bangladeshbulletin.com/?p=53978)
* [Poribortoner Sopoth](https://poribortonersopoth.com/%E0%A6%95%E0%A7%81%E0%A6%AE%E0%A6%BF%E0%A6%B2%E0%A7%8D%E0%A6%B2%E0%A6%BE-%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%AC%E0%A6%AC%E0%A6%BF%E0%A6%A6%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B2%E0%A7%9F-2/)
* [Dhaka News 71](https://www.dhakanews71.com/campus/news/210614842)
* [Insaff24](https://www.insaff24.com/%E0%A6%86%E0%A6%97%E0%A7%81%E0%A6%A8-%E0%A6%B2%E0%A6%BE%E0%A6%97%E0%A6%B2%E0%A7%87%E0%A6%87-%E0%A6%B8%E0%A6%A4%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87-%E0%A6%AC%E0%A6%BE/)
* [Somoy News](https://www.somoynews.tv/news/2021-06-23/%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F-%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87%E0%A6%B0%E0%A6%BF-%E0%A6%A4%E0%A7%88%E0%A6%B0%E0%A6%BF-%E0%A6%95%E0%A6%B0%E0%A6%B2-%E0%A6%95%E0%A7%81%E0%A6%AC%E0%A6%BF-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80)
* [BD Campus TV](https://bdcampus-tv.com/%E0%A6%95%E0%A7%81%E0%A6%AC%E0%A6%BF-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F/)
* [Amader Shomoy](https://www.amadershomoy.com/bn/2021/06/24/1395734.asp)
* [Etv BD24](https://etvbd24.com/%E0%A6%86%E0%A6%97%E0%A7%81%E0%A6%A8-%E0%A6%B2%E0%A6%BE%E0%A6%97%E0%A6%B2%E0%A7%87%E0%A6%87-%E0%A6%B8%E0%A6%A4%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87-%E0%A6%AC%E0%A6%BE/)
* [Observer BD](https://bn.observerbd.com/details.php?id=63913)
* [Cumillar Paper](https://cumillarpaper.com/%E0%A6%95%E0%A7%81%E0%A6%AC%E0%A6%BF-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%A8%E0%A6%A4%E0%A7%81%E0%A6%A8-2)
* [Protidiner Chitro BD](https://www.protidinerchitrobd.com/%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F-%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87%E0%A6%B0%E0%A6%BF-%E0%A6%A4%E0%A7%88%E0%A6%B0%E0%A6%BF-%E0%A6%95%E0%A6%B0%E0%A6%B2-%E0%A6%95%E0%A7%81%E0%A6%AC%E0%A6%BF-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80/42673)
* [Shomoyer Alo](https://www.shomoyeralo.com/details.php?id=148649)
* [Daily Bangladesh](https://www.daily-bangladesh.com/education/255286)
* [BD Barta 24](http://www.bbarta24.net/education-premises/149464)
* [Jugantor](https://www.jugantor.com/tech/434899/%E0%A6%95%E0%A6%B0%E0%A7%8B%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%A8%E0%A6%AE%E0%A7%81%E0%A6%A8%E0%A6%BE-%E0%A6%B8%E0%A6%82%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%B9-%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87-%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F-%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87%E0%A6%B0%E0%A6%BF)
* [BD-Pratidin](https://www.bd-pratidin.com/saturday-morning/2021/07/10/668708)
* [Samakal](https://samakal.com/whole-country/article/210666558/%E0%A6%95%E0%A6%A5%E0%A6%BE-%E0%A6%AC%E0%A6%B2%E0%A6%9B%E0%A7%87-%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87%E0%A6%B0%E0%A6%BF)
* [Bhorer Kagoj](https://www.bhorerkagoj.com/2021/06/23/%E0%A6%8F%E0%A6%AC%E0%A6%BE%E0%A6%B0-%E0%A6%A6%E0%A7%8D%E0%A6%AC%E0%A6%BF%E0%A6%A4%E0%A7%80%E0%A7%9F-%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F-%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87/)
* [The Daily Campus](https://thedailycampus.com/innovation-research/70807/%E0%A6%95%E0%A6%B0%E0%A7%8B%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%A8%E0%A6%AE%E0%A7%81%E0%A6%A8%E0%A6%BE-%E0%A6%B8%E0%A6%82%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%B9-%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87-%E0%A6%95%E0%A7%81%E0%A6%AC%E0%A6%BF-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%B0%E0%A7%8B%E0%A6%AC%E0%A6%9F-%E0%A6%AC%E0%A7%8D%E0%A6%B2%E0%A7%81%E0%A6%AC%E0%A7%87%E0%A6%B0%E0%A6%BF)
* [Odhikar](https://www.odhikar.news/education/192791)
 

</details>

<h2 id="Acknowledge"> Acknowledge</h2>

 * [Shivasiddharth](https://github.com/shivasiddharth)
 * [Picovoice](https://github.com/Picovoice)
 * [Simon Monk](https://github.com/simonmonk)
 * [StackOverflow](https://stackoverflow.com/questions/tagged/raspberry-pi)
