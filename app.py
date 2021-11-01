import htmltabletomd
from datetime import date
today = date.today()
d1 = today.strftime("%d-%m-%Y")
with open('table.html','r') as file:
    countriesStr = file.read()
html_table = countriesStr
md_table = htmltabletomd.convert_table(html_table)
print(md_table)
file = open("Python.md", "w")
file.write("######**Success Report ("+d1+")**")
file.write("\n")
file.write(md_table)
file.close()
