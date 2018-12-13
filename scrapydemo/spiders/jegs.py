# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import PartItem

class JegsSpider(scrapy.Spider):
    name = 'jegs'
    allowed_domains = ['jegs.com']
    start_urls = [
      'https://www.jegs.com/i/Chevrolet-Performance/809/12681429/10002/-1',
      'https://www.jegs.com/i/Chevrolet-Performance/809/12681430/10002/-1',
	  'https://www.jegs.com/i/Chevrolet-Performance/809/19355658/10002/-1',
	  'https://www.jegs.com//i/Chevrolet-Performance/809/12681429/10002/-1?NttInput=10067353',
	  'https://www.jegs.com/i/Chevrolet-Performance/809/12530283/10002/-1',
	  'https://www.jegs.com//i/Chevrolet-Performance/809/12681430/10002/-1?NttInput=12568758',
	  'https://www.jegs.com/i/Chevrolet-Performance/809/12681432/10002/-1',
	  'https://www.jegs.com//i/Chevrolet-Performance/809/12681432/10002/-1?NttInput=12530282',
    ]

    def parse(self, response):
        part = PartItem()
        part['name'] = response.css('h1.productItemName::text').extract()
        part['price'] = response.css('div#price::text').extract()
        part['partNumber'] = response.css('span#product_id::text').extract()
        part['url'] = response.url
        yield part
        pass