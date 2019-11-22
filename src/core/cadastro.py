from src.db.mysql_connection import connection, cursor
nome='JULIO CEZAR LIMA DE FIGUEREDO'#input("Qual o seu nome completo? ")
email='J.CEZAR4152@GMAIL.COM' #input("Informe seu email: ")
id_chat=958967767 #int(input("Iforme o ID do telegram: "))
gold='0'
cursor.execute("INSERT INTO bvzfdagnfqepipz70gyw.Clientes(nome, email, id_chat,gold) VALUES('%s', '%s', %d,%s)"%(nome , email , id_chat,gold))
print("Usuario cadastrado com sucesso")
connection.close()