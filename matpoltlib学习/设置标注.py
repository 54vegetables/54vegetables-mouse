import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

# ��ȡ��
ax = plt.gca()
# ѡ��right����������ɫ����Ϊ��
ax.spines['right'].set_color('none')
# ѡ��top����������ɫ����Ϊ��
ax.spines['top'].set_color('none')

# ָ��x��Ϊbottom����
ax.xaxis.set_ticks_position('bottom')
# ָ��y��Ϊleft����
ax.yaxis.set_ticks_position('left')

# ѡ��bottom�������ƶ���y��Ӧ��ֵΪ0
ax.spines['bottom'].set_position(('data', 0))
# ѡ��left�������ƶ���x��Ӧ��ֵΪ0
ax.spines['left'].set_position(('data', 0))

# ���Ƶ�
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='blue')  # ���СΪ50���أ���ɫΪ��ɫ
# ���Ƶ㵽x�������
plt.plot([x0, x0], [y0, 0], 'k--', linewidth=2.5)  # k--����Ϊ���ú�ɫ����

# method1
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0, y0), xycoords='data',  #��xy�������Ϊ��׼��
             # xytext��ʾ��ע��λ�ã�������꣩,textcoords���Ա�ʾ��עλ�û��ڵ�
             xytext=(+30, -30), textcoords='offset points',
             # arrowprops������ arrowstyle='->'����ͷ���ߣ�arrowprops���û��ȵķ��
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# method2
# -3.7,3��ʾ��ע��ʼ�����꣬fontdict�йر�ע���������
plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
        fontdict={'size':16, 'color':'red'})
plt.show()