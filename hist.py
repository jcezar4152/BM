from bs4 import BeautifulSoup
import requests
import pymysql
### as vareaveis abaixo sÃ£o contadores para pegar a posiÃ§Ã£o exata dos valores no html
b=8
c=9
d=10
e=11
f=12
g=13
h=14
diaI=input("Precisamos de um periodo para buscar o histrico, favor informar o dia inicial: ")
mesI=input("Informe o mÃªs incial: ")
anoI=input("informe o ano inicial: ")
diaF=input("Favor informar o dia final: ")
mesF=input("Informe mÃªs final: ")
anoF=input("Para finalizar, favor informar o ano final do periodo: ")
nav=requests.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay="+diaI+"&beginMonth="+mesI+"&beginYear="+anoI+"&endDay="+diaF+"&endMonth="+mesF+"&endYear="+anoF+"&size=200&page=1&period=")
html=nav.text
soup=BeautifulSoup(html,'html.parser')
a=soup.findAll('td')
valida=True
connection = pymysql.connect(host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com',
                                 port=3306,
                                 user='ufgpsjx1cswrmye3',
                                 password='ZoKM7HXwAaZAgd9ugpTr')
while(valida==True):

        data_acao=a[b].text

        valor_fechado=a[c].text.replace(",",".")
        valor_fechado=float(valor_fechado)

        valor_minimo=a[d].text.replace(",",".")
        valor_minimo=float(valor_minimo)

        valor_maximo=a[e].text.replace(",",".")
        valor_maximo=float(valor_maximo)

        valor_variacao=a[f].text.replace(",",".")
        valor_variacao=float(valor_variacao)

        valor_porc=a[g].text.replace(",",".")
        valor_porc=float(valor_porc)

        volume=a[h].text.replace(",",".")
        volume=float(volume)

        cursor = connection.cursor()
        cursor.execute(
                "INSERT INTO bvzfdagnfqepipz70gyw.Historico(data_acao, valor_fechado, valor_minimo, valor_maximo, valor_variacao, variacao_porc, volume) VALUES('%s', '%f', '%f','%f','%f','%f','%f')"%(data_acao,valor_fechado,valor_minimo,valor_maximo,valor_variacao,valor_porc,volume))
        connection.commit()
        connection.close()
        b=b+7
        c=c+7
        d=d+7
        e=e+7
        f=f+7
        g=g+7
        h=h+7
        '''###Agora iremos alterar a pagina para pegar o restante dos dados, foi necessario zerar os contadores pois Ã© "uma nova pagina".
        if(b==1401):
                arq.close()
                nav=requests.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay="+diaI+"&beginMonth="+mesI+"&beginYear="+anoI+"&endDay="+diaF+"&endMonth="+mesF+"&endYear="+anoF+"&size=200&page=2&period=")
                html=nav.text
                soup=BeautifulSoup(html,'html.parser')
                a=soup.findAll('td')        
                b=8 # DATA da cotaÃ§Ã£o
                c=9 # VALOR da cotaÃ§Ã£o (fechado)
                d=10# VALOR minimo da integraÃ§Ã£o
                e=11# VALOR maximo da cotaÃ§Ã£o
                f=12# VALOR da variaÃ§Ã£o
                g=13# VARIAÃÃO em porcentagem
                h=14# VOLUME "transaÃ§Ãµes"
                print(dados)
                while(valida==True):
                        dados.append(a[b].text+";"+a[c].text+";"+a[d].text+";"+a[e].text+";"+a[f].text+";"+a[g].text+";"+a[h].text+'\n')
                        b=b+7
                        c=c+7
                        d=d+7
                        e=e+7
                        f=f+7
                        g=g+7
                        h=h+7
                        print(dados)
                        if(b<=337):
                                valida=False
                        cursor = connection.cursor()
                        cursor.execute(
                                "INSERT INTO bvzfdagnfqepipz70gyw.Valor_acoes(Value, IncDec, Variation) VALUES('%s', '%s', '%s')" % (
                                filtro1, filtro2, filtro3))
                        connection.commit()
                        connection.close()'''