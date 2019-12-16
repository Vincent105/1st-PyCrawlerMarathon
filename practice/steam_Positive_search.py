import requests
import re
import csv
from bs4 import BeautifulSoup

steam_Positive_searchs = {}

# 控制擷取列表頁數量：
max_page = 2

for page_number in range(1, max_page+1, 1):

    url = 'https://store.steampowered.com/search/?'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    payload = {'page': str(page_number)}
    resp = requests.get(url, params=payload, headers=headers)
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'html.parser')
    html = soup.find("div", attrs={"id": "search_resultsRows"}).find_all("a")


    for i in html:
        satisfaction = i.find(
            "div", attrs={"class": "col search_reviewscore responsive_secondrow"}).find(
            "span", attrs={"data-tooltip-html": True})
        if satisfaction is None:
            continue
        elif re.match('Overwhelmingly Positive', satisfaction['data-tooltip-html']):
            print(
                "-------------------------------------------------------------------------")
            print("遊戲序號：", i.get('data-ds-appid'))
            game_name = i.find(
                "div", attrs={"class": "col search_name ellipsis"})
            print("遊戲名稱：", game_name.span.string)
            realse_date = i.find(
                "div", attrs={"class": "col search_released responsive_secondrow"})
            print("發售日期：", realse_date.string)
            print("遊戲評價：", satisfaction['data-tooltip-html'])

            print("商店頁面：", i.get('href'))

            price = i.find(
                "div", attrs={"class": "col search_price_discount_combined responsive_secondrow"})
            if price.div.span is None:
                print("產品原價：", price.find(
                    class_="col search_price responsive_secondrow").string.strip())
                print("產品折價：", '')
                print("折扣幅度：", '')
            else:
                print("產品原價：", price.find(
                    class_="col search_price discounted responsive_secondrow").strike.text)
                print("產品折價：", price.find(
                    class_="col search_price discounted responsive_secondrow").find('br').next_sibling)
                print("折扣幅度：", price.div.span.string)
        else:
            pass
