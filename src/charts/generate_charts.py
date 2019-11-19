import pandas as pd
import matplotlib.pyplot as plt
from db.mysql_connection import connection

df = pd.read_sql("select * from bvzfdagnfqepipz70gyw.Historico", connection) #faz um select na tabela

pd.plotting.register_matplotlib_converters()
plt.plot(df['data_acao'], df['valor_fechado']) #seleciona as colunas para mostrar no gráfico
#plt.show()
plt.savefig('diario.png')

connection.close()
