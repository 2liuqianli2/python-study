import requests
from lxml import etree


# 根据url获取内容， response
def get_content(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    return response


# 根据response 提取文本内容
def get_content_text(response, encoding="utf-8"):
    response.encoding = encoding
    return response.text


# 根据response 提取二进制内容，字节数据
def get_content_bytes(response):
    return response.content


# 根据response提取json格式数据
def get_content_json(response):
    return response.json()


# 根据文本内容构造 提取器
def extract_tree(text):

    tree = etree.HTML(text)

    return tree


# 根据规则从 xpath提取内容
def extract_hero(tree, xpath_rule):

    result = tree.xpath(xpath_rule)
    return result


# 存储图片列表
def save_images(hero_list):
    for hero in hero_list:
        save_image(hero[0], hero[1])


# 存储单张图片
def save_image(url, filename):
    image_bytes = get_content_bytes(get_content(url))
    with open(filename, "wb") as f:
        f.write(image_bytes)
        f.flush()


if __name__ == '__main__':
    url = "https://pvp.qq.com/web201605/herolist.shtml"
    # 数据获取
    text = get_content_text(get_content(url), encoding="gbk")
    # 数据提取
    hero_img_list = extract_hero(extract_tree(text), "//div[@class='herolist-content']/ul/li/a/img")

    # 数据清洗，数据预处理
    hero_list = []

    for hero_img in hero_img_list:
        image_url = "http:"+hero_img.xpath("./@src")[0]
        filename = "img/" +hero_img.xpath("./@alt")[0] + ".jpg"
        hero_list.append((image_url, filename))
    # 数据存储
    save_images(hero_list)