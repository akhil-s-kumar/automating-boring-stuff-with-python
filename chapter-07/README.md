<h2>Answers to Practice Questions from chapter 07</h2>

<p>1. re.compile function will create object pattern.</p>

<p>2. raw strings are used because it is useful when we want to have a string that contains backslash and don't want it to be treated as an escape character.</p>

<p>3. search method will returns the object that matches the pattern.</p>

<p>4. The group function will return the string that matched the pattern.</p>

<p>5. group(0) returns the entire string, group(1) returns string of first parentheses and group(2) returns the string of second parentheses.</p>

<p>6. \., \(, and \)</p>

<p>7. </p>

```
>>>import re
>>>a = re.compile(r'.at')
>>>b = a.findall('The cat in the hat sat on the flat mat.')
>>>print(b)
>>>['cat', 'hat', 'sat', 'lat', 'mat']
>>>print(b[0])
>>>'cat'
```

<p>8. '|' signify or</p>

<p>9. match zero or one of the preceding group.</p>

<p>10. + matches one or more and * matches zero or more.</p>

<p>11. {3} for three instances of the preceding group and {3,5} matches between three and five instances.</p>

<p>12. \d - single digit, \w - word, \s - space</p>

<p>13. \D, \W, and \S character classes match a single character that is not a digit, word, or space character, respectively</p>

<p>14. .* performs a greedy match, and the .*? performs a nongreedy match.</p>

<p>15. [0-9a-z]</p>

<p>16. re.IGNORECASE as the second argument in re.compile</p>

<p>17. If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.</p>

<p>18. 'X drummers, X pipers, five rings, X hens'</p>

<p>19. Helps to add whitespace and comments.</p>

<p>20. re.compile(r'^\d{1,3}(,\d{3})*$')</p>

<p>21. re.compile(r'[A-Z][a-z]*\sNakamoto')</p>

<p>22. re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)</p>
