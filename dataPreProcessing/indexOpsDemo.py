import pandas as pd

df = pd.read_excel(r"./multiLevelIndex.xlsx")
print(df)
print('*'*100)

df2 = df.reset_index()
print(df2)
