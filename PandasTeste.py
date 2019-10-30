import pandas as pd
import matplotlib.pyplot as plt
import pymysql


connection = pymysql.connect(host='bvzfdagnfqepipz70gyw-mysql.services.clever-cloud.com',
                                 port=3306,
                                 user='ufgpsjx1cswrmye3',
                                 password='ZoKM7HXwAaZAgd9ugpTr')


df = pd.read_sql("select * from test.uservitals", dbConnection)
#df = pd.read_csv('arq1.csv', sep=';')

plt.plot(df['Valor_total'], df['Valor_queda'])
plt.show()

connection.close()
