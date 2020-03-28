import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)  #在窗口上添加3D坐标轴

# X和Y的值
X = np.arange(-4,4,0.25) # 创建一个数组的取值范围为[-4,4]，间隔为0.25像素
Y = np.arange(-4,4,0.25)
# 将X和Y值编织成栅格
X,Y = np.meshgrid(X,Y)  
R = np.sqrt(X ** 2 + Y ** 2)

# 高度值
Z = np.sin(R)

# 绘制3D图像plot_surface()
# rstride:行之间的跨度  cstride:列之间的跨度
# rcount:设置间隔个数，默认50个，ccount:列的间隔个数，不能与上面两个参数同时出现

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')

# 绘制从3D曲面到底部的投影(等高线图contourf())
# zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')  # zdir = 'z', offset = -2 表示投影到z = -2上
# 设置z轴的范围，x,y类似
ax.set_zlim(-2,2)
plt.show()