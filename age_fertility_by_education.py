import openpyxl

workbook =openpyxl.load_workbook("Age-Specific-Fertility-Rates-by-Education-Attainment-2019.xlsx")

sheet=workbook.active
for row in sheet.iter_rows(values_only=True):
    for cell in row:
        print(cell)