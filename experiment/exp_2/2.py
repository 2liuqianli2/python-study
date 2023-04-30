import requests
from  bs4 import BeautifulSoup
import re

url="https://www.dytt8.net/index2.htm"

header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
}

res=requests.get(url,headers=header)
soup=BeautifulSoup(res.content,'lxml')


with open("./move_name.text",'w+',encoding='utf-8') as op:
    for i in soup.select('tr td[class="inddline"]>a'):
        if len(i.get_text()) > 7:
            op.write(i.get_text())
            op.write("\n")
            op.flush()
        # 网络爬虫与数据采集



        # print(i.get_text())


# for i in a:
#     aa=re.compile('html">(.*?)</a>')
#     bb=re.findall(aa,str(i))
#     print(bb)
