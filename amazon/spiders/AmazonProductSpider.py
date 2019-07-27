# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem

class AmazonproductspiderSpider(scrapy.Spider):
    name = 'AmazonDeals'
    
    start_urls = ['https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb_azl']

    def parse(self, response):
        items = AmazonItem()
        title = response.xpath('//*[@id="dealTitle"]/span/text()').extract()
        sale_price = response.xpath('//*[@id="100_dealView_0"]/div/div[2]/div/div/div[3]/div[1]/span/text()').extract()
        # category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        # availability = response.xpath('//div[@id="availability"]//text()').extract()
        items['product_deal'] = ''.join(title).strip()
        items['product_sale_price'] = ''.join(sale_price).strip()
        # items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
        # items['product_availability'] = ''.join(availability).strip()
        yield items
