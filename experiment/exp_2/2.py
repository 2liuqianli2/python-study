import requests
from  bs4 import BeautifulSoup
import re

url="https://www.dytt8.net/index2.htm"

header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
}

res=requests.get(url,headers=header)
soup=BeautifulSoup(res.content,'lxml')

for i in soup.select('tbody tr td[class="inddline"]>a'):
    if i.get_text()!="最新电影下载":

        print(i.get_text())


# for i in a:
#     aa=re.compile('html">(.*?)</a>')
#     bb=re.findall(aa,str(i))
#     print(bb)