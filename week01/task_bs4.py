import requests
import lxml.etree


# 爬取页面详细信息

# 电影详细页面
url = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers=header)


# xml化处理
selector = lxml.etree.HTML(response.text)

# 电影名称
film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span[1]/text()')
print(f'电影名称: {film_name}')

# 电影类型
file_type = selector.xpath('///*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/span/text()')
print(f'电影类型: {file_type}')

# 上映日期
plan_date = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/span/text()')
print(f'上映日期：{plan_date}')

mylist = [film_name, file_type,plan_date]


import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

