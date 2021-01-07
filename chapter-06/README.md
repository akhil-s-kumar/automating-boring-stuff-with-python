<h2>Answers to the Practice Questions from chapter 06</h2>

<p>1. What are escape characters?</p>
<h3><i>Answer</i></h3>
<p>It is represented by a '\' backslash, used for representing whitespaces.</p>

<p>2. What do the \n and \t escape characters represent?</p>
<h3><i>Answer</i></h3>
<p>'\t' - tab, '\n' - new line</p>

<p>3. How can you put a \ backslash character in a string?</p>
<h3><i>Answer</i></h3>
<p>\\</p>

<p>4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?</p>
<h3><i>Answer</i></h3>
<p>Because double quotes are used both for begining and end of the string.</p>

<p>5. If you don’t want to put \n in your string, how can you write a string with newlines in it?</p>
<h3><i>Answer</i></h3>
<p>Using Triple quotes makes into multiline string.</p>

<p>6. What do the following expressions evaluate to?</p>

```
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```

<h3><i>Answer</i></h3>
<p>'e', 'Hello', 'Hello', 'lo, world!'</p>

<p>7. What do the following expressions evaluate to?</p>

```
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```

<h3><i>Answer</i></h3>
<p>'HELLO', True, 'hello'</p>

<p>8. What do the following expressions evaluate to?</p>

```
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```

<h3><i>Answer</i></h3>
<p>['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.'], 'There-can-be-only-one.'</p>

<p>9. What string methods can you use to right-justify, left-justify, and center a string?</p>
<h3><i>Answer</i></h3>
<p>rjust(), ljust(), and center()</p>

<p>10. How can you trim whitespace characters from the beginning or end of a string?</p>
<h3><i>Answer</i></h3>
<p>lstrip() and rstrip</p>
