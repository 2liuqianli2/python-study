import scrapy


class ErshoucheSpider(scrapy.Spider):
    name = "ershouche"
    allowed_domains = ["www.che168.com"]
    start_urls = ["http://www.che168.com/"]

    def parse(self, response):
        pass
