import pdfplumber
import pandas as pd

with pdfplumber.open('贵州茅台2021年年度报告.pdf') as pdf:
    tb1 = pdf.pages[49].extract_table()
    tb2 = pdf.pages[50].extract_table()
    tb3 = pdf.pages[51].extract_table()
t1 = tb1[0]
name = t1[0]
df1 = pd.DataFrame(t1[1:], columns=['项目'])
# Pass the column name as a list
df1

print(df1)

# TypeError: Index(...) must be called with a collection of some kind, '项目' was passed
print(df1.dtypes)


t2 = tb2[0]
df2 = pd.DataFrame(t2, columns=[name])
df2
print(df1)
tb3[0]
t3 = tb3[0]
df3 = pd.DataFrame(t3, columns=[name])
df3
print(df3)

df4 = pd.concat([df1, df2, df3])
df4
print(df4)

df4.to_excel('贵州茅台2021年年度报告财务数据.xlsx')