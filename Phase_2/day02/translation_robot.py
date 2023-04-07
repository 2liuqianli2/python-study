
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def translate(word):
    option=Options()

    option.add_argument("--headless")
    driver = WebDriver(options=option)
    url="http://fanyi.youdao.com/"
    driver.get(url)
    # sleep(0.5)
    input_original=driver.find_element(By.ID,"js_fanyi_input")
    input_original.send_keys(word)
    sleep(1.5)

    trans_target=driver.find_element(By.CLASS_NAME,"resultOutput")
    print(trans_target.text)


if __name__ == '__main__':
    while True:
        en=input("请输入要翻译的中文内容：")
        translate(en)
