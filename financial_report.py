import akshare as ak

symbol = "现金流量表"

df = ak.stock_financial_report_sina(stock="600998", symbol=symbol)
df
print(df)


df2 = df.set_index('报告日')
df2 = df2.T
df2
df2.to_excel('九州通现金流量表.xlsx')

df2 = df.set_index('更新日期')
df2 = df2.T
df2
df2.to_excel('九州通现金流量表.xlsx')

# # AttributeError: module 'akshare' has no attribute 'stock_zh_a_balance_sheet'

# import sys
# print(sys.executable)