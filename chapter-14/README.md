<h2>Answers to the Practice Questions from chapter 14</h2>

<p>1. What three files do you need for EZSheets to access Google Sheets?</p>
<h3><i>Answer</i></h3>
<p>credentials-sheets.json, token-sheets.pickle, token-drive.pickle</p>

<p>2. What two types of objects does EZSheets have?</p>
<h3><i>Answer</i></h3>
<p>Spreadsheet object and Sheet object.</p>

<p>3. How can you create an Excel file from a Google Sheet spreadsheet?</p>
<h3><i>Answer</i></h3>
<p>Using downloadAsExcel() function we can download spreadsheet into excel file</p>

<p>4. How can you create a Google Sheet spreadsheet from an Excel file?</p>
<h3><i>Answer</i></h3>
<p>Using ezsheets.upload('example.xlsx')</p>

<p>5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?</p>
<h3><i>Answer</i></h3>

 ```
 import ezsheets
 ss = ezsheets.createSpreadsheet('My Spreadsheet')
 ss.createSheet('Students')
 sheet = ss[1]
 a = sheet['B2']
 print(a)
 ```

<p>6. How can you find the column letters for column 999?</p>
<h3><i>Answer</i></h3>

```
ezsheets.getColumnLetterOf(2)
```

<p>7. How can you find out how many rows and columns a sheet has?</p>
<h3><i>Answer</i></h3>

```
sheet.rowCount
sheet.columnCount
```

<p>8. How do you delete a spreadsheet? Is this deletion permanent?</p>
<h3><i>Answer</i></h3>
<p>Deleting sheets is permanent.</p>

```
import ezsheets
ss = ezsheets.createSpreadsheet('My Spreadsheet')
ss.createSheet('Students')
sheet = ss[1]
sheet.delete()
```

<p>9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?</p>
<h3><i>Answer</i></h3>

```
import ezsheets
ss = ezsheets.createSpreadsheet('My Spreadsheet')
ss.createSheet('Students')
```

<p>10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?</p>
<h3><i>Answer</i></h3>
<p>Attempting to exceed this quota will raise the googleapiclient.errors.HttpError “Quota exceeded for quota group” exception.</p>
