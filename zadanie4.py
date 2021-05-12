import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
df = pd.read_csv('iris.csv', names=['sepal len','sepal wid','petal len','petal wid', 'class'])
df = pd.DataFrame(df)
df = df[['sepal len','sepal wid', 'class']]
plt.xlabel('sepal length')
plt.ylabel('sepal width')
data = {'a': df['sepal len'],
        'b': df['sepal wid'],
        'c': np.random.randint(0, 150, 150)}
data['d'] = np.abs(data['a']-data['b'])
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.title('Iris sepal length and width')
plt.show()