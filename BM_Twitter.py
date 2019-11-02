from twitter_scraper import get_tweets
import datetime
import pymysql
#Consultar variação (gatilho):
connection = pymysql.connect(host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com',
                                 port=3306,
                                 user='ufgpsjx1cswrmye3',
                                 password='ZoKM7HXwAaZAgd9ugpTr')
cursor = connection.cursor()
cursor.execute("SELECT DATA_ACAO FROM bvzfdagnfqepipz70gyw.Historico WHERE data_acao='2019-10-31'")
data_acao=cursor.fetchone()
data=str(data_acao)
data=data.replace(' ','')
count=len(data)
#historico=[]
if(count==28):
    data=data[15:25]
    data=data.replace(',','-')
    data=datetime.datetime.strptime(data,'%Y-%m-%d')
    #historico.append(data)
else:
    if(count==27):
        data = data[15:24]
        data = data.replace(',', '-')
        data = datetime.datetime.strptime(data, '%Y-%m-%d')
        #historico.append(data)
    else:
        if(count==26):
            data = data[15:23]
            data = data.replace(',', '-')
            data = datetime.datetime.strptime(data, '%Y-%m-%d')
            #historico.append(data)
#Recebendo a data
for colet in get_tweets('bancointer'):
    CD = colet['time'].date()
    colet = colet['text']
    if(CD==data.date()):
        print(CD,colet)