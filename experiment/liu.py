import requests
from bs4 import BeautifulSoup
import re
import pandas
url="https://dy.dytt8.net/index2.htm"
header={
'User-Agent':'Mozilla/5.0'
             ' (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
             ' (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}

response=requests.get(url,headers=header)
response.encoding='gbk'
print(response.text)