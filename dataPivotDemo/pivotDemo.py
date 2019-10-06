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

df7 = pd.pivot_table(df6, values=["Category", "Sales", "Profit"],
                     index=["Region", "State"],
                     aggfunc={"Category":"count", "Sales":["sum", "mean"], "Profit":["sum", "mean", "median", "max"]})
print(df7)
print('='*100)

df8 = df7.reset_index()
print(df8)
print('='*100)

df8.to_excel("./dataPivotDemo/pivotDemo_output.xlsx")
