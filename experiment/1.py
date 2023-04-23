import requests
from lxml import etree
import pandas as pd

header={
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Accept-Encoding': 'gzip, deflate, br',
'Accept': '*/*',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
# 'Cookie': 'bid=f2924kdy97Q; ll="118277"; dbcl2="270039718:LebDIsZ2jSM"; '
#           'ck=kUB8; push_noty_num=0; push_doumail_num=0; __utma='
#           '30149280.1636434033.1682249765.1682249765.1682249765.1; __utmc=30149280; '
#           '__utmz=30149280.1682249765.1.1.utmcsr=movie.douban.com|utmccn=(referral)'
#           '|utmcmd=referral|utmcct=/; __utmt=1; __utmv=30149280.27003; __utmb=30149280.2.10.1682249765;'
#           ' frodotk_db="4e5a7e857a178d1deb0f7b906e46a757"'
}

url="https://movie.douban.com/subject/35267208/reviews"

res=requests.get(url=url,headers=header)
with open("./douban.html",'w',encoding='utf-8') as op :
    op.write(res.text)

data=etree.HTML(res.text)
# print(data.xpath("//div[@class='review-list  ']"))
# print(data.xpath("//div[@class='review-list  ']//div[@class='short-content']"))
img_list=[]
name_list=[]
assess_list=[]
data_list=data.xpath("//div[@class='review-list  ']/div")
print(data_list)
for i in data_list:
    img=i.xpath("./div//a[@class='avator']/img/@src")
    name=i.xpath("./div//a[@class='name']/text()")
    assess=i.xpath("./div/div/div/div[@class='short-content']/text()")
    img_list.append(img[0])
    name_list.append(name[0])
    assess_list.append(assess[0].strip())

# print(img_list,assess_list,name_list)

dic={
    'name':name_list,
    'img':img_list,
    'assess':assess_list
}
#
a=pd.DataFrame(data=dic)
a.to_excel("./豆瓣评论.xlsx")