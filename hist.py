from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
nav=webdriver.Chrome
nav.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay=26&beginMonth=10&beginYear=2018&endDay=26&endMonth=10&endYear=2019&size=200&page=1&period=")
time.sleep(10)
page=nav.page_source()
soup=bs(page,"html.parser")
print (soup)