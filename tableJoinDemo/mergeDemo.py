import pandas as pd

df1 = pd.read_excel("./tableJoinDemo/tableRawData.xlsx", sheet_name="sheet1")
df2 = pd.read_excel("./tableJoinDemo/tableRawData.xlsx", sheet_name="sheet2")

print(df1)
print(df2)

print('='*100)

df1on2 = pd.merge(df1, df2, on = "学号")
print(df1on2)
print('='*100)

df4 = pd.read_excel("./tableJoinDemo/tableRawData.xlsx", sheet_name="Sheet4")
print(df4)
print('='*100)

df1on4 = pd.merge(df1, df4, left_on = "学号", right_on="编号")
print(df1on4)
print('='*100)

df11 = df1.set_index("学号")
df41 = df4.set_index("编号")
print(df11)
print(df41)
print('='*100)

df11on41 = pd.merge(df11, df41, left_index=True, right_index=True)
print(df11on41)
print('='*100)

df5 = pd.read_excel("./tableJoinDemo/tableRawData.xlsx", sheet_name="Sheet5")
print(df5)
print('='*100)

# 默认内连接，仅有公共数据部分作为结果
df1on5 = pd.merge(df1, df5, on="学号", how="inner")
print(df1on5)
print('='*100)

# 左连接
df1on5left = pd.merge(df1, df5, on="学号", how="left")
print(df1on5left)
print('='*100)

# 右连接
df1on5right = pd.merge(df1, df5, on="学号", how="right")
print(df1on5right)
print('='*100)

# 外连接，合并结果集为最大化
df1on5outer = pd.merge(df1, df5, on="学号", how="outer")
print(df1on5outer)
print('='*100)

