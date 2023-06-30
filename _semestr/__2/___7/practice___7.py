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

c1 = pd.read_csv('data/c1.csv')
c2 = pd.read_csv('data/c2.csv')
c3 = pd.read_csv('data/c3.csv')

c1['h1_u'] = c1['h1'].apply(lambda x: ufloat(x, 0.3))
c1['h2_u'] = c1['h2'].apply(lambda x: ufloat(x, 0.3))

c1['kappa'] = c1['h1_u'] / (c1['h1_u'] - c1['h2_u'])

rho_1 = ufloat(997, 0)
g = ufloat(9.809980, 0)
p_0 = ufloat(97279.3, 0)

c1['kappa_u'] = (1/2) * ((c1['h1_u']*c1['h2_u']*rho_1 * g)/(p_0 * (c1['h1_u']-c1['h2_u'])))

I_0 = 4.05

c2['kappa'] = (c2['I1'] - I_0) / (c2['I1'] - c2['I2'])

l_1 = ufloat(26.8, 0.1)
l_2 = ufloat(20.4, 0.1)
l_3 = ufloat(15.7, 0.4)

f_1 = ufloat(638.48, 0.1)
f_2 = ufloat(843.55, 0.1)
f_3 = ufloat(1067.56, 0.1)

c_1 = 2 * l_1 * 10**(-2) * f_1
c_2 = 2 * l_2 * 10**(-2) * f_2
c_3 = 2 * l_3 * 10**(-2) * f_3

print(c_1)
print(c_2)
print(c_3)

rho_2 = ufloat(1.1564, 0)

k_1 = (c_1**2 * rho_2) / p_0
k_2 = (c_2**2 * rho_2) / p_0
k_3 = (c_3**2 * rho_2) / p_0

print(k_1)
print(k_2)
print(k_3)