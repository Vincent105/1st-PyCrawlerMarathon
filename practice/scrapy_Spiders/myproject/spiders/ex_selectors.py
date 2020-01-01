# -*- coding: utf-8 -*-
import scrapy
from ..items import MyprojectItem


class ExSelectorsSpider(scrapy.Spider):
    name = 'ex_selectors'
    allowed_domains = ['http://example.com/']
    start_urls = [
        'https://docs.scrapy.org/en/latest/_static/selectors-sample1.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived', response.url)

        item = MyprojectItem()

        print('==============================')
        # an XPath for selecting the text inside the title tag:
        print(response.xpath('//title/text()'))
        print('==============================')
        # To actually extract the textual data
        print(response.xpath('//title/text()').get())
        print(response.xpath('//title/text()').getall())
        print('==============================')
        # CSS selectors can select text
        print(response.css('title::text').get())
        print(response.xpath('//*[@id="images"]/a[1]/text()').get())
        print('==============================')
        # It returns None if no element was found:
        print(response.xpath('//div[@id="not-exists"]/text()').get())
        print(response.xpath(
            '//div[@id="not-exists"]/text()').get(default='not-found'))
        print('==============================')
        # Instead of using e.g. '@src' XPath it is possible to query for attributes using .attrib property of a Selector:
        print(response.css('img').xpath('@src').getall())
        print([img.attrib['src'] for img in response.css('img')])
        print('==============================')
        # As a shortcut, .attrib is also available on SelectorList directly;
        print(response.css('img').attrib['src'])
        print('==============================')
        
        yield item
