import datetime
from twitter_scraper import get_tweets
from src.db.mysql_connection import cursor, connection
cursor.execute("SELECT DATA_ACAO FROM bvzfdagnfqepipz70gyw.Historico WHERE valor_variacao > 3 or valor_variacao<-3")
result=cursor.fetchall()
historico=[]
x=0
tweets=[]
try:
    while(x<=len(result)):
        historico.append(str(result[x]).replace('(datetime.date(','').replace('),)','').replace(' ','').replace(',','-'))
        print(datetime.datetime.strptime(historico[x],'%Y-%m-%d').date()," foi coletado")
        x=x+1
except:
    try:
        print('----------------------------------------------------------------')
        x=len(result)-1
        for colet in get_tweets('bancointer'):
            dcoleta = colet['time'].date()
            colet = colet['text']
            data=datetime.datetime.strptime(historico[x],'%Y-%m-%d').date()
            if (data > dcoleta):
                x = x - 1
            else:
                if(dcoleta==data):
                    print(dcoleta,colet)
                    tweets.append(colet)
                    print('arquivado')
                    x=x-1
    except:
        if(x<=0):
            print('Concluido')
            connection.close()