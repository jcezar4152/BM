"""Para rodar o programa será necessario duas Bibliotecas(Selenium e BeautifulSoup)
Para instalar é só  rodar os seguintes comandos no prompt da maquina:

pip install Selenium bs4 pymysql
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pymysql
import time
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
ff = webdriver.Chrome(options=options)
ff.get('https://br.tradingview.com/symbols/BMFBOVESPA-BIDI4/')
while (True):
    print ('Iniciando coleta')
    time.sleep(5)
    html=ff.page_source
    soup=BeautifulSoup(html,"html.parser")
    time.sleep(5)
    ##-----------------------------------##
    filtro1 = soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
    filtro1 = (filtro1[0].text.replace('−','-'))
    ##-----------------------------------
    filtro2 = soup.find_all(class_='js-symbol-change tv-symbol-price-quote__change-value')
    filtro2 = (filtro2[0].text.replace('−','-'))
    ##-----------------------------------
    filtro3 = soup.find_all(class_='js-symbol-change-pt tv-symbol-price-quote__change-value')
    filtro3 = (filtro3[0].text[1:-1].replace('−','-'))
    print (filtro1,"\n",filtro2,"\n",filtro3)
    print("--------------------------------------------------------------------------------")
    ff.refresh()

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