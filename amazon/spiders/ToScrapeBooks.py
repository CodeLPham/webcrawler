# -*- coding: utf-8 -*-
import scrapy

class ToscrapebooksSpider(scrapy.Spider):
    name = 'books'
    
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'price': book.css('p.price_color::text').get()
            }