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
        """
        Using selectors
        """
        print('************************************************************')
        print('Using selectors*****************')
        print('************************************************************')

        print('01==============================')
        # an XPath for selecting the text inside the title tag:
        print(response.xpath('//title/text()'))
        print('02==============================')
        # To actually extract the textual data
        print(response.xpath('//title/text()').get())
        print(response.xpath('//title/text()').getall())
        print('03==============================')
        # CSS selectors can select text
        print(response.css('title::text').get())
        print(response.xpath('//*[@id="images"]/a[1]/text()').get())
        print('04==============================')
        # It returns None if no element was found:
        print(response.xpath('//div[@id="not-exists"]/text()').get())
        print(response.xpath(
            '//div[@id="not-exists"]/text()').get(default='not-found'))
        print('05==============================')
        # Instead of using e.g. '@src' XPath it is possible to query for attributes using .attrib property of a Selector:
        print(response.css('img').xpath('@src').getall())
        print([img.attrib['src'] for img in response.css('img')])
        print('06==============================')
        # As a shortcut, .attrib is also available on SelectorList directly;
        print(response.css('img').attrib['src'])
        print(response.css('base').attrib['href'])
        print('07==============================')
        # get the base URL and some image links:
        print(response.css('base').attrib['href'])
        print(response.xpath('//base/@href').get())
        print(response.css('base::attr(href)').get())

        print(response.xpath('//a[contains(@href, "image")]/@href').getall())
        print(response.css('a[href*=image]::attr(href)').getall())
        print(response.xpath('//*[@id="images"]/a/@href').getall())

        print(response.xpath(
            '//a[contains(@href, "image")]/img/@src').getall())
        print(response.css('a[href*=image] img::attr(src)').getall())
        print(response.xpath('//*[@id="images"]/a/img/@src').getall())
        print('08==============================')

        print('************************************************************')
        print('Extensions to CSS Selectors*****')
        print('************************************************************')
        print('09==============================')
        # title::text selects children text nodes of a descendant <title> element:
        print(response.css('title::text').get())
        print('10==============================')
        # *::text selects all descendant text nodes of the current selector context:
        print(response.css('#images *::text').getall())
        print(response.css('a::attr(href)').getall())

        print('************************************************************')
        print('Nesting selectors***************')
        print('************************************************************')
        links = response.xpath('//a[contains(@href, "image")]')
        print(links.getall())
        for index, link in enumerate(links):
            args = (index, link.xpath('@href').get(),
                    link.xpath('img/@src').get())
            print('Link number %d points to url %r and image %r' % args)

        print('************************************************************')
        print('Selecting element attributes***************')
        print('************************************************************')
        print(response.xpath("//a/@href").getall())
        print(response.css('a::attr(href)').getall())
        print([a.attrib['href'] for a in response.css('a')])
        print(response.css('base').attrib)
        print(response.css('base').attrib['href'])

        print('************************************************************')
        print('Using selectors with regular expressions***************')
        print('************************************************************')
        print(response.xpath('//a[contains(@href,"image")]/text()'))

        yield item
