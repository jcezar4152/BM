import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arq1.csv', sep=';')

plt.plot(df['Hora'], df['Valor_total'])
plt.show()


