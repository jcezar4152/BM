from selenium import webdriver
import time

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.google.com/'
        self.search_bar = 'q'  # tipo usado ( name )
        self.btn_search = 'btnK'  # tipo usado ( name )

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):              # barra de pesquisa
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
        time.sleep(1)                           # botÃ£o de pesquisa
        self.driver.find_element_by_name(
            self.btn_search).click()


        self.driver.save_screenshot('screen.png')       # print da tela


goo = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")    # local do browser driver
g = Google(goo)
g.navigate()
g.search('bidi4 banco inter')  # o que vai pesquisar
time.sleep(1)
goo.quit()


