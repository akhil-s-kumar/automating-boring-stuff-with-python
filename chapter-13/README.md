<h2>Answers to the practice questions from chapter 13</h2>

<p>1. openpyxl.load_workbook() function will returns the data file which is in the format xlxs and loads into the program.</p>

<p>2. wb.sheetnames will contain all the sheets names in the loaded data file.</p>

<p>3. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet3'] 
```

<p>4. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
print(wb.active)
```

<p>5. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1'] 
print(sheet['A1'].value)
```

<p>6. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1'] 
sheet['C5'] = "Hello"
```

<p>7. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1'] 
sheet.cell(row=2, column=2)
```

<p>8. sheet.max_column and sheet.max_row contains the total number of rows and columns in the data file and is in 'int' type</p>

<p>9. column_index_from_string('M')</p>

<p>10. get_column_letter(14)</p>

<p>11. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'F1']) )
```

<p>12. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1']
wb.save('example.xlsx') 
```

<p>13. sheet['A6'] = '=SUM(A1:A5)'</p>

<p>14. </p>

<p>15. </p>

```
import openpyxl
wb = openpyxl.load_workbook('book1.xlsx')
sheet = wb['Sheet1']
sheet.row_dimensions[5].height = 70
```

<p>16. sheet.column_dimensions['C'].hidden = True</p>

<p>17. freez palnes helps to make the row and column fixed at the top even when scroll down.</p>

<p>18. openpyxl.charts.Reference(), openpyxl.charts.Series(), chartObj.append(seriesObj), openpyxl.charts. BarChart(), and add_chart()</p>
