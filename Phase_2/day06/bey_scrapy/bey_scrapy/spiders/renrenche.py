import scrapy


class RenrencheSpider(scrapy.Spider):
    name = "renrenche"
    allowed_domains = ["www.renrenche.com"]
    start_urls = ["https://www.renrenche.com/"]

    def parse(self, response):
        pass
