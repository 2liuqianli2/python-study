from time import sleep

import requests
import selenium
from lxml import etree
from selenium.webdriver.chrome.webdriver import WebDriver
import pandas as pd


class spider():

    def __init__(self,url):
        self.url=url
        self.res=None
        self.header = {
            "Accept": "text/css,*/*;q=0.1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }

    def selenium_get(self):
        moni = WebDriver()
        moni.get(self.url)
        sleep(5)

        return moni.page_source

    def get_html(self):
        res=requests.get(self.url,headers=self.header)

        return res

    def get_html_text(self,encoding="utf-8"):
        a=self.get_html()
        a.encoding=encoding
        return a.text

    def get_html_content(self):

        return self.get_html().content

    def etrees(self,html):
        result=etree.HTML(html)
        return result

    def xpath_result(self,xp_re,encoding="utf-8"):
        b=self.etrees(self.get_html_text(encoding))
        if b.xpath(xp_re)==[]:
            # print(self.selenium_get())
            b = self.etrees(self.selenium_get())

        return b.xpath(xp_re)


if __name__ == '__main__':

    url="https://we.51job.com/pc/search?jobArea=010000&keyword=python&searchType=2&sortType=0&metro="

    list1=[]
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    dic={
        "公司名称":list1,
        "招聘发布时间":list2,
        "工资":list3,
        "待遇":list4,
        "岗位":list5,
        "公司性质":list6,
        "公司地址与要求":list7
    }

    a=spider(url)
    list0=a.xpath_result("//*[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div")

    for i in list0:
        a=i.xpath("./a/div/span[1]/text()")#什么岗位
        list5.append(a[0])

        b=i.xpath("./a/div/span[2]/text()")#什么时间发布的
        list2.append(b[0])

        c = i.xpath("./a/p/span[1]/text()")#工资
        list3.append(c[0])

        d = i.xpath("./a/p/span[2]/span/text()")#公司地址与要求
        d="".join(d)
        d=d.replace('|',' ',2)
        list7.append(d)

        f=i.xpath("./a/p[2]/span/@title")#待遇
        f=" ".join(f)
        list4.append(f)

        e=i.xpath("./div[2]/a/text()")#公司名称
        list1.append(e[0])

        g = i.xpath("./div[2]/p[1]/text()")  # 公司性质
        list6.append(g[0])




data=pd.DataFrame(dic)
data.to_excel("./招聘数据.xlsx")


