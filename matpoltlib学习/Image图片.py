import matplotlib.pyplot as plt
import numpy as np

# ͼ������
# np.array()������ά����
# reshape()����������ת��ά��
a = np.array([0.313660827978,0.365348418405,0.423733120134,
             0.365348418405,0.439599930624,0.525083754405,
             0.423733120134,0.525083754405,0.651536351379]).reshape(3,3)

# interpolation����ͼ�����ݵķ�ʽ��origin��ʾѡ���ԭ��λ��
plt.imshow(a,interpolation='nearest',cmap=plt.cm.bone,origin='lower')
plt.colorbar(shrink=0.9)  # shrinkѹ���߶�

plt.xticks(())
plt.yticks(())
plt.show()