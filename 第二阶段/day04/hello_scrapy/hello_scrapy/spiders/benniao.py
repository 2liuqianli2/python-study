import scrapy

from items import QuoteItem


class BenniaoSpider(scrapy.Spider):
    name = "benniao"
    allowed_domains = ["benniao365.com"]
    start_urls = ["http://benniao365.com/"]

    def parse(self, response):
        texts=response.xpath("//*[@id='portal_block_4_content']/div/div/ol/li/text()").extract()

        for text in texts:
           # from items import QuoteItem
           item=QuoteItem()
           item["content"]=text
           yield item