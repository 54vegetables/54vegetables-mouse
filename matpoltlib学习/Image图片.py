import matplotlib.pyplot as plt
import numpy as np

# 图像数据
# np.array()创建多维数组
# reshape()函数将数组转化维度
a = np.array([0.313660827978,0.365348418405,0.423733120134,
             0.365348418405,0.439599930624,0.525083754405,
             0.423733120134,0.525083754405,0.651536351379]).reshape(3,3)

# interpolation插入图像数据的方式，origin表示选择的原点位置
plt.imshow(a,interpolation='nearest',cmap=plt.cm.bone,origin='lower')
plt.colorbar(shrink=0.9)  # shrink压缩高度

plt.xticks(())
plt.yticks(())
plt.show()