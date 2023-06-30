import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec
from scipy import interpolate, integrate

temp = pd.read_csv('data/temp.csv')

temp['tk'] = (temp['tk_1'] + temp['tk_2']) / 2 
temp['t0'] = (temp['t0_1'] + temp['t0_2']) / 2 
temp['tk-t0'] = temp['tk'] - temp['t0']

fig, ax = plt.subplots(figsize=(10,10))

ax.grid()
ax.set_title('Závislost rozdílu teplot na čase')

ax.title.set_fontsize(20)
ax.set_xlabel(r'$\tau$ [s]')
ax.xaxis.label.set_fontsize(10)
ax.set_ylabel('$t_k-t_0$ [°C]')
ax.yaxis.label.set_fontsize(10)
ax.axhline(y=0, c="red", label="$t_k-t_0$ = 0")
plt.xlim([0, 1400])

ax.scatter(temp['tau'], temp['tk-t0'],
           s=3, c='blue', marker="s", label='Výsledná hodnota rozdílu teplot')

ax.fill_between(temp['tau'],temp['tk-t0'],
           color= "red", alpha= 0.2)

legend = ax.legend(scatterpoints=1,markerscale = 1)
frame = legend.get_frame()
frame.set_facecolor('0.90')

plt.show() 
fig.savefig('plots/temp.png', bbox_inches='tight') 

f = interpolate.interp1d(temp['tau'], temp['tk-t0'], kind='cubic', bounds_error=False)

def integrand(x):
    return f(x)
    
result = integrate.quad(integrand, 1.22566, 1140.88)
print(result)

print(f(1140.88))
print(f(1.22566))

m_0 = ufloat(241.1, 0.03)
m_1 = ufloat(499.5, 0.03) - m_0
m_2 = ufloat(499.9, 0.03) - m_0
t_1 = ufloat(19.4, 0.03)
t_2 = ufloat(29.9, 0.03)
t = ufloat(24.4, 0.03)
c = ufloat(4.19, 0)

k = ((m_2*(t_2-t))/(t-t_1)) - m_1
print(k)

K = k * c
print(K)

m = ufloat(576.8, 0.04)
tau = ufloat(1334.4, 0.03)
P = ufloat(30.3, 0)
dt = ufloat(15.8, 0.04)

print((m*c + K)*dt ,'=', P*tau)
print(np.mean(temp['t0']))
print((m*c + K)*dt - P*tau) 

c_2 = (((P*tau)/(dt)) - K)/m
print(c_2)