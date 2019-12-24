from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import pandas as pd

browser = webdriver.Chrome(executable_path='chromedriver\chromedriver.exe')
browser.get("http://taqm.epa.gov.tw/taqm/tw/MonthlyAverage.aspx")

selectSite = Select(browser.find_element_by_id("ctl05_ddlSite"))
selectSite.select_by_value('11')
selectYear = Select(browser.find_element_by_id("ctl05_ddlYear"))
selectYear.select_by_value('2019')
browser.find_element_by_id('ctl05_btnQuery').click()

time.sleep(3)

html_source = browser.page_source
html_source

soup = BeautifulSoup(html_source, 'html.parser')
tmp = soup.find('table', class_='TABLE_G').find_all('tr')

first = tmp[0]
allRows = tmp[1:-3]

headers = [header.get_text() for header in first.find_all('th')]
results = [[data.get_text() for data in row.find_all('td')] for row in allRows]
results

rowspan = []

for no, tr in enumerate(allRows):
    tmp = []
    for td_no, data in enumerate(tr.find_all('td')):
        # print(data.has_key("rowspan"))
        if data.has_attr("rowspan"):
            rowspan.append((no, td_no, int(data["rowspan"]), data.get_text()))

if rowspan:
    for i in rowspan:
        # tr value of rowspan in present in 1th place in results
        for j in range(1, i[2]):
            # - Add value in next tr.
            results[i[0]+j].insert(i[1], i[3])


df = pd.DataFrame(data=results, columns=headers)
print(df)