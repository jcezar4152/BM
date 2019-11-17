import mysql.connector
import datetime
from twitter_scraper import get_tweets
mydb = mysql.connector.connect(
     host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com',
     port=3306,
     user='ufgpsjx1cswrmye3',
     password='ZoKM7HXwAaZAgd9ugpTr')
cursor=mydb.cursor()
cursor.execute("SELECT DATA_ACAO FROM bvzfdagnfqepipz70gyw.Historico WHERE valor_variacao > 3 or valor_variacao<-3")
result=cursor.fetchall()
historico=[]
x=0
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
            #print(data,' ',dcoleta)
            #print(x)
            if (data > dcoleta):
                x = x - 1
            else:
                if(dcoleta==data):
                    print(dcoleta,colet)
                    x=x-1
    except:
        if(x<=0):
            print('Concluido')