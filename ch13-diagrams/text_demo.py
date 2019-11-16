import numpy as np
import matplotlib.pyplot as plt

# %config InlineBackend.figure_format = 'svg'

# 生成原始数据
x = range(0, 100)
y = [np.random.randn() for i in range(0, 100)]

# 对10分之一的数据进行采样，用来后续做标签
tenth_x = [x[i*10] for i in range(0,10)]
print(tenth_x)
tenth_y = [y[i*10] for i in range(0,10)]
print(tenth_y)

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = 'SimHei'

# 创建2x2坐标图
# 在第一个图里面绘图
plt.subplot(1,1,1)
plt.bar(x,y, color='red', label="折线图")
for i in range(0,10):
    plt.text(tenth_x[i], tenth_y[i], round(tenth_y[i],1), ha='center', va="bottom", fontsize=11)
plt.grid(b = 'True')
plt.legend()
plt.title(label="标记显示样例")

plt.show()