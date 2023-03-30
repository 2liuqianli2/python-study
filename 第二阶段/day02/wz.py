import requests
from lxml import etree
def get_content(url):
    header = {
        "Accept": "text/css,*/*;q=0.1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    res=requests.get(url,headers=header)
    return res

def get_content_text(res,encoding="utf-8"):
    res.encoding= encoding
    return res.text

def get_content_byte(res):

    return res.content

def extract_tree(text):
    tree=etree.HTML(text)
    return tree

def extract_hero(tree,xpath):
    result=tree.xpath(xpath)
    return result

def save_images(hero_list):
    for hero in hero_list:
        save_image(hero[0],hero[1])

def save_image(url,filename):
    image_bytes=get_content_byte(get_content(url))
    with open(filename,'wb') as op:
        op.write(image_bytes)
        op.flush()


if __name__ == '__main__':
    url="https://pvp.qq.com/web201605/herolist.shtml"
    text=get_content_text(get_content(url),encoding='gbk')
    hero_imag_list=extract_hero(extract_tree(text),"//div[@class='herolist-content']/ul/li/a/img")
    hero_list = []
    "//div[@class='herolist-content']/ul/li/a/text()"
    for i in hero_imag_list:
        img_url="http:"+i.xpath("./@src")[0]
        filename="img/"+i.xpath("./@alt")[0] + ".jpg"
        hero_list.append((img_url,filename))
        print(filename)
    save_images(hero_list)
























