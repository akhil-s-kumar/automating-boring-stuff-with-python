<h2>Answers to practice questions from chapter 4</h2>

<p>1. What is []?</p>
<h3><i>Answer</i></h3>
<p>Lists are mutable data type, represented as []</p>

<p>2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)</p>
<h3><i>Answer</i></h3>
<p>spam[2]='hello'</p>

<p>For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].</p>
<p>3. What does spam[int(int('3' * 2) // 11)] evaluate to?</p>
<h3><i>Answer</i></h3>
<p>'d'</p>

<p>4. What does spam[-1] evaluate to?</p>
<h3><i>Answer</i></h3>
<p>'d'</p>

<p>5. What does spam[:2] evaluate to?</p>
<h3><i>Answer</i></h3>
<p>['a','b']</p>

<p>For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].</p>
<p>6. What does bacon.index('cat') evaluate to?</p>
<h3><i>Answer</i></h3>
<p>1</p>

<p>7. What does bacon.append(99) make the list value in bacon look like?</p>
<h3><i>Answer</i></h3>
<p>[3.14, 'cat', 11, 'cat', True, 99]</p>

<p>8. What does bacon.remove('cat') make the list value in bacon look like?</p>
<h3><i>Answer</i></h3>
<p>[3.14, 11, 'cat', True]</p>

<p>9. What are the operators for list concatenation and list replication?</p>
<h3><i>Answer</i></h3>
<p>Concatination: '+', replication: '*'</p>

<p>10. What is the difference between the append() and insert() list methods?</p>
<h3><i>Answer</i></h3>
<p>Append adds element at the last of the list, whereas insert can place an element in a position wherever we want to.</p>

<p>11. What are two ways to remove values from a list?</p>
<h3><i>Answer</i></h3>
<p>pop, remove</p>

<p>12. Name a few ways that list values are similar to string values.</p>
<h3><i>Answer</i></h3>
<p>len(), concatination, replication</p>

<p>13. What is the difference between lists and tuples?</p>
<h3><i>Answer</i></h3>
<p>Lists are mutable data types while tuples are immutable data types.</p>

<p>14. How do you type the tuple value that has just the integer value 42 in it?</p>
<h3><i>Answer</i></h3>
<p>a = (42,) if it has only one element ',' should be used at the end.</p>

<p>15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?</p>
<h3><i>Answer</i></h3>
<p>tuple() & list()</p>

<p>16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?</p>
<h3><i>Answer</i></h3>
<p>Reference of the list value</p>

<p>17. What is the difference between copy.copy() and copy.deepcopy()?</p>
<h3><i>Answer</i></h3>
<p>The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list</p>
