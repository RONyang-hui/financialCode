
import pdfplumber
import pandas as pd

with pdfplumber.open('贵州茅台2021年年度报告.pdf') as pdf:
    tb1 = pdf.pages[48].extract_table()
    tb2 = pdf.pages[49].extract_table()
    tb3 = pdf.pages[50].extract_table()

t1 = tb1[0]
name = t1[0]
df1 = pd.DataFrame(t1[1:], columns=name)

t2 = tb2[0]
df2 = pd.DataFrame(t2, columns=name)

t3 = tb3[0]
df3 = pd.DataFrame(tb3[1:], columns=name)

df4 = pd.concat([df1, df2, df3])
df4.to_excel('贵州茅台2021年年度报告财务数据.xlsx', index=False)