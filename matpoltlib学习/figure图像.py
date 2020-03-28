import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)  # x轴坐标由-3到3绘制50个点
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y1)

plt.figure(num = 3, figsize=(8, 5))                            # num=3表示为figure3,figsize设置图像的长和宽
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=10, linestyle='--')    # linestyle='--'设置线为虚线

plt.show()