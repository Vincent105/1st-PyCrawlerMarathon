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

        item['url'] = response.url
        item['article_author'] = response.xpath(
            '//*[@id="main-content"]/div[1]/span[2]/text()').get(default='not-found')
        item['article_board'] = response.xpath(
            '//*[@id="main-content"]/div[2]/span[2]/text()').get(default='not-found')
        item['article_title'] = response.css(
            '#main-content > div:nth-child(3) > span.article-meta-value::text').get(default='not-found')
        item['article_time'] = response.xpath(
            '//*[@id="main-content"]/div[4]/span[2]/text()').get(default='not-found')

        yield item

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass
