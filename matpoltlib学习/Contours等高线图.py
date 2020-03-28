import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # ����߶�ֵ
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# �����������ֵnp.meshgrid()
X,Y=np.meshgrid(x,y)

# ʹ��plt.contourf()�Ѷ�Ӧ��ɫ�ŵ��ȸ�����
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

# ʹ��plt.contour()���Ƶȸ��ߣ���Ϊ8+2����
C = plt.contour(X,Y,f(X,Y),8,colors='black')

# �ڵȸ�������ӱ�ǩ
plt.clabel(C,inline=True,fontsize=10)

# ����x���y��Ǳ�
plt.xticks(())
plt.yticks(())
plt.show()