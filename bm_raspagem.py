"""Para rodar o programa será necessario duas Bibliotecas(Selenium e BeautifulSoup)
Para instalar é só  rodar os seguintes comandos no prompt da maquina:

pip install Selenium bs4 pymysql
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pymysql
import time
cont = int(1)
wait =int(300) # Trocar aqui os tempos de espera - mudar para rodar na FATEC devido a INTERNET lenta
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
ff = webdriver.Chrome(options=options)
ff.get('https://br.tradingview.com/symbols/BMFBOVESPA-BIDI4/')
while (True):
    print ('Iniciando',cont,'º coleta')
    time.sleep(wait)
    html=ff.page_source
    soup=BeautifulSoup(html,"html.parser")
    time.sleep(2)
    ##-----------------------------------##
    filtro1 = soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
    filtro1 = (filtro1[0].text.replace('−','-'))
    ##-----------------------------------
    filtro2 = soup.find_all(class_='js-symbol-change tv-symbol-price-quote__change-value')
    filtro2 = (filtro2[0].text.replace('−','-'))
    ##-----------------------------------
    filtro3 = soup.find_all(class_='js-symbol-change-pt tv-symbol-price-quote__change-value')
    filtro3 = (filtro3[0].text[1:-1].replace('−','-'))
    print (filtro1," / ",filtro2," / ",filtro3,"\n")
   # print("----------------------------------")
    ###Armazenando link com noticias na variavel noticia.
    noticia=soup.find_all("a",{"class": "tv-widget-news tv-widget-news--link js-widget-news-link js-ga-track-news-escape"})
    cont = cont +1
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