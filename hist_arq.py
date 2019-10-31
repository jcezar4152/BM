from bs4 import BeautifulSoup
import requests
### as vareaveis abaixo são contadores para pegar a posição exata dos valores no html
b=8
c=9
d=10
e=11
f=12
g=13
h=14
diaI=input("Precisamos de um periodo para buscar o histrico, favor informar o dia inicial: ")
mesI=input("Informe o mês incial: ")
anoI=input("informe o ano inicial: ")
diaF=input("Favor informar o dia final: ")
mesF=input("Informe mês final: ")
anoF=input("Para finalizar, favor informar o ano final do periodo: ")
nav=requests.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay="+diaI+"&beginMonth="+mesI+"&beginYear="+anoI+"&endDay="+diaF+"&endMonth="+mesF+"&endYear="+anoF+"&size=200&page=1&period=")
html=nav.text
soup=BeautifulSoup(html,'html.parser')
a=soup.findAll('td')
arq=open('historico.csv','w')
valida=True
while(valida==True):
        arq.write(a[b].text+";"+a[c].text+";"+a[d].text+";"+a[e].text+";"+a[f].text+";"+a[g].text+";"+a[h].text+'\n')
        b=b+7
        c=c+7
        d=d+7
        e=e+7
        f=f+7
        g=g+7
        h=h+7
        ###Agora iremos alterar a pagina para pegar o restante dos dados, foi necessario zerar os contadores pois é "uma nova pagina".
        if(b==1401):
                arq.close()
                nav=requests.get("http://200.147.99.191/acao/cotacoes-historicas.html?codigo=BIDI4.SA&beginDay="+diaI+"&beginMonth="+mesI+"&beginYear="+anoI+"&endDay="+diaF+"&endMonth="+mesF+"&endYear="+anoF+"&size=200&page=2&period=")
                html=nav.text
                soup=BeautifulSoup(html,'html.parser')
                a=soup.findAll('td')        
                b=8
                c=9
                d=10
                e=11
                f=12
                g=13
                h=14
                arq=open('historico.csv','r')
                dados=arq.readlines()
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
                                print("Armazenando dados")
                                arq=open('historico2.csv','w')
                                valida=False
                                arq.writelines(dados)
