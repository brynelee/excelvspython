import pandas as pd

print('demo of pandas.Series')

S1 = pd.Series(['a', 'b', 'c', 'd'])
print(S1)
print('='*100)

S2 = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])
print(S2)
print('='*100)

# create by dict
S3 = pd.Series({"a":1, "b":2, "c":3, "d":4})
print(S3)
print(S3.index)
print(S3.values)

print('='*100)
print('='*100)

# demo of DataFrame
print('demo of pandas.DataFrame')
df1 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']])
print(df1)
print('='*100)

df2 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']], 
    index = ["一", "二", "三", "四"])
print(df2)
print('='*100)

df3 = pd.DataFrame([['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']], 
    columns = ['小写', '大写'],
    index = ["一", "二", "三", "四"])
print(df3)
print(df3.iloc[0])
print('='*100)

data = {"小写":['a1', 'b1', 'c1', 'd1'],
        '大写':['A1', 'B1', 'C1', 'D1']}
df4 = pd.DataFrame(data, index = ["一", "二", "三", "四"])
print(df4)
print(df4.columns)
print(df4.index)
print('='*100)

