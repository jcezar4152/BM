import telegram
'''Para o funcionamento será necessario acionar o bot userinfobot no telegram do usuario para ter acesso ao CHAT_ID'''
chat_id=958967767 #vale lembrar que cada usuario de telegram tem o seu proprio chat_id e isso terá que ser cadastrado no DB
bot=telegram.Bot(token='1019878731:AAFnpL9k8clpPiCKqjMPupMBihCbQSHG9hU')#Estamos identificando o bot reponsavel pelo envio da msg.
bot.send_message(chat_id=chat_id, text="Estamos com bastante movimentação na ação, se eu fosse você acompanharia um pouco")
bot.send_photo(chat_id=chat_id,photo=open('telegram_notfy/diario.jpg', 'rb'))