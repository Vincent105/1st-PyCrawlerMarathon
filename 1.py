from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from datetime import timedelta, datetime

three_age = datetime.today() + timedelta(-3)
fotmated_day = three_age.strftime('%Y/%m/%d')
print(fotmated_day[8:10])