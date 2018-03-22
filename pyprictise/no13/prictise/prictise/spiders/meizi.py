# -*- coding: utf-8 -*-
import scrapy
from ..items import PrictiseItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    start_urls = ['http://tieba.baidu.com/p/2166231880']

    def parse(self, response):

        picturelist = response.xpath('//img/@src').extract()
        for m in picturelist:
            item = PrictiseItem()
            item['image_urls'] = [m]
            yield item

