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

