import matplotlib.pyplot as plt

fig = plt.figure()
# ��������
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

# ��ͼ
# ȷ����ͼ���½ǵ�λ���Լ���ߣ�4��ֵ����ռ����figure����ϵ�İٷֱ�
# ���������figure�Ĵ�С��10x10����ô��ͼ�ͱ���������(1, 1)��ʼ����8����8������ϵ��
left,bottom,width,height = 0.1,0.1,0.8,0.8
# ����ͼ����ϵ��ӵ�figure��
ax1 = fig.add_axes([left,bottom,width,height])
# ���ƴ�ͼ����ɫΪ��ɫ
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

# Сͼ
# ȷ��Сͼ���½ǵ�λ���Լ���ߣ�4��ֵ����ռ����figure����ϵ�İٷֱ�
# ���������figure�Ĵ�С��10x10����ôСͼ�ͱ���������(1, 1)��ʼ����8����8������ϵ��
left,bottom,width,height = 0.2,0.6,0.25,0.25
# ��Сͼ����ϵ��ӵ�figure��
ax2 = fig.add_axes([left,bottom,width,height])
# ����Сͼ����ɫΪ��ɫ
ax2.plot(y,x,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# Сͼ
# ��Сͼ����ϵ��ӵ�figure��
plt.axes([.6,0.2,0.25,0.25])

plt.plot(y[::-1],x,'g')   # ע���y������������
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')
plt.show()