"""
Para rodar o programa é necessário ter importada varias Bibliotecas
Para instalar é só  rodar o comando pip install -r req.txt
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from src.notification.alert import hahaha
from src.db.mysql_connection import cursor, connection

cont = int(1)
trigger_email = []
wait =int(10) # Trocar aqui os tempos de espera - mudar para rodar na FATEC devido a INTERNET lenta
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
ff = webdriver.Chrome(options=options,  executable_path="../../resources/chromedriver.exe")
ff.get('https://br.tradingview.com/symbols/BMFBOVESPA-BIDI4/')
while (True):
    while (True):
        print ('Iniciando',cont,'º coleta')
        time.sleep(wait)
        html=ff.page_source
        soup=BeautifulSoup(html,"html.parser")
        time.sleep(2)
        ##-----------------------------------##
        filtro1 = soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
        filtro1 = (filtro1[0].text.replace('−','-'))
        trigger_email.append(filtro1)
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
        cursor.execute("INSERT INTO bvzfdagnfqepipz70gyw.Valor_acoes(Value, IncDec, Variation) VALUES('%s', '%s', '%s')" %(filtro1,filtro2,filtro3))
        cursor.execute("SELECT email FROM bvzfdagnfqepipz70gyw.Usuario")
        q_result = list(cursor.fetchall())
        connection.commit()
        to_addrs = '' # q_result[0:1].
        for x in list(q_result):
            to_addrs += ''.join(x)
            to_addrs += ''.join('; ')

        if trigger_email[-1:] == trigger_email[-2:-1] and trigger_email[-2:-1] == trigger_email[-3:-2]:
            hahaha("Alerta: Ação do Inter MUITO valorizada","Cara, compra logo",to_addrs)
            print("Alerta Enviado: Compra Logo")
        else:
            if trigger_email[-1:] == trigger_email[-2:-1]:
                hahaha("Alerta: Ação do Inter valorizada", "Hora de Comprar",to_addrs)
                print("Alerta Enviado: Compra 1")
