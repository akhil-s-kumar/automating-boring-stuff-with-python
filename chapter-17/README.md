<h2>Answers to the Practice Questions from chapter 17</h2>

<p>1. What is the Unix epoch?</p>
<h3><i>Answer</i></h3>
<p>The Unix epoch is a time reference commonly used in programming: 12 AM on January 1, 1970, Coordinated Universal Time (UTC).</p>

<p>2. What function returns the number of seconds since the Unix epoch?</p>
<h3><i>Answer</i></h3>

```
time.time()
```

<p>3. How can you pause your program for exactly 5 seconds?</p>
<h3><i>Answer</i></h3>

```
time.sleep(5)
```

<p>4. What does the round() function return?</p>
<h3><i>Answer</i></h3>
<p>It will convert into closest integers.</p>

```
>>>round(5.6)
>>>6
```

<p>5. What is the difference between a datetime object and a timedelta object?</p>
<h3><i>Answer</i></h3>
<p>datetime values represent a specific moment in time whereas timedelta represents a duration of time.</p>

<p>6. Using the datetime module, what day of the week was January 7, 2019?</p>
<h3><i>Answer</i></h3>

```
import datetime
day = datetime.datetime(2019, 1, 7)
weekd = day.weekday()
print(weekd) #0 is Monday and 6 is Sunday
```

<p>7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?</p>
<h3><i>Answer</i></h3>

```
threadObj = threading.Thread(target=spam)
threadObj.start()
```

<p>8. What should you do to avoid concurrency issues with multiple threads?</p>
<h3><i>Answer</i></h3>
<p>Never let multiple threads read or write the same variables.</p>
