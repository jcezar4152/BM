import pandas as pd
import matplotlib.pyplot as plt
from src.db.mysql_connection import connection
def relat_diario():
    with connection:
        df = pd.read_sql("select * from bvzfdagnfqepipz70gyw.Valor_acoes where date_format(data_coleta, '%Y-%m-%d')=date_format(NOW(), '%Y-%m-%d')",connection)# faz um select na tabela
        pd.plotting.register_matplotlib_converters()
        plt.plot(df['data_coleta'], df['Value'])  # seleciona as colunas para mostrar no gráfico
        # plt.show()
        plt.savefig('diario.png')

def relat_historico():
    with connection:
        df = pd.read_sql("select * from bvzfdagnfqepipz70gyw.Historico", connection)  # faz um select na tabela
        pd.plotting.register_matplotlib_converters()
        plt.plot(df['data_acao'], df['valor_fechado'])  # seleciona as colunas para mostrar no gráfico
        # plt.show()
        plt.savefig('historico.png')
relat_historico()