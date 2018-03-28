# -*- coding: utf-8 -*-
import scrapy
from ..items import PrictiseItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    start_urls = ['http://tieba.baidu.com/p/2166231880']

    def parse(self, response):
        item = {}
        item['image_urls'] = []
        picturelist = response.xpath('//div/img[@pic_type="0"]/@src')
        for m in picturelist:
            src = m.extract()
            imgpath = 'http://' + src[7:]
            item['image_urls'].append(imgpath)
        yield item

