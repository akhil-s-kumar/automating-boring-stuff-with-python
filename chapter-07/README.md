<h2>Answers to the Practice Questions from chapter 07</h2>

<p>1. What is the function that creates Regex objects?</p>
<h3><i>Answer</i></h3>
<p>re.compile function will create object pattern.</p>

<p>2. Why are raw strings often used when creating Regex objects?</p>
<h3><i>Answer</i></h3>
<p>raw strings are used because it is useful when we want to have a string that contains backslash and don't want it to be treated as an escape character.</p>

<p>3. What does the search() method return?</p>
<h3><i>Answer</i></h3>
<p>search method will returns the object that matches the pattern.</p>

<p>4. How do you get the actual strings that match the pattern from a Match object?</p>
<h3><i>Answer</i></h3>
<p>The group function will return the string that matched the pattern.</p>

<p>5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?</p>
<h3><i>Answer</i></h3>
<p>group(0) returns the entire string, group(1) returns string of first parentheses and group(2) returns the string of second parentheses.</p>

<p>6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?</p>
<h3><i>Answer</i></h3>
<p>\., \(, and \)</p>

<p>7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?</p>
<h3><i>Answer</i></h3>

```
>>>import re
>>>a = re.compile(r'.at')
>>>b = a.findall('The cat in the hat sat on the flat mat.')
>>>print(b)
>>>['cat', 'hat', 'sat', 'lat', 'mat']
>>>print(b[0])
>>>'cat'
```

<p>8. What does the | character signify in regular expressions?</p>
<h3><i>Answer</i></h3>
<p>'|' signify or</p>

<p>9. What two things does the ? character signify in regular expressions?</p>
<h3><i>Answer</i></h3>
<p>match zero or one of the preceding group.</p>

<p>10. What is the difference between the + and * characters in regular expressions?</p>
<h3><i>Answer</i></h3>
<p>+ matches one or more and * matches zero or more.</p>

<p>11. What is the difference between {3} and {3,5} in regular expressions?</p>
<h3><i>Answer</i></h3>
<p>{3} for three instances of the preceding group and {3,5} matches between three and five instances.</p>

<p>12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?</p>
<h3><i>Answer</i></h3>
<p>\d - single digit, \w - word, \s - space</p>

<p>13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?</p>
<h3><i>Answer</i></h3>
<p>\D, \W, and \S character classes match a single character that is not a digit, word, or space character, respectively</p>

<p>14. What is the difference between .* and .*??</p>
<h3><i>Answer</i></h3>
<p>.* performs a greedy match, and the .*? performs a nongreedy match.</p>

<p>15. What is the character class syntax to match all numbers and lowercase letters?</p>
<h3><i>Answer</i></h3>
<p>[0-9a-z]</p>

<p>16. How do you make a regular expression case-insensitive?</p>
<h3><i>Answer</i></h3>
<p>re.IGNORECASE as the second argument in re.compile</p>

<p>17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?</p>
<h3><i>Answer</i></h3>
<p>If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.</p>

<p>18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?</p>
<h3><i>Answer</i></h3>
<p>'X drummers, X pipers, five rings, X hens'</p>

<p>19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?</p>
<h3><i>Answer</i></h3>
<p>Helps to add whitespace and comments.</p>

<p>20. How would you write a regex that matches a number with commas for every three digits? It must match the following:</p>

```
'42'
'1,234'
'6,368,745'

but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
```
<h3><i>Answer</i></h3>

```
re.compile(r'^\d{1,3}(,\d{3})*$')
```

<p>21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:</p>

```
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
```

<h3><i>Answer</i></h3>

```
re.compile(r'[A-Z][a-z]*\sNakamoto')
```

<p>22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:</p>

```
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'
```

<h3><i>Answer</i></h3>

```
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
```
