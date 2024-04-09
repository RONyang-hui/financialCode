import pdfplumber
import pandas as pd

# Open the PDF file
with pdfplumber.open('贵州茅台2021年年度报告.pdf') as pdf:
    # Extract tables from specific pages
    tb1 = pdf.pages[49].extract_table()
    tb2 = pdf.pages[40].extract_table()
    tb3 = pdf.pages[51].extract_table()

# Check if the table extraction was successful
if tb1 is not None:
    # Extract the column names
    columns = tb1[0]
    # Create the DataFrame
    df1 = pd.DataFrame(tb1[1:], columns=[f'Column_{i}' for i in range(len(columns))])
else:
    df1 = pd.DataFrame()

if tb2 is not None:
    # Extract the column names
    columns = tb2[0]
    # Create the DataFrame
    df2 = pd.DataFrame(tb2[1:], columns=[f'Column_{i}' for i in range(len(columns))])
else:
    df2 = pd.DataFrame()

if tb3 is not None:
    # Extract the column names
    columns = tb3[0]
    # Create the DataFrame
    df3 = pd.DataFrame(tb3[1:], columns=[f'Column_{i}' for i in range(len(columns))])
else：
    df3 = pd.DataFrame()

# Concatenate the DataFrames
df4 = pd.concat([df1, df2, df3], ignore_index=True)

# Save the DataFrame to an Excel file
df4.to_excel('贵州茅台2021年年度报告财务数据.xlsx', index=False)