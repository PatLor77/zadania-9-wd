import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
x = np.arange(0,30,0.1)
sin = np.sin(x)
cos = np.cos(x)
sin2 = np.sin(x+np.pi)
plt.title('Wykres sin(x), sin(x)')
plt.ylabel("sin(x)")
plt.xlabel("X")
plt.plot(x,sin2)
plt.plot(x,sin+2)
plt.show()