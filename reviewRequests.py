# Python单接口测试
"""
需要导入 requests 模块
通过 requests 发起 get、post请求
"""

# get请求
import requests,json
"""
'''直接访问url'''
urlstr = 'https://www.wanandroid.com/'
r = requests.get(url=urlstr)
# r 为 response
print(r.status_code)
#状态码为200，只能说明这个接口访问的服务器地址正确，并不能说明功能（业务）OK，要看相应内容 r.text（r.content()）
print(r.text)
"""

# params
"""
'''带参数访问 params：https://www.wanandroid.com/article/query?k=Android&key=value'''
urlstr = 'https://www.wanandroid.com/article/query'
payload = {'k': 'Android', 'key': 'value'}
r = requests.get(url=urlstr, params=payload)
print(r.status_code)
print(r.text)
"""

# r.content
"""
'''r.content  字节方式的响应体，自动解码 gzip 和 deflate 压缩'''
urlstr = 'https://www.baidu.com/'
r = requests.get(url=urlstr)
print(r.text)
'''百度首页响应内容是 gzip 压缩的（非 text 文本）'''
print(r.content)
"""

# response 返回内容
"""
urlstr = 'https://www.baidu.com/'
r = requests.get(url=urlstr)
print(f'响应状态{r.status_code}')
print(f'字节响应体，解析gzip和deflate压缩{r.content}')
print(f'以字典对象储服务器响应头{r.headers}')
# print(f'Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常{r.json()}')
print(f'获取url{r.url}')
print(f'获取编码格式{r.encoding}')
print(f'返回原始响应体{r.raw}')
print(r.ok)
"""

# help(requests)


# post请求
# body是json格式————根据 Request Header 中 Content-Type 为 json 格式——'Content-Type': 'application/json'
# 传递方式一：先导入 json 模块，用 dumps 方法转化成 json 格式
"""
urlstr = 'http://httpbin.org/post'
payload = {'qq群名': 'selenium+jmeter+loadrunner', 'qq群号': '106014970'}
payload = json.dumps(payload)
r = requests.post(url=urlstr, data=payload)
print(r.headers)
print(r.text)
"""
# 传递方式二：使用 json 参数默认处理成 json 格式进行传递
"""
urlstr = 'http://httpbin.org/post'
payload = {'qq群名': 'selenium+jmeter+loadrunner', 'qq群号': '106014970'}
payload = json.dumps(payload)
r = requests.post(url=urlstr, json=payload)
print(r.headers)
print(r.text)
"""

# 请求中传递 header————header 为 Python 的字典类型，可以直接 {} 定义
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
header = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
r = requests.post(url=urlstr, data=payload, headers=header)
print(r.headers)
"""

# post 请求
# body 是 data 格式————根据 Request Header 中 'Content-Type': 'application/x-www-form-urlencoded'
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
header = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
r = requests.post(url=urlstr, data=payload, headers=header)
print(r.headers)
print(r.json())
print(r.json()['data']['username'])
"""

# 判断登录成功
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
header = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0'}
r = requests.post(url=urlstr, data=payload, headers=header)
print(r.headers)
print(r.json())
print(r.json()['data']['username'])
if r.json()['data']['username'] == payload['username']:
    print('True')
"""

# data 和 json 区别
"""
# json
# 1、根据 Request Header 中Content-Type
# 1.1 Content-Type: application/json
# 2、通过抓包工具
# 1.1 raw 查看 body 部分，参数最外层 {} 包起来就是json
# 1.2 JSON 可以看到几组参数是json解析后的
# data
# 1、通过抓包工具
# 1.1 raw 查看 body 部分没有 {}
# 1.2 JSON 没有解析的数据
# 1.3 WebForms 中 body 部分左边的 Name 这项就是 key 值，右边的 Value 就是对应的 value 值
"""

# 发 https 请求（ssl）
# 写脚本时，因抓包工具导致代码执行报错：
# requests.exceptions.SSLError: [SSL:CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)
# 解决方法
# 一、关闭抓包工具
# 二、安装依赖包
'''
pip install cryptography
pip install pyOpenSSL
pip install certifi
'''

# session 关联接口
# help(requests.session()) #提供cookie持久性、连接池和配置
# 通过 session 函数自动携带上次请求返回的 cookie 信息，发送二次 post 请求
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
s = requests.session()
r = s.post(url=urlstr, data=payload)
r2 = s.post(url='https://www.wanandroid.com/lg/todo/list/0')
# print(r.text)
print('*****', r2.text)
print(type(r2.text))
if r2.text.find('王登科'):
    print('True')
"""

# json数据处理
# 为什么需要学习 json数据处理
# post 的请求参数是 json 格式，一般常见的接口返回数据也是 json 格式的，做处理时候只需提取关键的参数，就需要 json 来解析返回的数据
'''
json.dumps()#将 Python 对象编码成 JSON 字符串——encode 编码
json.loads()#将已编码的 JSON 字符串，解码为 Python 对象——decode 解码
'''

# encode 编码
# why？————python 中 bool值为True 和 False。json 中则为小写，且区分大小写。为了识别就需要 encode
# step：dict 类型经过 json.dumps（）后变成 str

# decode 解码
# why？————为了获取接口请求后的True 和 False，以便后续代码的判断
# step：r.json()

"""
urlstr = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-UUCAO1609775547781.html'
headers = {'Mozilla': '5.0 (Windows NT 10.0; Win64; x64)', 'AppleWebKit': '537.36 (KHTML, like Gecko)'}
s = requests.session()
r = s.get(url=urlstr, headers=headers, verify=False)
print(r.text)
print(r.json())
result = r.json()
print(result['success'])
print(type(result['success']))
if result['success'] or False:
    print('Ture')
else:
    print('False')
data = result['data']
print(data)
get_result = data[0]['context']
print(get_result)
"""

# token登录
# 前言：有些登录不使用cookie，而是用token参数判断是否登录
# token传参：一种放在请求头中，一种放在请求参数中
# 1、登录返回 token
# 2、请求头带 token
# token 关联
# 步骤：
# 1、登录成功后，
# 2、获取返回 JSON 中的toketn ———— oken = r.json()['token']
# 3、header 中添加 token ———— header['token'] = token
# 4、请求 ———— r = s.post(url, headers=header, data=body)

# 携带 cookie 发送请求
# 1、通过 r.cookie
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
r = requests.post(url=urlstr, data=payload)
print(r.cookies)
cookie = r.cookies
urlstr2 = 'https://www.wanandroid.com/lg/todo/list/0'
r2 = requests.post(url=urlstr2, cookies=cookie)
if r2.text.find('王登科') > 0:
    print('True')
"""
# 2、通过 session
"""
urlstr = 'https://www.wanandroid.com/user/login'
urlstr2 = 'https://www.wanandroid.com/lg/todo/list/0'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
s = requests.session()
r = s.post(url=urlstr, data=payload)
print(r.cookies)
print(r.text)
if r.json()['data']['username'] == payload['username']:
    print('登录成功')
    r2 = s.post(url=urlstr2)
    if r2.text.find('王登科') > 0:
        print('True')
    else:
        print('False')
"""
# 3、通过定制 cookie，单独设置 cookie 来访问目标网址
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nbdd'}
r = requests.post(url=urlstr, data=payload)
print('***', r.text)
print('$$$$', r.cookies)
cookie = {'JSESSIONID': r.cookies['JSESSIONID']}
r2 = requests.get(url='https://www.wanandroid.com/lg/todo/list/0', cookies=cookie)
print(r2.text)
"""

# 4、通过定制 cookie，放入 header 来访问目标网址
"""
urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username': 'dengke_wang', 'password': '0cr18ni11nb'}
r = requests.post(url=urlstr, data=payload)
print('***', r.text)
print('$$$$', r.cookies)
header = {'cookie': 'JSESSIONID='+r.cookies['JSESSIONID']}
r2 = requests.get(url='https://www.wanandroid.com/lg/todo/list/0', headers=header)
result = r2.text.find('王登科')
if result != -1:
    print('查询成功')
else:
    print('查询失败')
"""