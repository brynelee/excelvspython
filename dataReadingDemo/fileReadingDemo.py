import pandas as pd

# df1 = pd.read_csv(r"./train-pivot.csv", sep="\t", encoding="utf-8")
# encoding="utf-8", sep=" ", sep="\t", etc.
df1 = pd.read_csv(r"./train-pivot.csv", encoding="gbk")
print(df1)
print('='*100)

# import txt file
df11 = pd.read_table(r"./train-pivot.txt", sep=",", encoding="gbk")
print(df11)
print('='*100)


# 操作xls
# sheet_name="Sheet1", sheet_name = 0
# index_col = 0
# header = 0
# hearer = None (使用默认的0开始的列索引）
# usecols = [0, 2] 导入两列
# engine = "python", encoding = "utf-8-sig"p
df2 = pd.read_excel(r"./test1.xls")
print(df2)
print('='*100)

print(df2.shape)
print('='*100)
print(df2.info())
print('='*100)
print(df2.describe())
print('='*100)


# 操作xlsx
# df3 = pd.read_excel(r"./excelData/customer-service.xlsx", nrows=100)
# print(df3)
# print('='*100)

