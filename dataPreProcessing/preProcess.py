import pandas as pd

df = pd.read_excel(r"./test1-null-dup-cases.xls")
print(df)
print('='*100)
print(df.shape)
print('='*100)
print(df.info())
print('='*100)
print(df.describe())
print('='*100)

# 删除空值

df2 = df.dropna()
print(df2.info())
print('='*100)

df3 = df.fillna({"Postal Code":"900000"})
print(df3.info())
print('='*100)

# 数据去重

# drop_duplicates(subset = "id")
# drop_duplicates(subset = ["id", "name"], keep = "first")
# keep = "first", "last", False
df4 = df3.drop_duplicates()
print(df4.info())
print('='*100)

# 数据类型转换
# pandas: int, float, object, string_, unicode_, datetime64[ns]
print(df4["Discount"].dtype)
# df4["Discount"].astype("float64")
print('='*100)

print(df4.columns)
print('='*100)

print(df4.index)
print(df4["Row ID"])
df5 = df4.set_index("Row ID")
print(df5.index)
print('='*100)

df6 = df5.rename(columns = {"Order ID":"Order_ID"})
print(df6)
print('='*100)

sub_df6 = df6[["Order_ID", "Sales", "Profit"]]
print(sub_df6)
print('='*100)

# reset_index()
# reset_index(level = 0) 将第0级索引转化为columns
# reset_index(drop = True) 删除原索引




