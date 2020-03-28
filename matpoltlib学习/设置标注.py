import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

# 获取轴
ax = plt.gca()
# 选中right脊梁，将颜色设置为空
ax.spines['right'].set_color('none')
# 选中top脊梁，将颜色设置为空
ax.spines['top'].set_color('none')

# 指定x轴为bottom脊梁
ax.xaxis.set_ticks_position('bottom')
# 指定y轴为left脊梁
ax.yaxis.set_ticks_position('left')

# 选中bottom脊梁，移动到y对应的值为0
ax.spines['bottom'].set_position(('data', 0))
# 选中left脊梁，移动到x对应的值为0
ax.spines['left'].set_position(('data', 0))

# 绘制点
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='blue')  # 点大小为50像素，颜色为蓝色
# 绘制点到x轴的虚线
plt.plot([x0, x0], [y0, 0], 'k--', linewidth=2.5)  # k--属性为设置黑色虚线

# method1
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0, y0), xycoords='data',  #将xy这个点作为基准点
             # xytext表示标注的位置（相对坐标）,textcoords属性表示标注位置基于点
             xytext=(+30, -30), textcoords='offset points',
             # arrowprops方向线 arrowstyle='->'带箭头的线，arrowprops设置弧度的风格
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# method2
# -3.7,3表示标注开始的坐标，fontdict有关标注字体的设置
plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
        fontdict={'size':16, 'color':'red'})
plt.show()