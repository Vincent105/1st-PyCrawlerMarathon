# -*- coding: utf-8 -*-
import scrapy
from ..items import MyprojectItem


class MySpider(scrapy.Spider):
    name = 'My'
    allowed_domains = ['www.ptt.cc']
    start_urls = [
        'https://www.ptt.cc/bbs/Lifeismoney/M.1577787844.A.93E.html',
        'https://www.ptt.cc/bbs/Lifeismoney/M.1577790895.A.4C2.html',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived', response.url)
        item = MyprojectItem()
        item['title'] = response.xpath(
            '//*[@id="main-content"]/div[3]/span[2]/text()').get()

        item['author'] = response.xpath(
            '//*[@id="main-content"]/div[1]/span[2]/text()').get()

        yield item

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass
