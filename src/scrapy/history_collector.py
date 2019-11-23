from bs4 import BeautifulSoup
import requests
import datetime
from src.db.mysql_connection import cursor,connection
### as vareaveis abaixo sÃ£o contadores para pegar a posiÃ§Ã£o exata dos valores no html
def colet_history():
        b=8
        c=9
        d=10
        e=11
        f=12
        g=13
        h=14
        hoje=datetime.date.today()
        nav=requests.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay="+str(hoje.day)+"&beginMonth="+str(hoje.month)+"&beginYear="+str(hoje.year-1)+"&endDay="+str(hoje.day)+"&endMonth="+str(hoje.month)+"&endYear="+str(hoje.year)+"&size=200&page=1&period=")
        html=nav.text
        soup=BeautifulSoup(html,'html.parser')
        a=soup.findAll('td')
        valida=True
        while(valida==True):
                try:
                        data_acao=a[b].text
                        data_acao=data_acao.replace('/','-')
                        data_acao=datetime.datetime.strptime(data_acao,'%d-%m-%Y')

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

                        volume=a[h].text.replace(".","")
                        volume=int(volume)
                        try:
                                cursor.execute(
                                        "INSERT INTO bvzfdagnfqepipz70gyw.Historico(data_acao, valor_fechado, valor_minimo, valor_maximo, valor_variacao, variacao_porc, volume) VALUES('%s', '%f', '%f','%f','%f','%f','%f')"%(data_acao,valor_fechado,valor_minimo,valor_maximo,valor_variacao,valor_porc,volume))
                                connection.commit()
                                print(data_acao,"Inserido com sucesso")
                        except:
                                print(data_acao,"Já existe")
                        b=b+7
                        c=c+7
                        d=d+7
                        e=e+7
                        f=f+7
                        g=g+7
                        h=h+7
                        print(b)
                        ###Agora iremos alterar a pagina para pegar o restante dos dados, foi necessario zerar os contadores pois Ã© "uma nova pagina".
                except:
                        print("Primeira pagina OK")
                        nav=requests.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay="+diaI+"&beginMonth="+mesI+"&beginYear="+anoI+"&endDay="+diaF+"&endMonth="+mesF+"&endYear="+anoF+"&size=200&page=2&period=")
                        html=nav.text
                        soup=BeautifulSoup(html,'html.parser')
                        a=soup.findAll('td')
                        b=8 # DATA da cotacao
                        c=9 # VALOR da cotacao (fechado)
                        d=10# VALOR minimo da integracao
                        e=11# VALOR maximo da cotacao
                        f=12# VALOR da variacao
                        g=13# VARIACAO em porcentagem
                        h=14# VOLUME "transacoes"
                        while(valida==True):
                                try:
                                        data_acao = a[b].text
                                        data_acao = data_acao.replace('/', '-')
                                        data_acao = datetime.datetime.strptime(data_acao, '%d-%m-%Y')

                                        valor_fechado = a[c].text.replace(",", ".")
                                        valor_fechado = float(valor_fechado)

                                        valor_minimo = a[d].text.replace(",", ".")
                                        valor_minimo = float(valor_minimo)

                                        valor_maximo = a[e].text.replace(",", ".")
                                        valor_maximo = float(valor_maximo)

                                        valor_variacao = a[f].text.replace(",", ".")
                                        valor_variacao = float(valor_variacao)

                                        valor_porc = a[g].text.replace(",", ".")
                                        valor_porc = float(valor_porc)

                                        volume = a[h].text.replace(".", "")
                                        volume = int(volume)
                                        try:
                                                cursor.execute(
                                                        "INSERT INTO bvzfdagnfqepipz70gyw.Historico(data_acao, valor_fechado, valor_minimo, valor_maximo, valor_variacao, variacao_porc, volume) VALUES('%s', '%f', '%f','%f','%f','%f','%f')"%(data_acao,valor_fechado,valor_minimo,valor_maximo,valor_variacao,valor_porc,volume))
                                                connection.commit()
                                                print(data_acao,"Inserido com sucesso")
                                        except:
                                                print(data_acao,"Já existe")
                                        b=b+7
                                        c=c+7
                                        d=d+7
                                        e=e+7
                                        f=f+7
                                        g=g+7
                                        h=h+7
                                        print(b)
                                except:
                                        valida=False
        connection.close()