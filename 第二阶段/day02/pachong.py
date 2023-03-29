import bs4
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import re

header={
"Accept": "text/css,*/*;q=0.1",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

url="https://www.dytt8.net/index2.htm"

get_html=requests.get(url,headers=header)

soup=BeautifulSoup(get_html.content,features='lxml')

title_list=[]
herf_list=[]

titles=soup.select(".co_content2>ul a")
# atitles=soup.select(".co_content2>ul a.string")
# print(titles)
for i in titles:
    a=re.compile(r'<a href="(.*?)">')
    b=a.findall(str(i))[0]
    c='https://www.dytt8.net'+b
    herf_list.append(c)


    a = re.compile(r'html">(.*?)</a>')
    b = a.findall(str(i))[0]
    title_list.append(b)
    # print(b)

dic={
    "标题":title_list,
    "网址":herf_list
}
df=DataFrame(dic)

hh=herf_list[1:30]
# print(hh)
wz_list=[]
asd=[]
for i in hh:
    get_wz=requests.get(i,headers=header)
    soup1=BeautifulSoup(get_wz.content,features='lxml')
    soup2=soup1.select(".co_content8 ul a")
    asd.append(soup2)
    for i in asd:
        a=re.compile(r'<a href="magnet:(.*?)com%3a6969%2fannounce')
        b=a.findall(str(i))[0]
        wz_list.append(b)


print(wz_list)