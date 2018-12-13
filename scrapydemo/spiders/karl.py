# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import PartItem


class KarlSpider(scrapy.Spider):
    name = 'karl'
    allowed_domains = ['karlkustoms.com']
    start_urls = [
        'https://www.karlkustoms.com/p/19355658-Chevrolet-Performance-350-290-308HP-Crate-Engine/46823',
        'https://www.karlkustoms.com/p/12681429K3-5-7L-350-SBC-Engine-Level-3-Install/46826',
        'https://www.karlkustoms.com/p/350-5-7L-Chevrolet-Performance-Truck-Crate-Engine-12530283-Long-Block/1888',
        'https://www.karlkustoms.com/p/350-5-7L-Chevrolet-Performance-Truck-Crate-Engine-12681430-Small-Block/46821',
        'https://www.karlkustoms.com/p/12681432-5-7L-350-GM-OE-Replacement-L31-Vortec-Truck-Crate-Engine/46909',
        'https://www.karlkustoms.com/p/19331650-323-CID-LYS-LMG-GM-Engine/46455',
        'https://www.karlkustoms.com/p/19329865-6-2L-Gen-IV-379-CID-GM-Engine-2007-2008/46566',
        'https://www.karlkustoms.com/p/12632260-5-3L-323-CID-GM-Engine/837',
    ]

    def parse(self, response):
        part = PartItem()
        part['name'] = response.css('h3.title::text').extract()
        part['price'] = response.css('h1.lpprice::text').extract()
        part['partNumber'] = response.css('h4.lppartno::text').extract()
        part['url'] = response.url
        yield part
        pass