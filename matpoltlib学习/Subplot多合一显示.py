import matplotlib.pyplot as plt

plt.figure()
# ����Сͼ��������ͼ�񴰿ڷ�Ϊ2��2��,��ǰλ��Ϊ1
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

# ����Сͼ��������ͼ�񴰿ڷ�Ϊ2��2��,��ǰλ��Ϊ2
plt.subplot(2,2,2)
plt.plot([0,1],[0,1])

# ����Сͼ��������ͼ�񴰿ڷ�Ϊ2��2��,��ǰλ��Ϊ3
plt.subplot(2,2,3)
plt.plot([0,1],[0,1])

# ����Сͼ��������ͼ�񴰿ڷ�Ϊ2��2��,��ǰλ��Ϊ4
plt.subplot(2,2,4)
plt.plot([0,1],[0,1])
plt.show()