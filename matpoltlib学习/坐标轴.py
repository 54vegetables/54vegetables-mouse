import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置x轴和y轴范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# 设置x轴和y轴标签
plt.xlabel('I am x')
plt.ylabel('I am y')

# 更改x轴和y轴角标
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], 
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# gca获取当前轴
ax = plt.gca()
# 将右侧和上部的脊梁隐藏
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 指定x轴为bottom脊梁，y轴为left脊梁
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 选中bottom脊梁，移动bottom脊梁使y对应的值为-1
ax.spines['bottom'].set_position(('data', -1))
# 选中left脊梁，移动left脊梁使x对应的值为0
ax.spines['left'].set_position(('data', 0))

plt.show()