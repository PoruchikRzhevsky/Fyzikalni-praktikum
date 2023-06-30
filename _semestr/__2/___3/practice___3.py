import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec
from scipy.interpolate import interp1d

ubb = pd.read_csv('data/ubb.csv')
ubb_t = pd.read_csv('data/ubb_t.csv')

fig, ax = plt.subplots(figsize=(10,10))

ax.grid()
ax.set_title('Závislost viskozity na teplotě')

ax.title.set_fontsize(20)
ax.set_xlabel('$T$ [°C]')
ax.xaxis.label.set_fontsize(10)
ax.set_ylabel(r'$\nu$ [$\frac{mm^2}{s^2}$]')
ax.yaxis.label.set_fontsize(10)

ax.scatter(ubb['T'], ubb['v'],
           s=40, c='red', marker="v", label='Naměřené hodnoty')
ax.plot(ubb['T'], ubb['v'], 
            c='blue')

legend = ax.legend(scatterpoints=1,markerscale = 1)
frame = legend.get_frame()
frame.set_facecolor('0.90')

plt.show() 
fig.savefig('plots/Vis.png', bbox_inches='tight') 

