import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
y = np.arange(6)

fig,axes = plt.subplots(2,2)

axes[0,0].plot(x,y)

axes[1,1].bar(x,y)

plt.show()
