import openpyxl
sheet = openpyxl.load_workbook('Book1.xlsx')
print(sheet.sheetnames)
