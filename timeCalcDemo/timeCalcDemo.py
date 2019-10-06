import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pandas.tseries.offsets import Day

print(datetime.now())
print(datetime.now().year)

print(datetime.now().isocalendar())

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("*"*100)

now = datetime.now()
str_now = str(now)
print(str_now)
print("*"*100)
print("*"*100)

# 时间索引的创建和使用
print("demo of usage of DatetimeIndex")
print("*"*100)
index = pd.DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03',
                          '2018-01-04', '2018-01-05', '2018-01-06',
                          '2018-01-07', '2018-01-08', '2018-01-09',
                          '2018-01-10', '2018-02-01', '2018-02-02',
                          '2018-02-03', '2018-02-04', '2018-02-05',
                          '2018-02-06'])
data = pd.DataFrame(np.arange(1, 17), columns=["num"], index=index)
print(data)
print("*"*100)

print(data["2018-02"])
print("*"*100)

print(data["2018-01-09":"2018-02-05"])
print("*"*100)

# data loading
df = pd.read_excel(r"./dataOperationDemo/test1-null-dup-cases.xls")
# data preprocessing
df3 = df.fillna({"Postal Code":"900000"})
df4 = df3.drop_duplicates()
df5 = df4.set_index("Row ID")

df6 = df5.loc[:30, ["Product ID", "Order Date", "State", "Region", "Sales", "Discount", "Profit"]]

print(df6)
print("*"*100)

# 查看数据所在的时间范围
dateRange = df6["Order Date"].unique()
print(dateRange)
print("*"*100)

# 选取2016年的数据
df7 = df6[(df6["Order Date"] > datetime(2016,1,1)) & (df6["Order Date"] < datetime(2016,12,31))]
print(df7)
print("="*100)

dateRecords = df6["Order Date"]
print(dateRecords.mean())
print("="*100)

dateRecordsMinusOne1 = dateRecords - timedelta(days = 1)
print(dateRecordsMinusOne1[:3])
print("="*100)

dateRecordsMinusOne2 = dateRecords - Day(1)
print(dateRecordsMinusOne2[:3])
print("="*100)
