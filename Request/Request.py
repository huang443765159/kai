import requests
import json


cs_url = 'https://zhuanlan.zhihu.com/p/33288426'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# HEADERS 可以在f12 network headers找到
data = {'some': 'data'}
r = requests.get(cs_url, headers=headers, data=json.dumps(data))
# print(r.content.decode('utf-8'))  # 不一定是json格式，所以需要用decode
a = r.content.decode()
b = json.loads(a)  # 因为key和value不一致，所以转不成字典，只能用正则？这也太难了


str1 = '{"accessToken": "521de21161b23988173e6f7f48f9ee96e28", ' \
       '"User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_131)"}'

json1 = json.loads(str1)

print(json1)
print(type(json1))