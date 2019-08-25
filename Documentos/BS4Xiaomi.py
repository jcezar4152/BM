from selenium import webdriver
from bs4 import BeautifulSoup as bs


site = 'https://www.oficinadanet.com.br'
url_site = f'{site}/xiaomi'

ch = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
ch.get(url_site)
obj = bs(ch.page_source, 'html.parser')

for link in obj.find_all('a'):
    print (link.get('href', None), link.get_text())


