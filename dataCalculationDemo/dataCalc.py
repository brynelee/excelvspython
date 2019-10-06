import pandas as pd

# data loading
df = pd.read_excel(r"./dataOperationDemo/test1-null-dup-cases.xls")
# data preprocessing
df3 = df.fillna({"Postal Code":"900000"})
df4 = df3.drop_duplicates()
df5 = df4.set_index("Row ID")

df8 = df5.loc[:10, ["Product ID", "State", "Region", "Sales", "Discount", "Profit"]]

df9 = df8.mean()
print(df9)
print("*"*100)

df10 = df8.sum()
print(df10)
print("*"*100)

df11 = df8.count()
print(df11)
print("*"*100)

df12 = df5.max()
print("max is: \n", df12)
print("*"*100)

df13 = df5.median()
print("median is: \n", df13)
print("*"*100)

df14 = df5["Region"].mode()
print(df14)
print("*"*100)

var_df5 = df5.var()
print("var of df5 are: \n", var_df5)
print("*"*100)

std_df5 = df5.std()
print("std of df5 are: \n", std_df5)
print("*"*100)

# 分位数，25%， 50%， 75%
q25 = df5.quantile(0.25)
q75 = df5.quantile(0.75)
print("25% quantile is: \n", q25)
print("75% quantile is: \n", q75)
print("*"*100)

corr_df5 = df5.corr()
print(corr_df5)
print("*"*100)