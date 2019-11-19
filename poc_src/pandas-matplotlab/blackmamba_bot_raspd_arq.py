""" Para rodar o programa serÃ¡ necessario duas Bibliotecas(Selenium e BeautifulSoup)
Para instalar Ã© sÃ³  rodar os seguintes comandos no prompt da maquina:
# >>>> AVISO DA SABRINA  - O COMMIT DO COMPANHEIRO ROBSON FOI UM ERRO ONDE AS CREDENCIAIS ESTAVAM GRAVADAS NO PC FATEC <<<<
pip install Selenium bs4
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
ff = webdriver.Chrome(options=options)
ff.get('https://br.tradingview.com/symbols/BMFBOVESPA-BIDI4/')
while (True):
    arquivo = open('arq1.csv', 'a')
    print ('Iniciando coleta')
    time.sleep(5)
    html=ff.page_source
    soup=BeautifulSoup(html,"html.parser")
    time.sleep(5)
    ##-----------------------------------##
    filtro1 = soup.find_all(class_='tv-symbol-price-quote__value js-symbol-last')
    filtro1 = (filtro1[0].text.replace('â','-'))
    ##-----------------------------------
    filtro2 = soup.find_all(class_='js-symbol-change tv-symbol-price-quote__change-value')
    filtro2 = (filtro2[0].text.replace('â','-'))
    ##-----------------------------------
    filtro3 = soup.find_all(class_='js-symbol-change-pt tv-symbol-price-quote__change-value')
    filtro3 = (filtro3[0].text[1:-1].replace('â','-'))
    arquivo.write(filtro1+';'+filtro2+';'+filtro3+'\n')
    print (filtro1,"\n",filtro2,"\n",filtro3)
    print("--------------------------------------------------------------------------------")
    ff.refresh()