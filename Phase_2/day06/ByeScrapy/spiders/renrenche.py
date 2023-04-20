import scrapy

from ByeScrapy.items import RenRenCarItem


class RenrencheSpider(scrapy.Spider):
    name = 'renrenche'
    allowed_domains = ['www.renrenche.com']
    start_urls = ['https://www.renrenche.com/cn/ershouche/']

    renrenche_host = "https://www.renrenche.com"

    def parse(self, response):
        # 获取品牌列表
        brand_list = response.xpath('//div[contains(@class, "brand-section")]/p/span[contains(@class, "bn")]/a')

        for brand in brand_list[0:1]:
            brand_url = brand.xpath("./@href").extract_first()
            brand_name = brand.xpath("./text()").extract_first()
            # 根据不同的品牌地址发送请求
            yield scrapy.Request(url=self.renrenche_host + brand_url, callback=self.parse_brand, meta={"brand_name": brand_name})

    def parse_brand(self, response):
        # 获取车的列表
        car_list = response.xpath('//ul[@class="row-fluid list-row js-car-list"]/li/a/@href').extract()

        for car in car_list:
            # 获取车的详情信息
            yield scrapy.Request(url=self.renrenche_host + car, callback=self.parse_brand_car_detail, meta={"brand_name": response.meta.get("brand_name")})
        # 下一页的连接获取
        # next_url = response.xpath('//ul[@class="pagination js-pagination"]/li/a[@rrc-event-name="switchright"]/@href').extract_first()
        # # 判定是否是url
        # if not next_url.startswith("javascript"):
        #     yield scrapy.Request(url=self.renrenche_host + next_url, callback=self.parse_brand, meta={"brand_name": response.meta.get("brand_name")})

    def parse_brand_car_detail(self, response):

        car_description = response.xpath('//meta[@name="description"]/@content').extract_first()
        car_price = response.xpath('//p[@class="price detail-title-right-tagP"]/text()').extract_first()
        car_price_source = response.xpath('//div[@class="new-car-price detail-title-right-tagP"]/span/text()').extract_first()
        car_title = "".join(response.xpath('//h1[contains(@class,"title-name")]/text()').extract())
        # car_kilometre = response.xpath('//div[@id="zhimaicar-detail-header-right"]/div/ul/li[@class="kilometre"]/div/p/strong/text()').extract_first()
        car_description_item = [item.split(":") for item in car_description.split(",")]
        car_kilometre = car_description_item[2][1]
        car_timedelta = response.xpath('//li[@class="span7"]/div/p/strong/text()').extract_first()

        car_brand = response.meta.get("brand_name")

        print(car_price, car_price_source, car_title, car_kilometre, car_timedelta, car_brand)

        items = RenRenCarItem()

        items["car_price"] = car_price
        items["car_price_source"] = car_price_source
        items["car_title"] = car_title
        items["car_kilometre"] = car_kilometre
        items["car_timedelta"] = car_timedelta
        items["car_brand"] = car_brand

        yield items