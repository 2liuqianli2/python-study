import scrapy


class ChehomeSpider(scrapy.Spider):
    name = 'chehome'
    allowed_domains = ['www.che168.com']
    start_urls = ['https://www.che168.com/china/list/#pvareaid=100945']

    def parse(self, response):
        print(response.text)
        print(response)
