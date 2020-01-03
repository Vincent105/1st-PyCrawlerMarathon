# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyVinItem
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class Ptt28Spider(scrapy.Spider):
    name = 'ptt29'

    def __init__(self, board='Stock'):
        self.cookies = {'over18': '1'}
        self.host = 'https://www.ptt.cc'
        self.board = board
        self.start_urls = 'https://www.ptt.cc/bbs/{}/index.html'.format(board)
        super().__init__()

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        self.logger.info('A response from %s just arrived', response.url)

        soup = BeautifulSoup(response.text)
        main_list = soup.find('div', class_='bbs-screen')

        # 依序檢查文章列表中的 tag, 遇到分隔線就結束，忽略這之後的文章
        for div in main_list.findChildren('div', recursive=False):
            class_name = div.attrs['class']

            # 遇到分隔線要處理的情況
            if class_name and 'r-list-sep' in class_name:
                self.log('Reach the last article')
                break

            # 遇到目標文章
            if class_name and 'r-ent' in class_name:
                div_title = div.find('div', class_='title')
                a_title = div_title.find('a', href=True)
                # 如果文章已經被刪除則跳過
                if not a_title or not a_title.has_attr('href'):
                    continue
                article_URL = urljoin(self.host, a_title['href'])
                article_title = a_title.text
                self.log('Parse article {}'.format(article_title))
                yield scrapy.Request(url=article_URL,
                                     callback=self.parse_article,
                                     cookies=self.cookies)

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
