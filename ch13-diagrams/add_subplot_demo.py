import numpy as np
import matplotlib.pyplot as plt

# %config InlineBackend.figure_format = 'svg'

x = np.arange(6)
y = np.arange(6)

# 对象式编程

# 先生成画布
# fig = plt.figure()
fig = plt.figure(figsize=(12,6))

# 生成4个坐标系
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# 在第一个和第四个坐标系里面绘图
ax1.plot(x,y)
ax4.bar(x,y)

plt.show()
