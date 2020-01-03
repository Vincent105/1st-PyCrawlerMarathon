import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_board = ['Gossiping', 'Stock']
    process = CrawlerProcess({'SPIDER_MODULES': 'scrapy_vin.spiders'})
    for board in target_board:
        process.crawl('ptt29', board=board)
        process.start()


if __name__ == '__main__':
    main()
