# TableTop Multi Die
A Virtual die to assist with tabletop games. Written in python.

## Cloning and Running
1.Clone this Project:
```
git clone https://github.com/Luisjwhitaker/tabletop-multi-die.git
```
2.Import project into your code
```
import roll_die
```

## Usage Instructions
```
roll_die.roll(a,b)
```
Where<br>
a is an integer that represents the number of sides the die you want to roll is. and<br>
b is an integer that represents the number of times you want to roll said die. (default of once)<br>
example:<br>
&nbsp;&nbsp;&nbsp;&nbsp;roll_die(6) will roll a six sided die once.<br>
&nbsp;&nbsp;&nbsp;&nbsp;roll_die(20,3) will roll a twenty sided die three times.<br>
* output is a list of integers
