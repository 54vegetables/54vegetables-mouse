# 1.使用urlopen函数下载数据
# 导入模块
from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    # Python 2.x版本
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# Python向GitHub服务器发送请求，服务器响应请求后把文件发送给Python
request = urlopen(json_url)
# 读取数据
req = request.read()

# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)

# 加载数据
file_urllib = json.loads(req)
print(file_urllib)

# 2.使用requests模块下载数据
# import requests
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# # 将数据写入文件
# with open('btc_close_2017_request.json', 'w') as f:
#     f.write(req.text)
# # 加载数据
# file_request = req.json()
# print(file_request)
