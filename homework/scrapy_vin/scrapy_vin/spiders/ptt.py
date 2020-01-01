# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import ScrapyVinItem

class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Lifeismoney/M.1577614539.A.44E.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        author = response.xpath('//*[@id="main-content"]/div[1]/span[2]/text()').get()
        board = response.xpath('//*[@id="main-content"]/div[2]/span[2]/text()').get()
        title = response.xpath('//*[@id="main-content"]/div[3]/span[2]/text()').get()
        creat_time = response.xpath('//*[@id="main-content"]/div[4]/span[2]/text()').get()

        data = ScrapyVinItem()
        data['url'] = response.url
        data['article_author'] = author
        data['article_title'] = title
        data['article_board'] = board
        data['article_time'] = creat_time

        yield data
