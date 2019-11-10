import random
import pandas as pd

# using pandas DataFrame
# 直接使用DataFrame来构建原始数据

amount = 40
param1 = "参数1"
param2 = "参数2"
result = "结果"

x = pd.DataFrame()
col_name = [param1, param2, result]

for i in range(0,amount):
    y = {}
    y[param1] = int(random.random()*100)*10
    y[param2] = int(random.random()*10)
    y[result] = y[param1] * y[param2]
    # 根据字典来创建DataFrame，由于字典只有列定义，没有行索引，因此，临时使用index=[1]指定一个临时索引
    y_df = pd.DataFrame(y, index=[1])
    # 注意要append后赋值回给x，另外要注意这里面忽略了之前指定的临时索引
    x = x.append(y_df, ignore_index=True)

print(x)

'''
for i in range(0, amount):
    print(df[i][param1]," x ", df[i][param2], " = ")

for i in range(0, amount):
    print(df[i][param1], ' x ', df[i][param2], ' = ', df[i][result])

print(df)

'''
# 写入excel

export_file_name = r"./exported2.xlsx"

# df1.to_excel(excel_writer=r"./exported.xlsx", sheet_name="Qi Qi's calculations")
# df1.to_excel(excel_writer=r"./exported.xlsx", sheet_name="Qi Qi's calculations", index=False)
# df1.to_excel(excel_writer=r"./exported.xlsx", sheet_name="Qi Qi's calculations", index=False, columns=["x1", "x2"])
x.to_excel(excel_writer=export_file_name, 
    sheet_name="Qi Qi's calculations", 
    index=False, 
    columns=[param1, param2, result],
    encoding="utf-8")

