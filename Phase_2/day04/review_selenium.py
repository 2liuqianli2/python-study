from time import sleep
from lxml import etree

import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


#将浏览器隐藏起来
# option=Options()
# option.add_argument("--headless")
# driver=WebDriver(options=option)

driver=WebDriver()

url="https://101.qq.com/#/hero"

# sleep(4)
#访问网页
driver.get(url)
#返回网页资源
a=driver.page_source


etrees=etree.HTML(a)

b=etrees.xpath("//ul[@class='hero-list']/li/div/p/text()")


#返回网页资源
print(b)




#按照id查找元素
# data=driver.find_element(By.ID,"js_fanyi_input")

#往元素中送入参数
# data.send_keys("")

