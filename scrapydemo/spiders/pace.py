# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import PartItem

class PaceSpider(scrapy.Spider):
    name = 'pace'
    allowed_domains = ['paceperformance.com']
    start_urls = [
        'https://paceperformance.com/i-6485019-12681430-5-7l-350cid-lo5-k-1987-1995-chevy-gmc-full-size-trucks-g-van-up-to-7200-gvw.html',
        'https://paceperformance.com/i-6255330-19355658-chevrolet-performance-sbc-350cid-290hp-base-long-block-crate-engine.html',
        'https://paceperformance.com/i-6218525-10066039-replacement-gm-oil-pan-for-10067353-universal-350-engine.html',
        'https://paceperformance.com/i-23836612-12530283-new-gm-1996-2000-5-7l-350-cid-vin-r-3-4-1-ton-replacement-engine.html',
        'https://paceperformance.com/i-6485019-12681430-5-7l-350cid-lo5-k-1987-1995-chevy-gmc-full-size-trucks-g-van-up-to-7200-gvw.html',
        'https://paceperformance.com/i-23836611-12681432-new-gm-1996-2000-5-7l-350-cid-vin-r-replacement-engine.html',
        'https://paceperformance.com/i-23849780-19331650-remanufactured-engine.html',
        'https://paceperformance.com/i-23837802-19329865-engine.html',
        'https://paceperformance.com/i-5135038-12632260-new-gm-2010-2013-5-3l-323-cid-8-cylinder-engine.html'
    ]

    def parse(self, response):
        part = PartItem()
        part['name'] = response.css('h1.wsm-prod-title::text').extract()
        part['price'] = response.css('span.wsm-cat-price-price-value.wsmjs-product-price::text').extract()
        part['partNumber'] = response.css('span.wsm-prod-sku::text').extract()
        part['url'] = response.url
        yield part
        pass