import scrapy

from ByeScrapy.items import GuaziCarItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/www/buy/']

    guazi_host = "https://www.guazi.com"

    def parse(self, response):
        # 提取所有的品牌链接
        brand_list = response.xpath('//div[@class="screen"]/dl[1]/dd/div[contains(@class,"dd-all")]/ul/li/p/a')

        for brand in brand_list:
            car_brand = brand.xpath("./text()").extract_first()
            car_brand_url = brand.xpath("./@href").extract_first()
            # 请求各品牌的链接
            yield scrapy.Request(url=self.guazi_host + car_brand_url, callback=self.parse_brand, meta={"car_brand": car_brand})

    def parse_brand(self, response):
        # 提取品牌第一页的数据
        car_list = response.xpath('//ul[contains(@class,"carlist")]/li')

        car_brand = response.meta.get("car_brand")

        for car in car_list:
            # extract_first 导出第一项
            car_title = car.xpath('./a/h2/text()').extract_first()
            car_price = car.xpath('./a/div[@class="t-price"]/p/text()').extract_first()
            car_price_source = car.xpath('./a/div[@class="t-price"]/em/text()').extract_first()
            car_info = car.xpath('./a/div[@class="t-i"]/text()').extract()

            # 数据存储
            item = GuaziCarItem()
            item["car_brand"] = car_brand
            item["car_title"] = car_title
            item["car_price"] = car_price
            item["car_price_source"] = car_price_source
            item["car_info"] = car_info

            yield item

        # 获取下一页的地址，地址存在，继续发送请求
        next_url = response.xpath('//ul[contains(@class,"pageLink")]/li/a[@class="next"]/@href').extract_first()

        if next_url:
            # 将品牌对应的所有页面获取页面
            yield scrapy.Request(url=self.guazi_host + next_url, callback=self.parse_brand, meta={"car_brand": car_brand})