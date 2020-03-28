# 方法一
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
# 创建第一个小图，(3,3)表示将整个图像窗口分成3行3列
# (0,0)表示从第0行第0列开始作图
# colspan=3表示列的跨度为3, rowspan=1表示行的跨度为1. colspan和rowspan缺省, 默认跨度为1.
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')

# 使用plt.subplot2grid来创建第2个小图, (3,3)表示将整个图像窗口分成3行3列, 
# (1,0)表示从第1行第0列开始作图
# colspan=3表示列的跨度为2,rowspan缺省, 默认跨度为1
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)

# 使用plt.subplot2grid来创建第3个小图, (3,3)表示将整个图像窗口分成3行3列, 
# (1,2)表示从第1行第2列开始作图
# colspan=3表示列的跨度为1,rowspan行的跨度为2
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)

# 使用plt.subplot2grid来创建第4个小图, (3,3)表示将整个图像窗口分成3行3列, 
# (1,2)表示从第2行第0列开始作图
ax4 = plt.subplot2grid((3,3),(2,0))

# 使用plt.subplot2grid来创建第5个小图, (3,3)表示将整个图像窗口分成3行3列, 
# (1,2)表示从第2行第1列开始作图
ax5 = plt.subplot2grid((3,3),(2,1))

plt.tight_layout()  # plt.tight_layout()表示紧凑显示图像
plt.show()

# 方法二
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
# 使用gridspec.GridSpec将整个图像窗口分成3行3列
gs = gridspec.GridSpec(3,3)

# gs[0, :]表示这个图占第0行和所有列
ax1 = plt.subplot(gs[0,:])
# gs[1, :2]表示这个图占第1行和第2列前的所有列
ax2 = plt.subplot(gs[1,:2])
# gs[1:, 2]表示这个图占第1行后的所有行和第2列
ax3 = plt.subplot(gs[1:,2])
# gs[-1, 0]表示这个图占倒数第1行和第0列
ax4 = plt.subplot(gs[-1,0])
# gs[-1, -2]表示这个图占倒数第1行和倒数第2列
ax5 = plt.subplot(gs[-1,-2])

plt.tight_layout()  # plt.tight_layout()表示紧凑显示图像
plt.show()

# 方法三
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 使用plt.subplots建立一个2行2列的图像窗口
# sharex=True表示共享x轴坐标, sharey=True表示共享y轴坐标。
# ((ax11, ax12), (ax13, ax14))表示第1行从左至右依次放ax11和ax12, 第2行从左至右依次放ax21和ax22
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
plt.tight_layout()   # plt.tight_layout()表示紧凑显示图像
plt.show()