import htmltabletomd
with open('table.html','r') as file:
    countriesStr = file.read()
#print(countriesStr)

html_table = countriesStr


md_table = htmltabletomd.convert_table(html_table)
print(md_table)