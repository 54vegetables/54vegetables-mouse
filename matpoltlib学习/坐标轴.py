import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# ����x���y�᷶Χ
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# ����x���y���ǩ
plt.xlabel('I am x')
plt.ylabel('I am y')

# ����x���y��Ǳ�
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], 
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# gca��ȡ��ǰ��
ax = plt.gca()
# ���Ҳ���ϲ��ļ�������
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# ָ��x��Ϊbottom������y��Ϊleft����
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# ѡ��bottom�������ƶ�bottom����ʹy��Ӧ��ֵΪ-1
ax.spines['bottom'].set_position(('data', -1))
# ѡ��left�������ƶ�left����ʹx��Ӧ��ֵΪ0
ax.spines['left'].set_position(('data', 0))

plt.show()