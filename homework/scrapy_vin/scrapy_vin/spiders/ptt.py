# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Lifeismoney/M.1577614539.A.44E.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, features='xml')
        main_content = soup.find(id='main-content')
        print(main_content)
        metas = main_content.select('div.article-metaline')
