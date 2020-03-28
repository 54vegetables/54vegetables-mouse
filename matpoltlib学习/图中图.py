import matplotlib.pyplot as plt

fig = plt.figure()
# 创建数据
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

# 大图
# 确定大图左下角的位置以及宽高，4个值都是占整个figure坐标系的百分比
# 在这里，假设figure的大小是10x10，那么大图就被包含在由(1, 1)开始，宽8，高8的坐标系内
left,bottom,width,height = 0.1,0.1,0.8,0.8
# 将大图坐标系添加到figure中
ax1 = fig.add_axes([left,bottom,width,height])
# 绘制大图，颜色为红色
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

# 小图
# 确定小图左下角的位置以及宽高，4个值都是占整个figure坐标系的百分比
# 在这里，假设figure的大小是10x10，那么小图就被包含在由(1, 1)开始，宽8，高8的坐标系内
left,bottom,width,height = 0.2,0.6,0.25,0.25
# 将小图坐标系添加到figure中
ax2 = fig.add_axes([left,bottom,width,height])
# 绘制小图，颜色为蓝色
ax2.plot(y,x,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# 小图
# 将小图坐标系添加到figure中
plt.axes([.6,0.2,0.25,0.25])

plt.plot(y[::-1],x,'g')   # 注意对y进行了逆序处理
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')
plt.show()