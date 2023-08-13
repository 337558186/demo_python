"""
@Time ： 2023/5/30 10:39
@Auth ： 植树的牧羊人
@desc : 豆瓣电影TOP100
首先定义了要爬取的网页链接和请求头信息，
然后通过循环来依次爬取TOP100中每一页的电影信息，并将电影名字存入一个列表中。
最后，我们再通过循环输出列表中的电影名字即可。
注意，由于豆瓣网站的反爬虫机制比较厉害，所以我们需要在请求头中设置User-Agent信息来模拟浏览器访问。
"""

import requests
from fake_useragent import UserAgent
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import re
import csv


headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# bs4解析
def get_parse1(result):
    D = []  # 保存数据
    soup = BeautifulSoup(result,'lxml')
    items=soup.select('ol>li')
    for item in items:
        rank=item.select('.pic em')[0].string
        haibao=item.select('.pic>a>img')[0]['src']
        name=item.select('.hd>a>span')[0].string
        actor=item.select('.bd>p')[0].text
        pingfen=item.select('.star>span')[1].string
        pingjia=item.select('.star>span')[3].string
        jianjie=item.select('.quote span')[0].string
        print(rank,haibao,name,actor,pingfen,pingjia,jianjie)

        data = [rank, haibao, name, actor, pingfen, pingjia, jianjie]
        D.append(data)
    save(D)

# 保存总数据
def save(data):
    header = ('链接', '海报', '名称', '演员', '评分', '评价', '简介')
    with open('./豆瓣电影top250.csv', 'a', newline='', encoding='gb18030')as file:
        write = csv.writer(file)
        write.writerow(header)
        write.writerows(data)



# re解析
def get_parse2(result):
    regex = '<em class="">(\d+)</em>.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>'
    pattern=re.compile(regex,re.S)
    items=re.findall(pattern,result)
    # print(items)
    for item in items:
        content=""
        # 通过空格进行切片处理
        for i in item[2].split():
            content=content+"".join(i)
        # 去除字符串中的&nbsp;和换行符
        content = re.sub('&nbsp;', ' ', content)
        content = re.sub('<br>', ' ', content)
        print(item[0],item[1],content,item[3],item[4],item[5])


# jquery解析
def get_parse3(result):
    doc=pq(result)
    # 遍历操作，使用item()方法，会得到一个生成器
    items=doc('ol>li').items()
    for item in items:
        rank=item.find('.pic em').text()
        haibao=item.find('.pic>a>img').attr('src')
        name=item.find('.hd>a>span').text()
        actor=item.find('.bd>p').text()
        pingfen=item.find('.star>span').eq(1).text()
        pingjia=item.find('.star>span').eq(3).text()
        jianjie=item.find('.quote span').text()
        print(rank,haibao,name,actor,pingfen,pingjia,jianjie)


def main():
    for i in range(0,10):
        url='https://movie.douban.com/top250?start={}'.format(i*25)
        response=requests.get(url=url,headers=headers)

        result=response.text
        get_parse1(result)



if __name__=='__main__':
    main()