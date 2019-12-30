# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyVinItem(scrapy.Item):
    author = scrapy.Field()
    board = scrapy.Field()
    title = scrapy.Field()
    creat_time = scrapy.Field()
