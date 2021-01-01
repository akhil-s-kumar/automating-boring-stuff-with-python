import openpyxl
sheet = openpyxl.load_workbook('Book1.xlsx')
print(type(sheet))
active_sheet = sheet.active
print(active_sheet)
print(active_sheet.title)
