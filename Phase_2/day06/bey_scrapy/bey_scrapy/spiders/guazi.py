import scrapy



class GuaziSpider(scrapy.Spider):
    name = "guazi"
    allowed_domains = ["www.guazi.com"]
    start_urls = ["http://www.guazi.com/"]

    def parse(self, response):
        print(response.text)
