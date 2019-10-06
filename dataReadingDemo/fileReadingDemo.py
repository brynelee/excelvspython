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
df2 = pd.read_excel(r"./test1.xls")
print(df2)
print('='*100)

# 操作xlsx
df3 = pd.read_excel(r"./excelData/customer-service.xlsx", nrows=10)
print(df3)
print('='*100)



