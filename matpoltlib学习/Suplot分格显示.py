# ����һ
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
# ������һ��Сͼ��(3,3)��ʾ������ͼ�񴰿ڷֳ�3��3��
# (0,0)��ʾ�ӵ�0�е�0�п�ʼ��ͼ
# colspan=3��ʾ�еĿ��Ϊ3, rowspan=1��ʾ�еĿ��Ϊ1. colspan��rowspanȱʡ, Ĭ�Ͽ��Ϊ1.
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')

# ʹ��plt.subplot2grid��������2��Сͼ, (3,3)��ʾ������ͼ�񴰿ڷֳ�3��3��, 
# (1,0)��ʾ�ӵ�1�е�0�п�ʼ��ͼ
# colspan=3��ʾ�еĿ��Ϊ2,rowspanȱʡ, Ĭ�Ͽ��Ϊ1
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)

# ʹ��plt.subplot2grid��������3��Сͼ, (3,3)��ʾ������ͼ�񴰿ڷֳ�3��3��, 
# (1,2)��ʾ�ӵ�1�е�2�п�ʼ��ͼ
# colspan=3��ʾ�еĿ��Ϊ1,rowspan�еĿ��Ϊ2
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)

# ʹ��plt.subplot2grid��������4��Сͼ, (3,3)��ʾ������ͼ�񴰿ڷֳ�3��3��, 
# (1,2)��ʾ�ӵ�2�е�0�п�ʼ��ͼ
ax4 = plt.subplot2grid((3,3),(2,0))

# ʹ��plt.subplot2grid��������5��Сͼ, (3,3)��ʾ������ͼ�񴰿ڷֳ�3��3��, 
# (1,2)��ʾ�ӵ�2�е�1�п�ʼ��ͼ
ax5 = plt.subplot2grid((3,3),(2,1))

plt.tight_layout()  # plt.tight_layout()��ʾ������ʾͼ��
plt.show()

# ������
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
# ʹ��gridspec.GridSpec������ͼ�񴰿ڷֳ�3��3��
gs = gridspec.GridSpec(3,3)

# gs[0, :]��ʾ���ͼռ��0�к�������
ax1 = plt.subplot(gs[0,:])
# gs[1, :2]��ʾ���ͼռ��1�к͵�2��ǰ��������
ax2 = plt.subplot(gs[1,:2])
# gs[1:, 2]��ʾ���ͼռ��1�к�������к͵�2��
ax3 = plt.subplot(gs[1:,2])
# gs[-1, 0]��ʾ���ͼռ������1�к͵�0��
ax4 = plt.subplot(gs[-1,0])
# gs[-1, -2]��ʾ���ͼռ������1�к͵�����2��
ax5 = plt.subplot(gs[-1,-2])

plt.tight_layout()  # plt.tight_layout()��ʾ������ʾͼ��
plt.show()

# ������
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ʹ��plt.subplots����һ��2��2�е�ͼ�񴰿�
# sharex=True��ʾ����x������, sharey=True��ʾ����y�����ꡣ
# ((ax11, ax12), (ax13, ax14))��ʾ��1�д����������η�ax11��ax12, ��2�д����������η�ax21��ax22
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
plt.tight_layout()   # plt.tight_layout()��ʾ������ʾͼ��
plt.show()