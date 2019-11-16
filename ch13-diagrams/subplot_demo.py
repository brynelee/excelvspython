import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
y = np.arange(6)

# 创建2x2坐标图，在第一个图里面绘图
plt.subplot(2,2,1)
plt.plot(x,y)

# 在第四个图里面绘图
plt.subplot(2,2,4)
plt.bar(x,y)

plt.show()
