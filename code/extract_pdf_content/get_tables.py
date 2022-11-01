'''
Using tabula-py. Able to read pdf table into pandas DFs

Dependencies: tabula-py
'''

import tabula

tables = tabula.read_pdf("example.pdf", pages="all")
df = tables[0]
print(type(df))
print(df)