a=[('a','b','c','d','e','f','g','h'),
('aa','bb','cc','dd','ee','ff','gg','hh'),
('aaa','bbb','ccd','ddd','eee','fff','ggg','hhh')]
b=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print(a)
print(b)
print('*' * 20)

# 将每个b元素与列表a中的子列表的每个元素组合一遍形成字典
combined = [tuple(zip(b, i)) for i in a]

print(combined)
