<h2>Answers to the practise questions on chapter 2</h2>

<p>1. What are the two values of the Boolean data type? How do you write them?</p>
<h3><i>Answer</i></h3>
<p>True & False, It is writen with first capital letter followed by lowercase.</p>

<p>2. What are the three Boolean operators?</p>
<h3><i>Answer</i></h3>
<p>and, or, not</p>

<p>3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).</p>
<h3><i>Answer</i></h3>
<p>Truth Table for and, or, not</p>

<p>and</p>

| a | b | a and b |
| :---: | :---: | :---: |
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

<p>or</p>

| a | b | a or b |
| :---: | :---: | :---: |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

<p>not</p>

| a | not a |
| :---: | :---: |
| True | False |
| False | True |

<p>4. What do the following expressions evaluate to?</p>

```
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```

<h3><i>Answer</i></h3>
<p>False, False, True, False, False, True</p>

<p>5. What are the six comparison operators?</p>
<h3><i>Answer</i></h3>
<p>>, <, <=, >=, ==, !=</p>

<p>6. What is the difference between the equal to operator and the assignment operator?</p>
<h3><i>Answer</i></h3>
<p>Equal to operator is used to check a value is same as the given value whereas assignment operator is used to assign a value to a variable.</p>

<p>7. Explain what a condition is and where you would use one.</p>
<h3><i>Answer</i></h3>
<p>A condition is something makes a statement to true or false and It is used when multiple cases are there.</p>

<p>8. Identify the three blocks in this code:</p>

```
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```

<h3><i>Answer</i></h3>
<p>3 blocks in the code are</p>

```
print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
```

```
 print('bacon')
```

```
print('ham')
```

<p>9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.</p>
<h3><i>Answer</i></h3>
<p>Program</p>

```
spam = int(input())
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
```

<p>10. What keys can you press if your program is stuck in an infinite loop?</p>
<h3><i>Answer</i></h3>
<p>ctrl+c</p>

<p>11. What is the difference between break and continue?</p>
<h3><i>Answer</i></h3>
<p>'break' is used to exit from a loop and 'continue' is used to skip the rest of the instructions for the current itteration.</p>

<p>12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?</p>
<h3><i>Answer</i></h3>
<p>Working of range(10), range(0,10) and range(0,10,1) are exactly same all loops works for 9 times and gives same outputs but range(10) has only stop argument, range(0,10) has only start and stop argument, but range(0,10,1) has start, stop and step argument</p>

<p>13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.</p>
<h3><i>Answer</i></h3>
<p>Program</p>

```
fo i in range(1,11):
    print(i)
```

```
i = 1
while i<11:
    print(i)
    i+=1
```

<p>14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?</p>
<h3><i>Answer</i></h3>
<p>spam.bacon()</p>
