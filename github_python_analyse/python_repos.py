# 1.处理API响应
# import requests
#
# # 执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code: ", r.status_code)  # 输出请求状态码
#
# # 将API响应存储到一个变量中
# response_dict = r.json()     # 使用方法json()方法将str转化为dict
#
# # 处理结果
# print(response_dict.keys())


# 2.处理响应字典
# import requests
#
# # 执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code: ", r.status_code)
#
# # 将API响应存储在一个变量中
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# # 探索有关仓库的信息
# repo_dicts = response_dict['items']                # repo_dicts列表中嵌套字典仓库
# print("Repositories returned:", len(repo_dicts))   # 输出items对应的列表中有几个字典仓库
#
# # 研究第一个仓库
# repo_dict = repo_dicts[0]                    # 列表中第一个元素---第一个字典仓库
# print('\nKeys:', len(repo_dict))             # 第一个仓库的长度
# for key in sorted(repo_dict.keys()):         # 对第一个仓库的键按从小到大排序
#     print(key)

# 下面来提取repo_dict中与一些键相关的值
# import requests
#
# # 执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)

# 将API响应存储在一个变量中
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# # 研究有关仓库的信息
# repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))
#
# # 研究第一个仓库
# repo_dict = repo_dicts[0]
#
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])


# 3.概述最受欢迎的仓库
# import requests
#
# # 执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# # 将API响应存储在一个变量中
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# # 研究有关仓库的信息
# repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))     # 仓库个数
#
# # 打印每个项目的名称、所有者、星级、在GitHub上的URL以及描述信息
# print("\n Selected information about each repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])


# 4.使用Pygal可视化仓库
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# #  执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
#
# # 将API响应存储到一个变量中
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# # 研究有关仓库的信息
# repo_dicts = response_dict['items']
#
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)     # 定义一种样式，将其基色设置为深蓝色，不交互时为浅蓝色
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)    # 创建条形图，样式为my_style,x轴对应刻度顺时针旋转45°，隐藏图例
# chart.title = 'Most-starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', stars)
# chart.render_to_file('python_repos_1.svg')


# 5.改进pygal图表
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# #  执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print('Status code:', r.status_code)
#
# # 将API响应存储到一个变量中
# response_dict = r.json()
# print('Total repositories:', response_dict['total_count'])
#
# # 研究有关仓库的信息
# repo_dicts = response_dict['items']
#
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)
#
# # 通过修改my_config的属性，制定图表的外观
# my_config = pygal.Config()
# my_config.x_label_rotation = 45  # x轴对应的文字顺时针旋转45°
# my_config.show_legend = False  # 隐藏图例
# my_config.truncate_label = 15  # 较长的项目名缩短为15个字符
# my_config.show_y_guides = False  # 隐藏图表中的水平线
# my_config.width = 1000  # 自定义宽度
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.config.style.title_font_size = 24  # 标题
# chart.config.style.label_font_size = 14  # 副标题：x轴上的项目名以及y轴上的大部分数字
# chart.config.style.major_label_font_size = 18  # 主标题：y轴上为5000整数倍的刻度
# chart.x_labels = names
# chart.title = 'Most-starred Python Projects on GitHub'
#
# chart.add('', stars)
# chart.render_to_file('python_repos_2.svg')


# 6.添加自定义工具提示
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
#
# chart.title = 'Python Projects'
# chart.x_labels = ['httpie', 'django', 'flask']
#
# plot_dicts = [
#     {'value': 16101, 'label': 'Description of httpie.'},
#     {'value': 15028, 'label': 'Description of django.'},
#     {'value': 14798, 'label': 'Description of flask.'},
#     ]
#
# chart.add('', plot_dicts)
# chart.render_to_file('bar_descriptions.svg')


# 7.根据数据绘图
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# #  执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print('Status code:', r.status_code)
#
# # 将API响应存储到一个变量中
# response_dict = r.json()
# print('Total repositories:', response_dict['total_count'])
#
# # 研究有关仓库的信息
# repo_dicts = response_dict['items']
#
# names, plot_dicts = [], []
#
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#
#     plot_dict = {
#         'value': repo_dict['stargazers_count'],
#         'label': str(repo_dict['description']),
#     }
#     plot_dicts.append(plot_dict)
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
# # 通过修改my_config的属性，制定图表的外观
# chart = pygal.Bar(my_config, style=my_style)
# chart.config.style.title_font_size = 24
# chart.config.style.label_font_size = 14
# chart.config.style.major_label_font_size = 18
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', plot_dicts)
# chart.render_to_file('python_repos_3.svg')


# 8.在图表中添加可单击的链接
# import requests
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#
# #  执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print('Status code:', r.status_code)
#
# # 将API响应存储到一个变量中
# response_dict = r.json()
# print('Total repositories:', response_dict['total_count'])
#
# # 研究有关仓库的信息
# repo_dicts = response_dict['items']
#
# names, plot_dicts = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     # 存储每个仓库的星级、描述和所在链接
#     plot_dict = {
#         'value': repo_dict['stargazers_count'],
#         'label': str(repo_dict['description']),
#         'xlink': repo_dict['html_url'],
#         }
#     # 将每个仓库的信息添加到列表末尾
#     plot_dicts.append(plot_dict)
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)
#
# # 通过修改my_config的属性，制定图表的外观
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.truncate = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.config.style.title_font_size = 24
# chart.config.style.label_font_size = 14
# chart.config.style.major_label_font_size = 18
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('', plot_dicts)
# chart.render_to_file('python_repos_4.svg')

# 9.Hacker News API
import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()  # 文章编号列表
submission_dicts = []
for submission_id in submission_ids[:10]:
    # 处理有关每篇文章的信息
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    # 存储每个文章的评论数量和所在链接
    plot_dict = {
        'value': submission_dict['comments'],
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate = 15
my_config.show_y_guides = False
my_config.width = 1600

chart = pygal.Bar(my_config, style=my_style)
chart.config.style.title_font_size = 24
chart.config.style.label_font_size = 14
chart.config.style.major_label_font_size = 18
chart.title = 'Most-hottest Projects on Hacker News'
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('hn_submissions.svg')
