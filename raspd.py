from selenium import webdriver
from bs4 import BeautifulSoup
import time

for contagem in range(0,3):
    ff=webdriver.Chrome()
    ff.get('https://br.tradingview.com/symbols/BMFBOVESPA-BIDI4/')
    html=ff.page_source
    soup=BeautifulSoup(html,"html.parser")
    filtro1=soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
    filtro2=soup.find_all(class_='js-symbol-change tv-symbol-price-quote__change-value')
    filtro3=soup.find_all(class_='js-symbol-change-pt tv-symbol-price-quote__change-value')
    print (filtro1,filtro2,filtro3)
    ff.quit()
    time.sleep(20)
