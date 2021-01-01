import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
sheet = openpyxl.load_workbook('Book1.xlsx')
select_sheet = sheet['Sheet1']
for i in select_sheet['A1':'C3']:
    for j in i:
        print(j.coordinate, j.value)
    print("--End of row--")
