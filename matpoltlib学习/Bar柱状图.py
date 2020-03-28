import matplotlib.pyplot as plt
import numpy as np

n=12  # 12个柱状图
X=np.arange(n) # 从0到11的数字
# 生成数据, 均匀分布(0.5, 1.0)之间
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

# 绘制柱状图, 向上
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
# 绘制柱状图, 向下
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    # plt.text()加文字。
    # x+0.05,y+0.05左移0.05，上移0.05。
    # '%.2f'%y 传入Y1的值   
    # ha:横向对齐的方式,va:纵向对齐方式
    plt.text(x+0.05,y+0.05,'%.2f'%y,ha='center',va='bottom')
    
for x,y in zip(X,Y2):
    # plt.text()加文字
    # ha:横向对齐的方式,va:纵向对齐方式
    plt.text(x+0.05,-y-0.05,'-%.2f'%y,ha='center',va='top')

# 设置坐标轴范围
plt.xlim(-1,n)
plt.ylim(-1.25,1.25)
# 去掉坐标轴刻度
plt.xticks(())
plt.yticks(())
plt.show()