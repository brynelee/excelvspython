
# numpy arange 生成等差数列

'''
start:可忽略不写，默认从0开始;起始值
stop:结束值；生成的元素不包括结束值
step:可忽略不写，默认步长为1；步长
dtype:默认为None，设置显示元素的数据类型
'''

import numpy as np
nd1 = np.arange(5)#array([0, 1, 2, 3, 4])
nd2 = np.arange(1,5)#array([1, 2, 3, 4])
nd3 = np.arange(1,5,2)#nd3 = np.arange(1,5,2)
print(nd1, nd2, nd3)


nd4 = nd2.reshape(2,2)#array([[1, 2], [3, 4]])
print(nd4)

# 注意：对数组重塑后的元素个数不能大于原来本身的元素个数，不然会报错
# 比如说，nd2生成了四个元素，你要重塑（2,3）就是六个元素，会报错的


