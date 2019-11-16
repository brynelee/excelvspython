import numpy as np
import matplotlib.pyplot as plt

# %config InlineBackend.figure_format = 'svg'

'''
fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

'''
x = np.arange(6)
y = np.arange(6)

plt.subplot2grid((2,2), (0,0))
plt.plot(x,y)

plt.subplot2grid((2,2), (0,1))
plt.bar(x,y)

plt.show()
