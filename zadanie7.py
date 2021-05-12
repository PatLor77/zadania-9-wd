import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
csv = pd.read_csv('zamowienia.csv',sep=';')
sumy = csv.groupby(['Sprzedawca']).agg({'Utarg':['sum']})
suma_og = sum(csv['Utarg'])
sumy = (sumy/suma_og)*100
sumy = round(sumy)
plt.show()