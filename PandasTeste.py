import pandas as pd
import matplotlib.pyplot as plt
import pymysql


connection = pymysql.connect(host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com', #abre conexão com o banco
                                 port=3306,
                                 user='ufgpsjx1cswrmye3',
                                 password='ZoKM7HXwAaZAgd9ugpTr')


df = pd.read_sql("select * from bvzfdagnfqepipz70gyw.Historico", connection) #faz um select na tabela

pd.plotting.register_matplotlib_converters()
plt.plot(df['data_acao'], df['valor_fechado']) #seleciona as colunas para mostrar no gráfico
#plt.show()
plt.savefig('/Users/Aluno/Desktop/Informatica/Python 3.7/webbot_blackmamba/diario.png')

connection.close()
