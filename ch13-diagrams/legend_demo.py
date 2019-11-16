import numpy as np
import matplotlib.pyplot as plt

# %config InlineBackend.figure_format = 'svg'

x = range(0, 100)

half_x = range(0, 50)

y = [np.random.randn() for i in range(0, 100)]

half_y = [y[i*2] for i in range(int(len(y)/2))]

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = 'SimHei'

# 创建2x2坐标图
# 在第一个图里面绘图
plt.subplot(2,2,1)
plt.plot(x,y, color='red', label="折线图")
plt.plot(half_x, half_y, color='green', label="半数抽样")
plt.grid(b = 'True')
plt.legend()
plt.title(label="折线图演示标题")

# 在第四个图里面绘图
plt.subplot(2,2,4)
plt.bar(x, y, label="柱形图")
plt.grid(b = 'True', axis = "x", linewidth=2)
plt.legend()
plt.title(label="柱形图演示标题")

plt.show()