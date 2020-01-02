# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyVinItem

class Ptt28Spider(scrapy.Spider):
    name = 'ptt28'
    allowed_domains = ['www.ptt.cc']
    start_urls = []

    def __init__(self, filename=None):
        self.cookies = {'over18', '1'}
        self.filename = filename

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived', response.url)

        data = ScrapyVinItem()

        data['url'] = response.url
        data['article_author'] = response.xpath(
            '//*[@id="main-content"]/div[1]/span[2]/text()').get(default='not-found')
        data['article_board'] = response.xpath(
            '//*[@id="main-content"]/div[2]/span[2]/text()').get(default='not-found')
        data['article_title'] = response.css(
            '#main-content > div:nth-child(3) > span.article-meta-value::text').get(default='not-found')
        data['article_time'] = response.css(
            '#main-content > div:nth-child(4) > span.article-meta-value::text').get(default='not-found')

        yield data
