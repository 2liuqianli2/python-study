import scrapy

from ..items import QuoteItem


class BenniaoSpider(scrapy.Spider):
    name = "benniao"
    allowed_domains = ["benniao365.com"]
    start_urls = ["http://benniao365.com/"]

    def parse(self, response):
        texts=response.xpath("//*[@id='portal_block_4_content']/div/div/ol/li/a/text()").extract()
        print(texts)
        print("*-"*50)


        for text in texts:
            item=QuoteItem()
            item["content"]=text
            yield item


