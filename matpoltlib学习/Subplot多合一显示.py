import matplotlib.pyplot as plt

plt.figure()
# 绘制小图，将整个图像窗口分为2行2列,当前位置为1
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

# 绘制小图，将整个图像窗口分为2行2列,当前位置为2
plt.subplot(2,2,2)
plt.plot([0,1],[0,1])

# 绘制小图，将整个图像窗口分为2行2列,当前位置为3
plt.subplot(2,2,3)
plt.plot([0,1],[0,1])

# 绘制小图，将整个图像窗口分为2行2列,当前位置为4
plt.subplot(2,2,4)
plt.plot([0,1],[0,1])
plt.show()