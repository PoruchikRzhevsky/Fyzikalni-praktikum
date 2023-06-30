import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec
from scipy.interpolate import interp1d

A = pd.read_csv('data/MetodA.csv')
B = pd.read_csv('data/MetodB.csv')

fig, ax = plt.subplots(figsize=(10,10))

ax.grid()
ax.set_title('V-A characteristic')

ax.title.set_fontsize(20)
ax.set_xlabel('$U$ [V]')
ax.xaxis.label.set_fontsize(10)
ax.set_ylabel('$I$ [mA]')
ax.yaxis.label.set_fontsize(10)

ax.scatter(A['U'], A['I'],
           s=40, c='red', marker="v", label='Metoda A')
ax.plot(A['U'], A['I'], 
            c='red')

ax.scatter(B['U'], B['I'],
           s=20, c='blue', marker="s", label='Metoda B')
ax.plot(A['U'], A['I'], 
            c='blue')

legend = ax.legend(scatterpoints=1,markerscale = 1)
frame = legend.get_frame()
frame.set_facecolor('0.90')

plt.show() 
fig.savefig('plots/V-A.png', bbox_inches='tight') 

