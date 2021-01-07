<h2>Answers for practice questions from chapter 5</h2>

<p>1. What does the code for an empty dictionary look like?</p>
<h3><i>Answer</i></h3>
<p>{}</p>


<p>2. What does a dictionary value with a key 'foo' and a value 42 look like?</p>
<h3><i>Answer</i></h3>
<p>{'foo':4}</p>


<p>3. What is the main difference between a dictionary and a list?</p>
<h3><i>Answer</i></h3>
<p>Dictionary uses key value pair, means there is key for every values whereas list doesn't, lists are ordered and dictionary are unordered.</p>


<p>4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?</p>
<h3><i>Answer</i></h3>
<p>KeyError</p>


<p>5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?</p>
<h3><i>Answer</i></h3>
<p>No, difference both checks whether the key exists or not.</p>


<p>6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?</p>
<h3><i>Answer</i></h3>
<p>'cat' in spam checks whether a key exist or not and 'cat' in spam.values() checks whether this value exists for a key or not.</p>


<p>7. What is a shortcut for the following code?</p>

```
if 'color' not in spam:
    spam['color'] = 'black'
```

<h3><i>Answer</i></h3>
<p>spam.setdefault('color', 'black')</p>


<p>8. What module and function can be used to “pretty print” dictionary values?</p>
<h3><i>Answer</i></h3>
<p>pprint.pprint()</p>
