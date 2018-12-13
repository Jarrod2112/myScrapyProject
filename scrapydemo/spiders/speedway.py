# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import PartItem

class SpeedwaySpider(scrapy.Spider):
    name = 'speedway'
    allowed_domains = ['speedwaymotors.com']
    start_urls = [
        'https://www.speedwaymotors.com/Chevrolet-Performance-19355658-SBC-350-290-HP-LB-Crate-Engine,330742.html',
        'https://www.speedwaymotors.com/GM-12681429-Replacement-Base-Truck-350-5-7-Crate-Engine,330667.html',
        'https://www.speedwaymotors.com/GM-12530283-Replacement-Long-Block-Vortec-5-7-350-Crate-Engine,256448.html',
        'https://www.speedwaymotors.com/GM-12530282-Replacement-Vortec-350-L31-Crate-Engine-1996-02,330665.html',
    ]

    def parse(self, response):
        part = PartItem()
        part['name'] = response.css('h1#title::text').extract()
        part['price'] = response.css('span#priceText::text').extract()
        part['partNumber'] = response.css('div.productId::text').extract()
        part['url'] = response.url
        yield part
        pass
