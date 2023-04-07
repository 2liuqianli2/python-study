import requests
from bs4 import BeautifulSoup

def request_content_fun(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
    }   # 反反爬伪装头
    response = requests.get(url, headers=header) # 发送请求
    # response.encoding='UTF-8'
    return response.content # 明面上没有使用utf-8或者其他的解码方式解码

if __name__=='__main__':
    url = 'https://www.douban.com'  # 待爬取地址
    res = request_content_fun(url)
    print(res)
    bs1 = BeautifulSoup(res, features='lxml')
    print(bs1)
