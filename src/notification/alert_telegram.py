import telegram
from src.db.mysql_connection import connection,cursor
from src.charts.generate_charts import relat_diario
'''Para o funcionamento será necessario acionar o bot userinfobot no telegram do usuario para ter acesso ao CHAT_ID'''
id_colect=[]
id_chat=[]
x=0
try:
    cursor.execute("select id_chat from bvzfdagnfqepipz70gyw.Clientes")
    id_colect=cursor.fetchall()
    for linha in id_colect:
        id_chat.append(str(id_colect[x]).replace(',)','').replace('(',''))
        id_chat[x]=int(id_chat[x])
        x=x+1
    print("Todos os IDs foram coletado")
except:
    print("erro")
x=0
relat_diario()
for id in id_chat:
    chat_id=id_chat[x] #Vale lembrar que cada usuario de telegram tem o seu proprio chat_id e isso terá que ser cadastrado no DB
    bot=telegram.Bot(token='1019878731:AAFnpL9k8clpPiCKqjMPupMBihCbQSHG9hU')#Estamos identificando o bot reponsavel pelo envio da msg.
    bot.send_message(chat_id=chat_id, text="Estamos com bastante movimentação na ação, se eu fosse você acompanharia um pouco")
    bot.send_photo(chat_id=chat_id,photo=open('../charts/diario.png', 'rb'))
    print("Mensagem enviada com sucesso para o id: ", id_chat[x])
    x=x+1