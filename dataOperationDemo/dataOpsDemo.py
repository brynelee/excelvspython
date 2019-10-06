import pandas as pd

# data loading
df = pd.read_excel(r"./dataOperationDemo/test1-null-dup-cases.xls")
# data preprocessing
df3 = df.fillna({"Postal Code":"900000"})
df4 = df3.drop_duplicates()
df5 = df4.set_index("Row ID")

# 过滤
# df6是过滤后的子集
df6 = df5[df5["Region"] == "South"]
print(df6)
print('*'*100)

# 替换
df5["Region"].replace("South", "Southern", inplace=True)
print(df5)
# print(df5[["Region", "Sales"]].loc[:20])
print(df5.loc[:20, ["Region", "Sales", "Profit"]])
print('*'*100)

# 多对一替换
df5["Region"].replace({"Southern":"South", "East":"Eastern", "West":"Western"}, inplace=True)
print(df5)
print(df5.loc[:40, ["Region", "Sales", "Profit"]])
print('*'*100)

# 排序
df7 = df4.set_index("Row ID")
df8 = df7.sort_values(by = ["Sales", "Profit"], ascending = [False, False])
df9 = df8.loc[:10, ["Region", "Sales", "Profit"]]
# 由于重新排序，因此需要reset_index才能够按照序列进行打印
df9.reset_index()
print(df9.iloc[:10])
print('*'*100)

# df7.to_excel("./back1.xlsx")
# df8.to_excel("./back2.xlsx")

# 排名rank(method = "min")
# method = "average"
df10 = df7["Profit"].rank(method = "min")
print(df10.iloc[:10])
print('*'*100)


# 删除drop
# 两种方式，使用axis，或者使用columns
df11 = df7.drop(["Sales", "Profit"], axis = 1)
df12 = df7.drop(columns = ["Discount", "Quantity"])
print(df11)
print(df12)
print('*'*100)

# 计数
# value_counts(normalize = False, sort = True)
# 结果是pandas.Series
df13 = df7["Region"].value_counts()
print(df13)
print('='*100)

# 唯一值
df14 = df7["Region"].unique()
print(df14)
print('='*100)

# 查找
df15 = df7[:10]
S16 = df15["Sub-Category"].isin(["Phones", "Art"])
print(S16)
print('='*100)

# 区间切分
# cut方法
# 输入需要是序列，不能是DataFrame
S17 = pd.cut(df7["Quantity"], bins=[1, 5, 10, 15])
print(S17)
print('='*100)
# qcut根据区间数量自动切分
S18 = pd.qcut(df7["Quantity"], 3)
print(S18)
print('='*100)

S19 = pd.qcut(df7["Sales"], 3)
print(S19)
print('='*100)

# 创建新的列，依据区间来定义内容（打标记）
# lambda表达式用来生成内容
df7["SalesLevel"] = df7["Sales"].apply(lambda x: "High" if x > 149.023 else "Middle" if x > 27.784 else "Low")
print(df7)
print(df7.info())
print('='*100)

# 数据转置
df20 = df7.loc[:10, ["Product ID", "State", "Region", "Sales", "Discount", "Profit"]]
df21 = df20.T
print(df21)
df22 = df21.T
print(df22)
print('='*100)

# 宽表转换成窄表
# stack
# melt 和 pivot 用来进行宽表和窄表的转换
df23 = df20.reset_index().set_index(["Row ID", "State", "Region"]).stack().reset_index()
print(df23)
print('='*100)

'''
df24 = df23.pivot_table(index=["Row ID", "State", "Region"], columns="Performance", values = 0)
print(df24)
print('='*100)

'''

sdf1 = pd.read_excel(r"./dataOperationDemo/simpleData4Map.xlsx")
print(sdf1)
print('='*100)

sdf2 = sdf1["C1"].apply(lambda x:x+1)
print(sdf2)
print('='*100)

sdf3 = sdf1.applymap(lambda x:x+1)
print(sdf3)
print('='*100)



