from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver

from wz import extract_hero, extract_tree, save_images

driver=WebDriver()

url = "https://pvp.qq.com/web201605/herolist.shtml"
driver.get(url)

sleep(5)

text=driver.page_source
hero_imag_list = extract_hero(extract_tree(text), "//div[@class='herolist-content']/ul/li/a/img")
hero_list = []
"//div[@class='herolist-content']/ul/li/a/text()"
for i in hero_imag_list:
    img_url = "http:" + i.xpath("./@src")[0]
    filename = "img2/" + i.xpath("./@alt")[0] + ".jpg"
    hero_list.append((img_url, filename))
    print(filename)
save_images(hero_list)




