# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/19 8:54
@Auth ： magician
@Desc ：请求响应
"""
import requests

"""
params	字典	url为基准的url地址，不包含查询参数；该方法会自动对params字典编码,然后和url拼接
url	字符串	requests 发起请求的地址
headers	字典	请求头，发送请求的过程中请求的附加内容携带着一些必要的参数
cookies	字典	携带登录状态
proxies	字典	用来设置代理 ip 服务器
timeout	整型	用于设定超时时间， 单位为秒
"""
resp = requests.get(url="https://www.baidu.com")
print(resp)



# POST
word = input("please input a word")
url = "https://fanyi.baidu.com/sug"
data = {
    "kw": word,
}
headers = {
    'User-Agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664 .93 Safari / 537.36",
}
"""
data	字典	作为向服务器提供或提交资源时提交，主要用于 post 请求
json	字典	json格式的数据， json合适在相关的html
"""
resp = requests.get(url=url, data=data, headers=headers)
"""
resp.status_code	http请求的返回状态，若为200则表示请求成功。
resp.raise_for_status()	该语句在方法内部判断resp.status_code是否等于200，如果不等于，则抛出异常
resp.text	http响应内容的字符串形式，即返回的页面内容
resp.encoding	从http header 中猜测的相应内容编码方式
resp.apparent_encoding	从内容中分析出的响应内容编码方式（备选编码方式）
resp.content	http响应内容的二进制形式
resp.json()	得到对应的 json 格式的数据，类似于字典
"""
print(resp.json())



