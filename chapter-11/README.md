<h2>Answers to the Practice Questions from chapter 11</h2>

<p>1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.</p>
<h3><i>Answer</i></h3>

```
assert spam >= 10, 'spam variable is less than 10.'
```

<p>2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).</p>
<h3><i>Answer</i></h3>

```
assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!' or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'
```

<p>3. Write an assert statement that always triggers an AssertionError.</p>
<h3><i>Answer</i></h3>

```
assert false, 'This assertion is forever!'
```

<p>4. What are the two lines that your program must have in order to be able to call logging.debug()?</p>
<h3><i>Answer</i></h3>

```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
```

<p>5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?</p>
<h3><i>Answer</i></h3>

```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
```

<p>6. What are the five logging levels?</p>
<h3><i>Answer</i></h3>
<p>DEBUG, INFO, WARNING, ERROR, and CRITICAL</p>

<p>7. What line of code can you add to disable all logging messages in your program?</p>
<h3><i>Answer</i></h3>

```
logging.disable(logging.CRITICAL)
```

<p>8. Why is using logging messages better than using print() to display the same message?</p>
<h3><i>Answer</i></h3>
<p>Logging messages provide a trail of breadcrumbs that can help you figure out when things started to go wrong.</p>

<p>9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?</p>
<h3><i>Answer</i></h3>
<p> Step In - Execute the next line of code, Step Out - Execute lines of code at full speed until it returns from the current function, Step Over - Execute the next line of code.</p>

<p>10. After you click Continue, when will the debugger stop?</p>
<h3><i>Answer</i></h3>
<p>The debugger stops when it reached the end of the program.</p>

<p>11. What is a breakpoint?</p>
<h3><i>Answer</i></h3>
<p>It is a specific line of code that forces the debugger to pause whenever the program execution reaches that line.</p>

<p>12. How do you set a breakpoint on a line of code in Mu?</p>
<h3><i>Answer</i></h3>
<p>Not using Mu, using VS code instead.</p>
