"""Para rodar o programa será necessario duas Bibliotecas(Selenium e BeautifulSoup)
Para instalar é só rodar o seguinte comando no prompt da maquina:

pip install Selenium bs4

"""
from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
import time
x=0
while (x==0):
    ff=webdriver.Chrome()
    ff.get('https://br.tradingview.com/symbols/BTCUSD/?exchange=COINBASE')
    html=ff.page_source
    soup=BeautifulSoup(html,"html.parser")
    time.sleep(10)
    ##-----------------------------------
    filtro1 = soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
    filtro1 = filtro1[0].text[0:-1]
    ##-----------------------------------
    filtro2 = soup.find_all(class_='js-symbol-change tv-symbol-price-quote__change-value')
    filtro2 = filtro2[0].text[0:]
    ##-----------------------------------
    filtro3 = soup.find_all(class_='js-symbol-change-pt tv-symbol-price-quote__change-value')
    filtro3 = filtro3[0].text[1:-1]
    print (filtro1,"\n",filtro2,"\n",filtro3)
    print ("--------------------------------------------------------------------------------")
    time.sleep(10)
    ff.quit()
