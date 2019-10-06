import pandas as pd

# data loading
df = pd.read_excel(r"./dataOperationDemo/test1-null-dup-cases.xls")
# data pre-processing
df3 = df.fillna({"Postal Code":"900000"})
df4 = df3.drop_duplicates()
df5 = df4.set_index("Row ID")

df6 = df5.loc[:100, ["Product ID", "State", "Region", "Category", "Sales", "Discount", "Profit"]]
print(df6[:10])
print('='*100)

# 单字段分组
df7 = df6.groupby("Region")
df7_count = df7["Category"].count()
df7_sum = df7.sum()
df7_mean = df7.mean()
print(df7_count)
print(df7_sum)
print(df7_mean)
print('='*100)

# 分组汇总计算 groupby()
df71 = df6.groupby("Region")["Sales", "Profit"].mean()
print(df71)
print('='*100)

# 双字段分组
# df8 = df6.groupby(["Region", "State"])
df8 = df6.groupby(["Region", "State"])["Sales", "Profit"]
df8_sum = df8.sum()
df8_mean = df8.mean()
print(df8_sum)
print(df8_mean)
print('='*100)

# 分组汇总 aggregate()
df9 = df6.groupby("Region").aggregate(["count", "sum", "mean", "median"])
print(df9)
print('='*100)

# 分组汇总，aggregate()，使用分字段不同种类操作的方式
df10 = df6.groupby("Region").aggregate({"Category":"count", "Sales":"sum", "Profit":["sum", "mean"]})
print(df10)
print('='*100)

df10.reset_index()
print(df10)