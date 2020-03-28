# ����һ
import matplotlib.pyplot as plt
import numpy as np

n=1024
# np.random.normal()����˼��һ����̬�ֲ�
# numpy.random.normal(loc=0,scale=1e-2,size=shape)
# ����loc(float)����̬�ֲ��ľ�ֵ����Ӧ������ֲ������ġ�loc=0˵����һ����Y��Ϊ�Գ������̬�ֲ�
# ����scale(float)����̬�ֲ��ı�׼���Ӧ�ֲ��Ŀ�ȣ�scaleԽ����̬�ֲ�������Խ���֣�scaleԽС������Խ���ݡ�
# ����size(int ��������Ԫ��)�������ֵ����shape�Ĭ��ΪNone
X=np.random.normal(loc=0,scale=1,size=n)  
Y=np.random.normal(loc=0,scale=1,size=n)
T=np.arctan2(Y,X) # arctan2���ظ�����X��Yֵ�ķ�����ֵ

plt.figure(num=1,figsize=(8, 5))
plt.scatter(X,Y,s=75,c=T,marker='+',alpha=0.5) # marker='+'���õ�ĵ���״Ϊ�Ӻ�

# ����x���y�᷶Χ
plt.xlim((-3,3))
plt.ylim((-3,3))

# ��x���y��ĽǱ�����Ϊ��
plt.xticks(())
plt.yticks(())
plt.show()

# ������
import matplotlib.pyplot as plt
import numpy as np

n=1024
X=np.random.normal(0,2,n)
Y=np.random.normal(0,2,n)
T=np.arctan2(Y,X) # ������ɫ

plt.figure(num=1,figsize=(8, 5))
plt.scatter(np.arange(5),np.arange(5))

plt.xticks(())
plt.yticks(())
plt.show()