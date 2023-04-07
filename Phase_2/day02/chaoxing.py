import requests
from lxml import etree
url='http://i.chaoxing.com/base?t=1645608348941'

header={
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

'accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',

}

data=requests.get(url,headers=header)

data_xpath=etree.HTML(data.text)
print(data.text)
ke=data_xpath.xpath("//div[@class='courselistArea'and@id='courselistArea']/div/ul/li/text()")
print(ke)