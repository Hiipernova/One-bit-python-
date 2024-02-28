from openpyxl import load_workbook

wb = load_workbook("data/pivot_table.xlsx")
print(wb)
sheet = wb["Relatorio"]

print(sheet["A3"].value)
print(sheet["B3"].value)

for i in range(2, 6):
    ano =  sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print("{0} o Aston martin vendeu {1} e o Bentley vendeu {2}".format(ano, am, bt))