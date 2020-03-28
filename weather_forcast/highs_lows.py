# 1.分析文件头
import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)     # 创建一个与该文件相关联的阅读器（reader）对象
#     header_row = next(reader)  # 返回文件下一行（第一行）
#     print(header_row)


# 2.打印文件头及其位置
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)        # 创建一个与该文件相关联的阅读器（reader）对象
#     header_row = next(reader)     # 返回文件下一行（第一行）
#
#     for index, column_header in enumerate(header_row):    # enumerate()用来获取元素的索引及其值
#         print(index, column_header)


# 3.提取并读取数据
# import csv
#
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)       # 创建一个与该文件相关联的阅读器对象（reader）
#     herder_row = next(reader)    # 返回文件的下一行（第一行）
#
#     highs = []
#     for row in reader:           # 从第二行开始循环
#         # 每次循环，都将索引1(第2列)的值附加到highs的末尾
#         high = int(row[1])       # 将表示气温的字符串转化为数字
#         highs.append(high)       # 将high附加到列表末尾
#     print(highs)


# 4.绘制气温图表
# import csv
# import matplotlib.pyplot as plt
# filename = 'sitka_weather_07-2014.csv'
#
# # 从文件中获取最高气温
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     highs = []
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# l1, = plt.plot(highs, c='red')
# plt.legend(handles=[l1, ], labels=['Highest Temperature'], loc='best')   # 使用legend()设置图例
# # 设置图形的格式
# plt.title("Daily high temperatures, July 2014", fontsize=24)
# plt.xlabel("", fontsize=16)
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()


# 5.模块datetime
# from datetime import datetime
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)


# 6.在图表中添加日期
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_07-2014.csv'
# # 从文件中获取日期和最高气温
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs = [], []
#     for row in reader:
#         # 从文件中获取日期
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         # 从文件中获取最高气温
#         high = int(row[1])
#         highs.append(high)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# l1, = plt.plot(dates, highs, c='red')
# plt.legend(handles=[l1, ], labels=['Highest Temperature'], loc='best')
#
# # 设置图形的格式
# plt.title("Daily high temperatures, July 2014", fontsize=24 )
# plt.xlabel("", fontsize=16)
# fig.autofmt_xdate()    # 绘制斜的日期标签
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()


# 7.涵盖更长的时间
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_2014.csv'
# # 从文件中获取日期和最高气温
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs = [], []
#     for row in reader:
#         # 从文件中获取日期
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#         # 从文件中获取最高气温
#         high = int(row[1])
#         highs.append(high)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# l1, = plt.plot(dates, highs, c='red')
# plt.legend(handles=[l1, ], labels=['Highest Temperature'], loc='best')
#
# # 设置图形格式
# plt.title("Daily high temperatures - 2014", fontsize=24)
# plt.xlabel("", fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()


# 8.再绘制一个数据系列
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# filename = 'sitka_weather_2014.csv'
# # 从文件中获取日期、最高气温和最低气温
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs, lows = [], [], []
#     for row in reader:
#         # 从文件中获取日期
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#
#         # 从文件中获取最高气温
#         high = int(row[1])
#         highs.append(high)
#
#         # 从文件中获取最低气温
#         low = int(row[3])
#         lows.append(low)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# l1, = plt.plot(dates, highs, c='red')
# l2, = plt.plot(dates, lows, c='blue')
# plt.legend(handles=[l1,l2,], labels=['Highest Temperature', 'Lowest Temperature'], loc='best')
#
# # 设置图形格式
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
# plt.xlabel("", fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()


# 9.给图表区域着色
# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt
#
# filename = 'sitka_weather_2014.csv'
# # 从文件中获取日期、最高气温和最低气温
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs, lows = [], [], []
#     for row in reader:
#         # 从文件中获取日期
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#
#         # 从文件中获取最高气温
#         high = int(row[1])
#         highs.append(high)
#
#         # 从文件中获取最低气温
#         low = int(row[3])
#         lows.append(low)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# l1, = plt.plot(dates, highs, c='red', alpha=0.5)  # alpha属性设置颜色的透明度，0为完全透明，1为完全不透明
# l2, = plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # facecolor属性设置填充的颜色
# plt.legend(handles=[l1, l2, ], labels=['Highest Temperature', 'Lowest Temperature'], loc='best')  # 设置图像的图例
#
# # 设置图形的格式
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
# plt.xlabel("", fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()


# 错误检查
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        # 从文件中获取日期、最高气温、最低气温
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
l1, = plt.plot(dates, highs, c='red', alpha=0.5)
l2, = plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.legend(handles=[l1, l2, ], labels=['Highest Temperature', 'Lowest Temperature'], loc='best')

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()