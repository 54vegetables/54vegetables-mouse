import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, zorder=1)  # zorder���Ա�ʾ���ƻ�ͼ˳���Ȼ���
# ����y�᷶Χ
plt.ylim(-2,2)

# ��ȡ��
ax=plt.gca()
# ѡ��right����������ɫ����Ϊ��
ax.spines['right'].set_color('none')
# ѡ��top����������ɫ����Ϊ��
ax.spines['top'].set_color('none')

# ָ��x��Ϊbottom����
ax.xaxis.set_ticks_position('bottom')
# ָ��y��Ϊleft����
ax.yaxis.set_ticks_position('left')

# ѡ��bottom�������ƶ���yֵ��Ӧ0
ax.spines['bottom'].set_position(('data', 0))
# ѡ��left�������ƶ���xֵ��Ӧ0
ax.spines['left'].set_position(('data', 0))

# ���ƽǱ��ǩ
for label in ax.get_xticklabels()+ax.get_yticklabels():  # ����x���y�����еĽǱ��ǩ
    label.set_zorder(2)  # zorder���ƻ�ͼ˳���ٻ��Ǳ��ǩ
    label.set_fontsize(12)
    # set_bbox()���ýǱ��ǩ����ʽ��facecolor�����ɫ��edgecolor�߿�alpha͸����
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7)) 
    
plt.show()