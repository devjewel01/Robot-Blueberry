 ## salute

>start.

| pin | degree  |
| --- | ------  |
| 7	  |    0    |
| 3   |	  180   |
| 7	  |    80   |
| 6	  |    60   |

>normal

| pin | degree |
| --- | ------ |
| 7	  |  180   |
| 3   |	   0   |
| 6	  |  170   |

<br/>
<br/>

## Hug 

> start

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
| 7 |	0|	10	|180|
|3	|90	|4	|90 |
|2	|50 |	5	|150|
|7 |	50	| 10	|130|
|6	|90	|9	|90|

>stop

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
|7|	180|	10|	0|
|3	|0|	4|	180|
|2	|20	|5|	160|
|6	|170 |	9	|10|

<br/>
<br/>

## hand_shake 

>start

| pin |	degree |
| ----| ----   |
| 3	| 60 |
|7	|150|

>shake

```python
for i in range(0, 10):
    if i&1:
        pin 7 = 170
    else:
        pin 7 = 120
```

>normal

| pin |	degree |
| ----| ----   |
| 7	| 180 |
|3	| 0|

<br/>
<br/>

## hand's_up.py  

>start

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
|10|	180|	7|	0|
|5	|40	|2	|140|
|4	|90|	3|	90|
|10	|130|	7	|70|

>stop

| pin1 | degree	 | pin2	| degree |
| ---- | ------- | -----| -------|
|10	| 0 |	7 |	180 |
|4 |	180|	3|	0|
|5 |	160 |	2 |	20|




<br/>
<br/>

>Thank you

