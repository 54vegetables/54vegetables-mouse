import matplotlib.pyplot as plt
import numpy as np

n=12  # 12����״ͼ
X=np.arange(n) # ��0��11������
# ��������, ���ȷֲ�(0.5, 1.0)֮��
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

# ������״ͼ, ����
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
# ������״ͼ, ����
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    # plt.text()�����֡�
    # x+0.05,y+0.05����0.05������0.05��
    # '%.2f'%y ����Y1��ֵ   
    # ha:�������ķ�ʽ,va:������뷽ʽ
    plt.text(x+0.05,y+0.05,'%.2f'%y,ha='center',va='bottom')
    
for x,y in zip(X,Y2):
    # plt.text()������
    # ha:�������ķ�ʽ,va:������뷽ʽ
    plt.text(x+0.05,-y-0.05,'-%.2f'%y,ha='center',va='top')

# ���������᷶Χ
plt.xlim(-1,n)
plt.ylim(-1.25,1.25)
# ȥ��������̶�
plt.xticks(())
plt.yticks(())
plt.show()