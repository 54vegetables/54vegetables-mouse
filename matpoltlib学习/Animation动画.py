%matplotlib notebook
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()
# 数据是一个0~2π内的正弦曲线
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    # 构造自定义动画函数animate，用来更新每一帧上各个x对应的y坐标值，参数表示第i帧
    line.set_ydata(np.sin(x + i/10.0))
    return line,

# 构造开始帧函数init
def init():
    line.set_ydata(np.sin(x))
    return line,

# 调用FuncAnimation函数生成动画
# fig 进行动画绘制的figure
# func 自定义动画函数，即传入刚定义的函数animate
# frames 动画长度，一次循环包含的帧数
# init_func 自定义开始帧，即传入刚定义的函数init
# interval 更新频率，以ms计
# blit 选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显示动画
ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=False)

plt.show()