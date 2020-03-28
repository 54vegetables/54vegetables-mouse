import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # 计算高度值
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# 绑定网格的输入值np.meshgrid()
X,Y=np.meshgrid(x,y)

# 使用plt.contourf()把对应颜色放到等高线中
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

# 使用plt.contour()绘制等高线，分为8+2部分
C = plt.contour(X,Y,f(X,Y),8,colors='black')

# 在等高线中添加标签
plt.clabel(C,inline=True,fontsize=10)

# 隐藏x轴和y轴角标
plt.xticks(())
plt.yticks(())
plt.show()