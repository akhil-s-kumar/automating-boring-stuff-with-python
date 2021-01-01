import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
sheet = openpyxl.load_workbook('Book1.xlsx')
select_sheet = sheet['Sheet1']
for i in list(select_sheet.columns)[1]:
    print(i.value)
