import scrapy


class XpcSpider(scrapy.Spider):
    name = "xpc"
    allowed_domains = ["www.xinpianchang.com"]
    # start_urls = ["https://www.benniao365.com/article-368-1.html"]
    start_urls =["https://www.xinpianchang.com/discover/article-1-0-all-all-0-0-hot?page=1"]

    x=1
    def parse(self, response):
        # text=response.xpath("//a[@class='nxt']/@href").extract_first()
        text="https://www.xinpianchang.com/discover/article-1-0-all-all-0-0-hot?page=%s"
        text1=response.text

        print(text1)
        print("...................")
        self.x +=1
        if self.x<15:
            yield scrapy.Request(url=text%str(self.x))

        else:
            print("完成。。。。。。。。。。。。。。")

