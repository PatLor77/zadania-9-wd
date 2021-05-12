import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
x = np.arange(0,30,0.1)
sin = np.sin(x)
cos = np.cos(x)
plt.plot(x,sin,label='sin(x)')
plt.plot(x,cos,label='cos(x)')
plt.legend()
plt.show()