%matplotlib notebook
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()
# ������һ��0~2���ڵ���������
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    # �����Զ��嶯������animate����������ÿһ֡�ϸ���x��Ӧ��y����ֵ��������ʾ��i֡
    line.set_ydata(np.sin(x + i/10.0))
    return line,

# ���쿪ʼ֡����init
def init():
    line.set_ydata(np.sin(x))
    return line,

# ����FuncAnimation�������ɶ���
# fig ���ж������Ƶ�figure
# func �Զ��嶯��������������ն���ĺ���animate
# frames �������ȣ�һ��ѭ��������֡��
# init_func �Զ��忪ʼ֡��������ն���ĺ���init
# interval ����Ƶ�ʣ���ms��
# blit ѡ��������е㣬���ǽ����²����仯�ĵ㡣Ӧѡ��True����mac�û���ѡ��False�������޷���ʾ����
ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=False)

plt.show()