<h2>Answers to the Practice Questions from chapter 20</h2>

<p>1. What does the openpyxl.load_workbook() function return?</p>
<h3><i>Answer</i></h3>
<p>openpyxl.load_workbook() function will returns the data file which is in the format xlxs and loads into the program.</p>

<p>2. What does the wb.sheetnames workbook attribute contain?</p>
<h3><i>Answer</i></h3>
<p>wb.sheetnames will contain all the sheets names in the loaded data file.</p>

<p>3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet3'] 
```

<p>4. How would you retrieve the Worksheet object for the workbook’s active sheet?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
print(wb.active)
```

<p>5. How would you retrieve the value in the cell C5?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1'] 
print(sheet['A1'].value)
```

<p>6. How would you set the value in the cell C5 to "Hello"?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1'] 
sheet['C5'] = "Hello"
```

<p>7. How would you retrieve the cell’s row and column as integers?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1'] 
sheet.cell(row=2, column=2)
```

<p>8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?</p>
<h3><i>Answer</i></h3>
<p>sheet.max_column and sheet.max_row contains the total number of rows and columns in the data file and is in 'int' type</p>

<p>9. If you needed to get the integer index for column 'M', what function would you need to call?</p>
<h3><i>Answer</i></h3>

```
column_index_from_string('M')
```

<p>10. If you needed to get the string name for column 14, what function would you need to call?</p>
<h3><i>Answer</i></h3>

```
get_column_letter(14)
```

<p>11. How can you retrieve a tuple of all the Cell objects from A1 to F1?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'F1']) )
```

<p>12. How would you save the workbook to the filename example.xlsx?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1']
wb.save('example.xlsx') 
```

<p>13. How do you set a formula in a cell?</p>
<h3><i>Answer</i></h3>

```
sheet['A6'] = '=SUM(A1:A5)'
```

<p>14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?</p>
<h3><i>Answer</i></h3>
<p></p>

<p>15. How would you set the height of row 5 to 100?</p>
<h3><i>Answer</i></h3>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1']
sheet.row_dimensions[5].height = 100
```

<p>16. How would you hide column C?</p>
<h3><i>Answer</i></h3>

```
sheet.column_dimensions['C'].hidden = True
```

<p>17. What is a freeze pane?</p>
<h3><i>Answer</i></h3>
<p>freez palnes helps to make the row and column fixed at the top even when scroll down.</p>

<p>18. What five functions and methods do you have to call to create a bar chart?</p>
<h3><i>Answer</i></h3>

```
openpyxl.charts.Reference()
openpyxl.charts.Series()
chartObj.append(seriesObj)
openpyxl.charts.BarChart()
add_chart()
