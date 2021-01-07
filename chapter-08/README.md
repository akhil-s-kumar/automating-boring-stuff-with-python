<h2>Answers to the Practice Questions from chapter 08</h2>

<p>1. Does PyInputPlus come with the Python Standard Library?</p>
<h3><i>Answer</i></h3>
<p>No, We need to install it manually.</p>

<p>2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?</p>
<h3><i>Answer</i></h3>
<p>Actually pyinputplus is too long, to make it short and crisp we import it as pyip like import tensorflow as tf.</p>

<p>3. What is the difference between inputInt() and inputFloat()?</p>
<h3><i>Answer</i></h3>
<p>inputInt() inputs only integer value whereas inputFloat() inputs both integers and decimal values.</p>

<p>4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?</p>
<h3><i>Answer</i></h3>

```
import pyinputplus as pyip
response = pyip.inputNum('Enter num: ', greaterThan=0, lessThan=99)
```

<p>5. What is passed to the allowRegexes and blockRegexes keyword arguments?</p>
<h3><i>Answer</i></h3>
<p>The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.</p>

<p>6. What does inputStr(limit=3) do if blank input is entered three times?</p>
<h3><i>Answer</i></h3>
<p>limit is used for the number of times to reprompts users and a timeout if users are required to respond within a time limit.</p>

<p>7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?</p>
<h3><i>Answer</i></h3>
<p>'Blank values are not allowed' Message will be showing three times. and 'hello' will be stored as the value for the variable by default.</p>
