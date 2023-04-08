import scrapy


class XpcSpider(scrapy.Spider):
    name = "xpc"
    allowed_domains = ["www.xinpianchang.com"]
    start_urls = ["https://www.xinpianchang.com/discover/article-1-0-all-all-0-0-hot?from=navigator"]

    def parse(self, response):
        source=response.xpath("//div[@class='sc-5a9b134c-0 ikELow']")
        print(source[0])
        for i in source:
            a=i.xpath("./div[2]/div/a")
            text1=a.xpath("./@title")
            text2=a.xpath("./@href")
            print(text1,text2)
