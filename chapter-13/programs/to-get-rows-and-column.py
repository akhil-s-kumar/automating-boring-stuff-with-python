import openpyxl
sheet = openpyxl.load_workbook('Book1.xlsx')
select_sheet = sheet['Sheet1']
item = select_sheet['A2'].value
print(item)
item2 = select_sheet['B2']
print('cell %s is %s'%(item2.coordinate, item2.value))
print('Row %s and column %s is %s'%(item2.row, item2.column, item2.value))
