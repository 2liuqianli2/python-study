import requests
from lxml import etree



# url="https://beijing.zbj.com/search/f/?type=new&kw=saas&r=2"
url='https://pvp.qq.com/web201605/herolist.shtml'

header={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

'accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',


        }
res=requests.get(url,headers=header)
res.encoding='gbk'

et = etree.HTML(res.text)
heros = et.xpath("//div[@class='herolist-content']/ul/li/a/text()")
for i in heros:
        print(i,len(heros))