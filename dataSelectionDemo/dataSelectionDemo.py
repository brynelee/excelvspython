import pandas as pd

# data loading
df = pd.read_excel(r"./test1-null-dup-cases.xls")
# data preprocessing
df3 = df.fillna({"Postal Code":"900000"})
df4 = df3.drop_duplicates()
df5 = df4.set_index("Row ID")

# 普通索引
df51 = df5[["Order ID", "Sales", "Profit"]]
print(df51)
print('*'*100)

# 位置索引

## 行筛选
## loc可以是字段筛选
## iloc是数字索引筛选
df52 = df5.loc[0:8]
print(df52)
print('*'*100)

df53 = df5.iloc[0:8]
print(df53)
print('*'*100)

## 列筛选

df54 = df5.iloc[0:8, 0:10]
print(df54)
print('*'*100)

df55 = df5.iloc[:, 0:10]
print(df55)
print('*'*100)

# 值过滤

df56 = df5[(df5["Sales"] > 900) & (df5["Profit"] < 90)]
df57 = df56[["Product Name", "Sales", "Profit"]]
print(df57)
print('*'*100)

# 写入excel文件
# DataFrame.to_excel(...)
# df57.to_excel("./back.xlsx")
