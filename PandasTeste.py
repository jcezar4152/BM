import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arq1.csv', sep=';')

plt.plot(df['Valor_total'], df['Valor_queda'])
plt.show()
