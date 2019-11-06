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
        x=x+1
        print(x,"° data coletada")
except:
    x=0
    for colet in get_tweets('bancointer'):
        dcoleta = colet['time'].date()
        colet = colet['text']
        if(dcoleta==datetime.datetime.strptime(historico[x], '%Y-%m-%d').date):
            print(colet)
            x=x+1