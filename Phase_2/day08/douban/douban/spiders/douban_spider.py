import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["www.douban.com"]
    start_urls = ["https://movie.douban.com/"]

    def parse(self, response):
        # print(response.text)
        with open("./douban.html",'w',encoding='utf-8') as op:
            op.write(response.text)
