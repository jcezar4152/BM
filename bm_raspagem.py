from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
import pymysql

import time
x=0
while (x==0):
    ff=webdriver.Chrome()
    ff.get('https://br.tradingview.com/symbols/BTCUSD/?exchange=COINBASE')
    html=ff.page_source
    soup=BeautifulSoup(html,"html.parser")
    time.sleep(3)
    #
    filtro1 = soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
    filtro1 = filtro1[0].text[0:-1]
    #
    filtro2 = soup.find_all(class_='js-symbol-change tv-symbol-price-quote__change-value')
    filtro2 = filtro2[0].text[0:]
    #
    filtro3 = soup.find_all(class_='js-symbol-change-pt tv-symbol-price-quote__change-value')
    filtro3 = filtro3[0].text[1:-1]
    #
    connection = pymysql.connect(host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com',
                                 port=3306,
                                 user='ufgpsjx1cswrmye3',
                                 password='ZoKM7HXwAaZAgd9ugpTr')

    #sql = str.format("INSERT INTO bvzfdagnfqepipz70gyw.Valor_acoes (Value, IncDec, Variation) VALUES (%s, %s, %s)" %(filtro1,filtro2,filtro3))

    cursor = connection.cursor()
    cursor.execute("INSERT INTO bvzfdagnfqepipz70gyw.Valor_acoes(Value, IncDec, Variation) VALUES('%s', '%s', '%s')" %(filtro1,filtro2,filtro3))
    connection.commit()
    connection.close()
    time.sleep(10)
    ff.quit()
