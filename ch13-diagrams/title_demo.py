import numpy as np
import matplotlib.pyplot as plt

# %config InlineBackend.figure_format = 'svg'

x = np.arange(6)
y = np.arange(6)

# 解决中文显示问题
plt.rcParams["font.sans-serif"] = 'SimHei'

# 创建2x2坐标图，在第一个图里面绘图
plt.subplot(2,2,1)
plt.plot(x,y)

# plt.xlabel("月份")
# plt.ylabel("注册量")
plt.xlabel("月份", labelpad=10, color="green", fontsize=20, fontweight = 'bold')
plt.ylabel("注册人数", labelpad=10)

# 在第四个图里面绘图
plt.subplot(2,2,4)
plt.bar(x,y)

plt.show()