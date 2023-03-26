import requests as re
from bs4 import  BeautifulSoup
url='https://movie.douban.com/subject/35312421/?tag=%E7%83%AD%E9%97%A8&from=gaia'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'accept':'*/*',
}
# for i in range(11):
ros=re.get(url,headers=headers)

# print(ros.text)
bs1=BeautifulSoup(ros.content,features='html.parser')
print(bs1)
    # with open('./%d.html'%i,"w",encoding='utf-8') as op:
    #     op.write(ros.text)
    #     op.flush()


# print(a.decode('gzip'))
# with open('./王者荣耀.html','w',encoding='utf-8') as op:
#     op.write(str(bs1))
#     op.flush()