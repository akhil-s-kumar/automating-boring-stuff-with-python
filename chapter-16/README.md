<h2>Answers to the Practice Questions from chapter 16</h2>

<p>1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?</p>
<h3><i>Answer</i></h3>
<p>Spreadsheets have different data types other than strings, whereas CSV files only have strings as data type.</p>


<p>2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?</p>
<h3><i>Answer</i></h3>
<p>In cs.reader() we pass the csv file object and in csv.writer() we pass the csv file object along with write argument.</p>


<p>3. What modes do File objects for reader and writer objects need to be opened in?</p>
<h3><i>Answer</i></h3>
<p>'rb' and 'wb'</p>


<p>4. What method takes a list argument and writes it to a CSV file?</p>
<h3><i>Answer</i></h3>

```
import csv
File = open('example.csv', 'w', newline='')
headWriter = csv.DictWriter(outputFile, ['Name', 'Class', 'Phone'])
headWriter.writeheader()
headWriter.writerow(['Akhil', 'EAC', '1234567890'])
```


<p>5. What do the delimiter and lineterminator keyword arguments do?</p>
<h3><i>Answer</i></h3>
<p>The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline. </p>


<p>6. What function takes a string of JSON data and returns a Python data structure?</p>
<h3><i>Answer</i></h3>

```
import json
JsonData = '{"Name": "Akhil", "Class": "EAC", "Phone": 1234567890}'
DataAsPythonValue = json.loads(JsonData)
print(DataAsPythonValue)
```


<p>7. What function takes a Python data structure and returns a string of JSON data?</p>
<h3><i>Answer</i></h3>

```
import json
PythonData = {"Name": "Akhil", "Class": "EAC", "Phone": 1234567890}
DataAsJsonValue = json.dumps(pythonData)
print(DataAsJsonValue)
```
