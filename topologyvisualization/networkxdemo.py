import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 创建图
G = nx.Graph()  # 无多重边无向图

df1 = pd.read_csv("/Users/xiaodong/GitRoot/mathstudyjava/output/friendrellist.csv")
print(df1)

# print(df1.iloc[1])
# node = df1.iloc[1][0]
# print(df1.iloc[2])

# 添加节点
# for i in range(1, 30):
#    G.add_node(i)

dataarray = np.array(df1)

dataset = set()

for i in range(len(dataarray)):
    num1 = dataarray[i][0]
    num2 = dataarray[i][1]
    if num1 not in dataset:
        dataset.add(num1)
    if num2 not in dataset:
        dataset.add(num2)

print(dataset)
        
# 添加边
for i in range(0, 28):
    G.add_edge(df1.iloc[i][0],df1.iloc[i][1])
    
# 绘图
nx.draw_networkx(G, with_labels=True)

# 绘图
# nx.draw(G, pos=nx.random_layout(G), alpha=1, node_size=20, with_labels=True, node_color='white', font_size=20)

plt.figure(figsize=(50,50))

plt.show()