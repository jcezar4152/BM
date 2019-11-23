from src.db.mysql_connection import connection, cursor
def cad_cliente():
    with connection:
        nome=input("Qual o seu nome completo? ").upper()
        email=input("Informe seu email: ").upper()
        id_chat=int(input("Iforme o ID do telegram: "))
        try:
            cursor.execute("INSERT INTO bvzfdagnfqepipz70gyw.Clientes(nome, email, id_chat,gold) VALUES('%s', '%s', %d,NULL)"%(nome , email , id_chat))
            connection.commit()
            print("Usuario cadastrado com sucesso")
        except:
            print("Já existe um usuario com o email informado")
    connection.close()