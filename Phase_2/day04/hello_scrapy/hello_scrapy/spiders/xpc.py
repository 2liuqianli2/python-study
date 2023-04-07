import scrapy


class XpcSpider(scrapy.Spider):
    name = "xpc"
    allowed_domains = ["www.xinpianchang.com"]
    start_urls = ["https://www.xinpianchang.com/discover/article-1-0-all-all-0-0-hot?page=1"]

    def parse(self, response):
        url1="https://www.xinpianchang.com/discover/article-1-0-all-all-0-0-hot?page=%s"


        for i in range(25):
            print(i)
            print("8"*50)
            print(scrapy.Request(url1%str(i)))
