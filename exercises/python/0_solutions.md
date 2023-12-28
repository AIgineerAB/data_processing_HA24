# Answers and hints for exercises in Python :blue_book:

Click to jump directly to a secion
- [count with Python](#count-with-python)
- [if statements](#if-statements)
- [while statements](#while-statement)
- [for statements](#for-statement)
- [lists](#lists)
- [strings](#strings)
- [functions](#functions)
- [exceptions](#exceptions)
- [file handling](#file-handling)
- [dictionary](#dictionary)
- [numpy](#numpy)

A tips for working with the exercises is to   
- analyze the problem
- solve it yourself
- ask an LLM to improve on your code 
- refactor your code, but don't copy the answer directly as muscle memory is an important part of learning programming 

---

## Count with Python

### 0. Pythagorean theorem

<details>
<summary>Hint</summary>

[Video lecture][pythagoras_video] (swedish)

[pythagoras_video]: https://www.youtube.com/watch?v=3iivEnKEJ88

To do square root in Python
```python 
import math
math.sqrt()
```

</details>


<details>

<summary>Answer</summary>
a) 

```
The hypothenuse is 5 length units
```

b)

```
The other cathetus is 4.9 length units
```
</details>

### 1. Classification accuracy

<details>
<summary>Hint</summary>

Ratio between correct predictions and total number of predictions.

</details>

### 2. Classification accuracy

<details> 

<summary>Hint </summary>

Try to understand what it means for the actual user with each category. 

</details>

<details> 

<summary>Answer </summary>

```
The accuracy of this model is 0.987.
```

</details>

### 3. Line

<details> 

<summary>Hint </summary>

$k = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$

Either plug in one point into $y = kx + m$ and solve for $m$ or read the intersection with y-axis in the graph.

[Video lecture][video_line] (Swedish)

[video_line]: https://www.youtube.com/watch?v=9Buuq6rkaJ0

</details>

<details> 

<summary>Solution </summary>

```
k = 0.75, m = 1, so the equation for the slope is y = 0.75x + 1
```

</details>

### 4. Euclidean distance

<details> 

<summary>Hint </summary>
The formula is: 

$\text{distance} = \sqrt{(x_2-x_1)^2 +(y_2-y_1)^2}$

[Video lecture][video_distance] (Swedish)

[video_distance]: https://www.youtube.com/watch?v=DrTsKgHg7ng

</details>

<details> 

<summary>Answer </summary>

```
The distance is around 5.1 length units.
```

</details>

### 5. Euclidean distance in 3D

<details> 

<summary>Hint </summary>

Let $p =(p_1, p_2, p_3)$ and $q = (q_1, q_2, q_3) \Rightarrow$   

$d(p,q) = \sqrt{(p_1-q_1)^2 +(p_2-q_2)^2 +(p_3-q_3)^2 }$, where $d(p,q)$ is the Euclidean distance between $p$ and $q$
</details>

<details> 

<summary>Answer </summary>

```
The distance is around 4.12 l.u.
```

</details>

---
## if-statements

There are no hints and answers here, as you can check for your answer immediately through results of the code.

---
## while-statement

### 0. Count numbers

<details>

<summary>Hint </summary>

```python

i += 1 # adds one and assigns it to i, equivalent to i = i + 1
```

</details>
 
<details>

<summary>Answer </summary>

```

-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10
```

</details>


### 1. Arithmetic sum

<details>

<summary>Answer </summary>

```
a) 1 + 2 + ... + 99 + 100 = 5050 

b) 1 + 3 + 5 +...+ 97 + 99 = 2500
```

</details>

### 2. Guess number game

<details>

<summary>Hint </summary>

&nbsp; b) &nbsp; Half your testing number each time 

</details>



### 4. Check convergence

<details>

<summary>Answer </summary>

&nbsp; a) &nbsp; $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots + \frac{1}{2^n} \xrightarrow[n\rightarrow \infty]{} 2$ 

&nbsp; b) &nbsp; $ 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots + \frac{(-1)^n}{2n+1} \xrightarrow[n\rightarrow \infty]{} \frac{\pi}{4}$

</details>

---
## for statement

### 0. Count numbers

<details>

<summary>Answer </summary>

```
a) -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10

b) -10  -8  -6  -4  -2  0  2  4  6  8  10
```

</details>

### 1. Arithmetic sum

<details>

<summary>Answer </summary>

```
a) 1 + 2 + ... + 99 + 100 = 5050 

b) 1 + 3 + 5 +...+ 97 + 99 = 2500
```

</details>

### 2. Multiplication table 


<details>

<summary>Hint</summary>

c) Use nested for-loops, which means a for-loop in a for-loop. To format the table nicely, use **f-string**: 

```python
print(f"{number :4}", end = "")
```


</details>


<details>

<summary>Answer </summary>

a)
```
0 6 12 18 24 30 36 42 48 54 60
```

b) e.g. 

```
Which table are you interested in? 5
Specify start of table: 5
Specify end of table: 12

Your 5th multiplication table from 5 to 12: 25 30 35 40 45 50 55 60
```

c)

```
   0   0   0   0   0   0   0   0   0   0   0
   0   1   2   3   4   5   6   7   8   9  10
   0   2   4   6   8  10  12  14  16  18  20
   0   3   6   9  12  15  18  21  24  27  30
   0   4   8  12  16  20  24  28  32  36  40
   0   5  10  15  20  25  30  35  40  45  50
   0   6  12  18  24  30  36  42  48  54  60
   0   7  14  21  28  35  42  49  56  63  70
   0   8  16  24  32  40  48  56  64  72  80
   0   9  18  27  36  45  54  63  72  81  90
   0  10  20  30  40  50  60  70  80  90 100
```

</details>


### 4. Pin code cracking

<details>

<summary>Answer </summary>

e.g.
```
The final guess is 8993
The computer number is 8993
```

</details>

### 5. Rice on chessboard

<details>

<summary>Answer</summary>

```
18446744073709551615 number of grains
```

</details>

---
## Lists

### 0. Dice rolls


<details>

<summary>Answer </summary>

a)
```
Ascending order: [1, 1, 2, 3, 4, 4, 4, 5, 6, 6]
```

b) 
```
Descending order: [6, 6, 5, 4, 4, 4, 3, 2, 1, 1]
```

c) 
```
Maximum: 6
Minimum: 1
```

</details>

### 1. Food menu

<details>

<summary>Answer</summary>

c) 
```
Bambameny
Mån: vegetarisk lasagne
Tis: spaghetti
Ons: fisk
Tor: grönsakssoppa
Fre: pannkakor
```

</details>


### 2. Squares

<details>
<summary>Answer</summary>

a)
```
[100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

b) 

<img align="left" src="https://github.com/kokchun/assets/blob/main/python/x%5E2_graph.png?raw=true" width="300"/>

</details>

### 3. Chessboard

<details>

<summary>Hint</summary>

b) Use **f-string** and create a list of characters with: 

```python
list("ABCDEFGH)
```

b) One option is to use nested list comprehension where one for-loop creates the first list and the other creates several of the first list

</details>


<details>

<summary>Answer</summary>

b)
```
[['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
 ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
 ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
 ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
 ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
 ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
 ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
 ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']]
```

</details>

### 4. Dice rolls convergence

<details>

<summary>Hint </summary>

Use this code for plot settings: 

```python
plt.plot(probability_six, '-*')
plt.title("Probability of six for different number of rolls")
plt.xticks([0,1,2,3,4,5], num_rolls);
plt.xlabel("Number of dice rolls")
plt.ylabel("Probability")

```
</details>

<details>

<summary>Answer </summary>

a)
```
The number of outcome six in 100 dice rolls is: 17 
```

b) 
```
Count number of six: [1, 21, 161, 1642, 16560, 166406]
P(six) = [0.1, 0.21, 0.161, 0.1642, 0.1656, 0.1664]
```

c) Note that the graph changes due to random simulation. To reproduce this result, use 

```python
random.seed(1)
```

<img src = "https://github.com/kokchun/assets/blob/main/python/probability_six_graph.png?raw=true" width="300"/>

</details>


### 5. Monte Carlo simulation

<details>

<summary>Hint</summary>

a) 

Try solve this task with pen and paper before approaching to code it.

b)

Think in terms of theoretical areas. Also try to increase the number of simulated points, to see if you find convergence.

</details>

<details>

<summary>Answer</summary>


a) 

<img src="https://github.com/kokchun/assets/blob/main/python/MC_simulation_5k.png?raw=true" width = 300>


b) 

0.7908

No answer here, try to prove it theoretically. 


</details>

### 6. A cute rabbit among two ferocious snakes

<details>

<summary>Hint</summary>

a) 

Try to reason using probability.


</details>

<details>

<summary>Answer</summary>


a) 

You will simulate the answer in b).

b) 

<img src="https://github.com/kokchun/assets/blob/main/python/mh_simulations.png?raw=true" width = 300>



</details>

---
## Strings

### 1. Counting words

<details>

<summary>Answer</summary>

```
There are 17 words in that sentence
```

</details>

### 3. Vowels

<details>

<summary>Answer</summary>

```

There are 22 vowels in this sentence 

```

</details>

---
## Functions

### 1. Euclidean distance

<details>

<summary>Hint</summary>

Use a **for** statement

</details>
 
<details>

<summary>Answer</summary>

c)

```
[10.4, 9.1, 14.1, 4.5, 13.5]
```

</details>

### 2. Mathematical functions 

<details>

<summary>Hint</summary>
Use numpy's linspace function:

```python
import numpy as np
x = np.linspace(-10,10)
```

[Derivative video][derivative_video] (Swedish)

[Derivative of polynomials][derivative_polynomial] (Swedish)

[derivative_video]: https://www.youtube.com/watch?v=hzXJxOXkU_M
[derivative_polynomial]: https://www.youtube.com/watch?v=dFnro1sBn1Y

</details>
 
<details>

<summary>Answer</summary>

<img src = "https://github.com/kokchun/assets/blob/main/python/functions_graph.png?raw=true" width="400"/>

</details>

### 3. Name cleaner

<details>

<summary>Hint</summary>
Here are some potentially useful string methods

- [title() method][str_title]
- [strip() method][str_strip]
- [join() method][str_join]
- [split() method][str_split]

[str_title]: https://www.w3schools.com/python/ref_string_title.asp
[str_strip]: https://www.w3schools.com/python/ref_string_strip.asp
[str_join]: https://www.w3schools.com/python/ref_string_join.asp
[str_split]: https://www.w3schools.com/python/ref_string_split.asp 

</details>
 
<details>

<summary>Answer</summary>

```
Marcus
Ida Anderson
Olof Olofsson
```

</details>

---
## Exceptions

### 0. Find and fix errors

<details>

<summary>Hint </summary>

Also look for logical errors. 

</details>
 
<details>

<summary>Answer </summary>

```
The distance between (0.5, 0.5) and origin is around 0.707.
```

</details>

### 1. Find and fix errors

<details>

<summary>Hint </summary>

Print out and test different cases to build up the condition in the if-statement

</details>
 
<details>

<summary>Answer </summary>

```

231 is not four-digit
3124 is four-digit
-4124 is four-digit
-1000 is four-digit
-999 is not four-digit
1001 is four-digit
10000 is not four-digit
-10000 is not four-digit
999 is not four-digit

```

</details>

### 2. Tram


<details>

<summary>Hint </summary>

Raise user friendly exceptions to guide the user to give right input format.

</details>

<details>

<summary>Answer </summary>

For example: 

```
How many times do you take tram in one month? -23
Number of times you take tram must be between 0 and 100

How much does one ticket cost? (kr) 1000
One ticket must cost between 0 and 100 kr

How many times do you take tram in one month? 23
How much does one ticket cost? (kr) 35
How much does one month card cost? (kr) 600

Cost with one-time tickets 805.0
Cost with monthly card 600.0
It's worth to buy a monthly card

```

</details>

## File handling

### 0. Dice rolls

<details>

<summary>Answer </summary>

For example: 

```

Simulate 20 dice rolls:
[3 4 4 3 1 2 6 6 4 6 2 4 5 3 1 2 1 3 3 1]

Sorted dice rolls:
[1 1 1 1 2 2 2 3 3 3 3 3 4 4 4 4 5 6 6 6]

Number of fours: 4

```

</details>


### 1. Test results


<details>

<summary>Hint </summary>

Open the file using option "r" for read and open the file using option "a" for append. 

</details>
<br>
<details>

<summary>Answer </summary>

```

Adam Gustafsson 25
Emil Johansson 23
Sven Erik Karlsson 13
Ove Karlsten 41
Emma Boden 32
Ida Håkansson 23
Ella Ester 41
Hanna Karlsson 23 
Johan Johansson 42
Sven Erik Lundin 39
Björn Björnsson 39
Karl Karlsson 32
Bose Bosseson 32
Håkan Håkanson 24
Jonas Jonasson 31
Erik Eriksson 31
Gore Bord 55
Jakob Kallander 65
Fredrika Ulven 10

Sorted alphabetically
Adam Gustafsson 25
Björn Björnsson 39
Bose Bosseson 32
Ella Ester 41
Emil Johansson 23
Emma Boden 32
Erik Eriksson 31
Fredrika Ulven 10
Gore Bord 55
Hanna Karlsson 23
Håkan Håkanson 24
Ida Håkansson 23
Jakob Kallander 65
Johan Johansson 42
Jonas Jonasson 31
Karl Karlsson 32
Ove Karlsten 41
Sven Erik Karlsson 13
Sven Erik Lundin 39

Sorted results: 
Grade: F
Fredrika Ulven 10
Sven Erik Karlsson 13
Grade: E
Adam Gustafsson 25
Emil Johansson 23
Hanna Karlsson 23
Håkan Håkanson 24
Ida Håkansson 23
Grade: D
Björn Björnsson 39
Bose Bosseson 32
Emma Boden 32
Erik Eriksson 31
Jonas Jonasson 31
Karl Karlsson 32
Sven Erik Lundin 39
Grade: C
Ella Ester 41
Johan Johansson 42
Ove Karlsten 41
Grade: B
Gore Bord 55
Grade: A
Jakob Kallander 65

```

</details>

### 2. National test

<details>

<summary>Hint </summary>

Use **subplot** in **matplotlib**

</details>
<br>
<details>

<summary>Answer </summary>

<img src="https://github.com/kokchun/assets/blob/main/python/NP.png?raw=true" width="400"/>

</details>

### 3. Dice roll experiment


<details>

<summary>Answer </summary>

```

Number of rolls: 10 
Ones: 4, probability: 0.4
Twos: 1, probability: 0.1
Threes: 1, probability: 0.1
Fours: 2, probability: 0.2
Fives: 1, probability: 0.1
Sixes: 1, probability: 0.1

Number of rolls: 100 
Ones: 16, probability: 0.16
Twos: 12, probability: 0.12
Threes: 24, probability: 0.24
Fours: 18, probability: 0.18
Fives: 16, probability: 0.16
Sixes: 14, probability: 0.14

Number of rolls: 1000 
Ones: 181, probability: 0.181
Twos: 167, probability: 0.167
Threes: 184, probability: 0.184
Fours: 152, probability: 0.152
Fives: 168, probability: 0.168
Sixes: 148, probability: 0.148

Number of rolls: 10000 
Ones: 1630, probability: 0.163
Twos: 1666, probability: 0.1666
Threes: 1686, probability: 0.1686
Fours: 1616, probability: 0.1616
Fives: 1677, probability: 0.1677
Sixes: 1725, probability: 0.1725

Number of rolls: 100000 
Ones: 16804, probability: 0.16804
Twos: 16625, probability: 0.16625
Threes: 16646, probability: 0.16646
Fours: 16660, probability: 0.1666
Fives: 16576, probability: 0.16576
Sixes: 16689, probability: 0.16689

```

</details>

---
## Dictionary

### 0. Curriculum

<details>

<summary>Answer</summary>

Look at your course program curriculum

</details>


### 1. Dice simulation

<details>

<summary>Answer</summary>

```
1: 166481
2: 166844
3: 166154
4: 167400
5: 167260
6: 165861
```

</details>

### 2. Pokemon list

<details>

<summary>Answer</summary>

```
{'Bulbasaur': 'Gräs/Gift, 1',
 'Ivysaur': 'Gräs/Gift, 2',
 'Venusaur': 'Gräs/Gift, 3',
 'Charmander': 'Eld, 4',
 'Charmeleon': 'Eld, 5',
 'Charizard': 'Eld/Flygande, 6',
 'Squirtle': 'Vatten, 7',
 'Wartortle': 'Vatten, 8',
 'Blastoise': 'Vatten, 9',
 ...
}
```

</details>

---
## Numpy 

### 0. Dice simulations

<details>

<summary>Answer </summary>

a)
```
3.5
```

b) 

<img src="https://github.com/kokchun/assets/blob/main/python/numpy_0b.png?raw=true" width = 400>

</details>

### 1. Several dices


<details>

<summary>Hint</summary>

a) 

Here are some potentially useful methods:

```py

np.meshgrid(), np.add.reduce(), np.unique()

```

c)

Divide by the total number of outcomes


</details>

<details>

<summary>Answer</summary>


a) 

Sample space

```
[[ 2  3  4  5  6  7]
 [ 3  4  5  6  7  8]
 [ 4  5  6  7  8  9]
 [ 5  6  7  8  9 10]
 [ 6  7  8  9 10 11]
 [ 7  8  9 10 11 12]]
```

b) 

Unique values:
```
[ 2  3  4  5  6  7  8  9 10 11 12]
```

Count: 
```
[1 2 3 4 5 6 5 4 3 2 1]
```

c)

```
[0.028 0.056 0.083 0.111 0.139 0.167 0.139 0.111 0.083 0.056 0.028]
```

d) 


<img src="https://github.com/kokchun/assets/blob/main/python/numpy1d.png?raw=true" width = 300>


e) 

<img src="https://github.com/kokchun/assets/blob/main/python/numpy1e.png?raw=true" width = 500>


We see that when we sum several uniformly distributed random variables we will approach the normal distribution. This is called the central limit theorem, which we will come back to in the statistics course.

</details>

---
## OOP basics

### 0. Unit conversion
<details>

<summary>Hint</summary>

Use the property decorator:
- @property

You can read about the [units here][units] 

[units]: https://en.wikipedia.org/wiki/United_States_customary_units 

Check for: 
- negative values 
- types that are not **int** or **float**

Use isinstance() to check for type

</details>
<br>
<details>

<summary>Answer</summary>
For example: 

```python

units = UnitUS(5)
print(f"5 feet = {units.foot_to_meters()} m")
print(f"5 inch = {units.inch_to_cm()} cm")
print(f"5 pounds = {units.pound_to_kg():.2f} kg")

``` 

```
5 feet = 1.524 m
5 inch = 12.7 cm
5 pounds = 2.27 kg
```
</details>

### 1. Person

<details>

<summary>Hint</summary>

Use the property decorator:
- @property

Use isinstance() to check for type

Check for: 
- negative values 
- types that are not **int** or **float**


</details>
<br>
<details>

<summary>Answer</summary>
For example: 

```python

p = Person("Pernilla", 32, "pernilla@gmail.com") 
print(p)

``` 

```
Person(Pernilla, 32, pernilla@gmail.com)

```

```python

try:
    p = Person("Pernilla", 32, "pernillagmail.com")
except TypeError as ex:
    print(ex)
except NameError as ex:
    print(ex)

```

```

pernillagmail.com is not a valid email, format must be xxxx@yyyy.zzz

```
</details>


### 2. Student and Teacher


<details>

<summary>Answer</summary>
For example: 

```python

teacher = Teacher("Pernilla", 32, "pernilla@gmail.com") 

student = Student("Karl", 25, "karl@gmail.com")

print(teacher.teach())
print(teacher.say_hello())

print(student.study())
print(student.say_hello())

``` 

```
teach...teach...teach...more teaching

Hi, my name is Pernilla, I am 32 years old, my email address is pernilla@gmail.com

study...study...study...more study

Yo, I am a student, my name is Karl, I am 25 years old, my email address is karl@gmail.com


```

</details>

### 4. Simple Travian

<details>

<summary>Answer</summary>
For example: 

```python
vill = Village()
vill.wheat_field += 500
vill.clay_field -= 25
vill.lumber_field +=200
print(vill)
``` 

```
Stock: Lumber:700/800 	 Clay:475/800 	 Iron:500/800 	 Crop:800/800 
Production: 
Lumber: 4 per hour
Clay: 4 per hour
Iron: 4 per hour 
Crop: 4 per hour
```

</details>

---
## OOP inheritance and polymorphism

<details>

<summary>Hint</summary>

Use ```__super__()``` in each subclass to call the \_\_init\_\_() in parent class. Add additional parameters in the \_\_init\_\_() of each subclass when needed. Keep error handling and validation in parent class and let the subclass inherit them in order to avoid repeating validation code.

</details>