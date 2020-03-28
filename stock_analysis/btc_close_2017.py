# 1.提取相关数据
# import json
#
# # 将数据加入到一个列表中
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# # 遍历btc_data打印每一天的信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = btc_dict['month']
#     week = btc_dict['week']
#     weekday = btc_dict['weekday']
#     close = btc_dict['close']
#     print("{} is month {} week {}, {}, the close price is {} RMB.".format(date, month, week, weekday, close))


# 2.将字符串转换为数字值
# import json
#
# # 将数据加入到一个列表中
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# # 遍历btc_data打印每一天的信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     close = int(eval(btc_dict['close']))  # 或close = int(float(btc_dict['close']))
#     print("{} is month {} week {}, {}, the close price is {} RMB.".format(date, month, week, weekday, close))


# 3.绘制收盘价折线图
# import json
# import pygal
#
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# dates, months, weeks, weekdays, closes = [], [], [], [], []
# # 每一天的信息
# for btc_dict in btc_data:
#     try:
#         date = btc_dict['date']
#         month = int(btc_dict['month'])
#         week = int(btc_dict['week'])
#         weekday = btc_dict['weekday']
#         close = int(float(btc_dict['close']))
#     except ValueError:
#         print(date, "is missing.")
#     else:
#         dates.append(date)
#         months.append(month)
#         weeks.append(week)
#         weekdays.append(weekday)
#         closes.append(close)
#
# # 将数据进行可视化
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价(￥)'
# line_chart.x_labels = dates
# N = 20
# line_chart.x_labels_major = dates[::N]
# line_chart.add('收盘价', closes)
# line_chart.render_to_file('收盘价折线图(￥).svg')


# 4.时间序列特征初探
# import json
# import pygal
# import math
#
# filename = 'btc_close_2017.json'
# with open(filename) as f:
#     btc_data = json.load(f)
#
# dates, months, weeks, weekdays, closes = [], [], [], [], []
# # 每一天的信息
# for btc_dict in btc_data:
#     try:
#         date = btc_dict['date']
#         month = int(btc_dict['month'])
#         week = int(btc_dict['week'])
#         weekday = btc_dict['weekday']
#         close = int(float(btc_dict['close']))
#     except ValueError:
#         print('{}is missing.'.format(date))
#     else:
#         dates.append(date)
#         months.append(month)
#         weeks.append(week)
#         weekdays.append(weekday)
#         closes.append(close)
#
# # 将数据进行可视化
# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = "收盘价对数变换（￥）"
# line_chart.x_labels = dates
# N = 20
# line_chart._x_labels_major = dates[::N]
# close_log = [math.log10(x) for x in closes]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')


# 5.zip()和groupby()的作用
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9, 10]
# zipped_1 = zip(a, b)      # 合并成(1,4)(2,5)(3,6)
# zipped_2 = zip(a, b, c)   # 合并成(1,4,7)(2,5,8)(3,6,9)舍去10
#
# print(zipped_1)         # 无法直接打印
# print(list(zipped_1))   # list函数以一个元组为参数转化为列表
# print(*zipped_1)          # 打印元组(1,4)(2,5)(3,6)
#
# print(zipped_2)
# print(list(zipped_2))
# print(*zipped_2)
# # 将解压后的zipped_2提取出来
# x, y, z = [*zipped_2]
# print(x)
# print(y)
# print(z)


# from itertools import groupby
# print('groupby的结果')
# test = [(1, 5), (1, 4), (1, 3), (1, 2), (2, 4), (2, 3), (3, 5)]
# # 将元组排序，按打头的元素一致分到一组
# temp = groupby(sorted(test), key=lambda x: x[0])
# print('list处理之前打印temp')
# print(temp)                  # 无法直接打印
# print('list处理的temp')
# print(list(temp))          # 只能打印第一个元素，无法直接打印第二个元素
#
# for a, b in temp:
#     print(list(b))


# 6.收盘价均值
import json
import pygal
from itertools import groupby

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates, months, weeks, weekdays, closes = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))


def draw_line(x_data, y_data, title, y_legend):
    # x轴  y轴  生成文件的名称  y_legend='月日均值'，线的名称
    xy_map = []
    # 一个空列表，以后里面装的元素也是列表
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        # zip:将x轴和y轴合并，对应组成元素，如：
        # x_data = [1, 1, 2, 2]
        # y_data = [3, 2, 4, 6]
        # zip(x_data, y_data)=[(1, 3), (1, 2), (2, 4), (2, 6)]  x轴和y轴数据纵向合并
        # 排序：sorted(zip(x_data, y_data))=[(1, 2), (1, 3), (2, 4), (2, 6)]
        # groupby:分组
        # key=lambda _:_[0]  分组按索引0位的元素分组，得到一个字典
        # 如：{1:[(1, 2), (1, 3)], 2:[(2, 4), (2, 6)]}
        # for循环：x就是字典中的key值，也就是分组的依据，x=1,x=2
        # y就是字典中的value值，也就是元组组成的列表

        y_list = [v for _, v in y]
        # y里面的元素是元组(1, 2), (1, 3)，不要1，取出2,3
        # 对于y列表里面的元素，_对应1（分组的依据），v对应2,3，把v取出来

        xy_map.append([x, sum(y_list) / len(y_list)])
        # 每一对值作为一个列表，放到xy_map中
        # xy_map = [[1, 2.5], [2, 5]]

    x_unique, y_mean = [*zip(*xy_map)]
    # *解包，提取出两个列表：
    # *xy_map = [1, 2.5], [2, 5]
    # zip再进行纵向压缩：zip(*xy_map)=[(1, 2), (2, 2.5)]
    # *zip再解包：*zip(*xy_map)=(1, 2), (2, 2.5)
    # 用两个值把这两个列表提取出来
    # x_unique = (1, 2)   y_mean = (2, 2.5)

    # 对数据进行可视化
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + ".svg")
    return line_chart


# 调用函数，求月均值
# 由于2017年12月的数据不完整，所以只取一月到十一月的数据
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值（￥）', '月日均值')
line_chart_month

# 调用函数，求周均值
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值（￥）', '周日均值')
line_chart_week

# 调用函数，求星期均值
idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekday_int, closes[1:idx_week], '收盘价星期均值（￥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')

# 收盘价数据仪表盘
with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图(￥).svg', '收盘价对数变换折线图（￥）.svg', '收盘价月日均值（￥）.svg',
        '收盘价周日均值（￥）.svg', '收盘价星期均值（￥）.svg'
    ]:
        html_file.write('        <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')
