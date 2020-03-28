import matplotlib.pyplot as plt
import numpy as np

# 创建一个数组的取值范围[0,10]，间隔0.1像素
x = np.arange(0,10,0.1)
y1 = 0.05 * x**2
y2 = -1*y1
# 获取figure默认的坐标系 ax1
fig,ax1 = plt.subplots()

# 对ax1调用twinx()方法，生成如同镜面效果后的ax2
ax2 = ax1.twinx()
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax2.set_ylabel('Y2',color='b')

plt.show()