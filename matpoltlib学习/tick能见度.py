import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, zorder=1)  # zorder属性表示控制绘图顺序，先画线
# 设置y轴范围
plt.ylim(-2,2)

# 获取轴
ax=plt.gca()
# 选中right脊梁，将颜色设置为空
ax.spines['right'].set_color('none')
# 选中top脊梁，将颜色设置为空
ax.spines['top'].set_color('none')

# 指定x轴为bottom脊梁
ax.xaxis.set_ticks_position('bottom')
# 指定y轴为left脊梁
ax.yaxis.set_ticks_position('left')

# 选中bottom脊梁，移动到y值对应0
ax.spines['bottom'].set_position(('data', 0))
# 选中left脊梁，移动到x值对应0
ax.spines['left'].set_position(('data', 0))

# 绘制角标标签
for label in ax.get_xticklabels()+ax.get_yticklabels():  # 遍历x轴和y轴所有的角标标签
    label.set_zorder(2)  # zorder控制绘图顺序，再画角标标签
    label.set_fontsize(12)
    # set_bbox()设置角标标签的样式，facecolor填充颜色，edgecolor边框，alpha透明度
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7)) 
    
plt.show()