import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
excel = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(excel, header=0)
grupa1 = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa1.plot.bar()
plt.xlabel("Płeć")
plt.ylabel("Liczba")
plt.xticks(rotation=0)
plt.show()