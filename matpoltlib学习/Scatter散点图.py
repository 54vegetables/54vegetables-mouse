# 方法一
import matplotlib.pyplot as plt
import numpy as np

n=1024
# np.random.normal()的意思是一个正态分布
# numpy.random.normal(loc=0,scale=1e-2,size=shape)
# 参数loc(float)：正态分布的均值，对应着这个分布的中心。loc=0说明这一个以Y轴为对称轴的正态分布
# 参数scale(float)：正态分布的标准差，对应分布的宽度，scale越大，正态分布的曲线越矮胖，scale越小，曲线越高瘦。
# 参数size(int 或者整数元组)：输出的值赋在shape里，默认为None
X=np.random.normal(loc=0,scale=1,size=n)  
Y=np.random.normal(loc=0,scale=1,size=n)
T=np.arctan2(Y,X) # arctan2返回给定的X和Y值的反正切值

plt.figure(num=1,figsize=(8, 5))
plt.scatter(X,Y,s=75,c=T,marker='+',alpha=0.5) # marker='+'设置点的的形状为加号

# 设置x轴和y轴范围
plt.xlim((-3,3))
plt.ylim((-3,3))

# 将x轴和y轴的角标设置为空
plt.xticks(())
plt.yticks(())
plt.show()

# 方法二
import matplotlib.pyplot as plt
import numpy as np

n=1024
X=np.random.normal(0,2,n)
Y=np.random.normal(0,2,n)
T=np.arctan2(Y,X) # 字体颜色

plt.figure(num=1,figsize=(8, 5))
plt.scatter(np.arange(5),np.arange(5))

plt.xticks(())
plt.yticks(())
plt.show()