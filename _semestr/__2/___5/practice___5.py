import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

k_1plus = ufloat(4.7538165901965*10**(-4),  2.9794349869204*10**(-6))
k_1minus = ufloat(4.7664667377935*10**(-4),  5.4479069915030*10**(-6))

k_1final = (k_1plus + k_1minus) / 2

print(k_1final)

g = ufloat(9.809980, 0)
l_1 = ufloat(1565, 0)
d_1 = ufloat(0.50, 0.01)
k_1final_new = ufloat(4760*10**(-7), 120*10**(-7))

l_1 = l_1 * 10**(-3)
d_1 = d_1 * 10**(-3)

E_1 = (4*g*l_1)/(np.pi*(d_1**2)*k_1final_new)

print(E_1)

k_2_1plus = ufloat(2.7321414396821*10**(-3),  6.1154451675715*10**(-7))
k_2_1minus = ufloat(2.7340466541304*10**(-3),  7.2165633954165*10**(-7))

k_2_1final = (k_2_1plus + k_2_1minus) / 2

print(k_2_1final)

l_2 = ufloat(899.2, 1)
h_2_1 = ufloat(4.99, 0.01)
w_2_1 = ufloat(28.45, 0.05)
k_2_1final_new = ufloat(27331*10**(-7), 21*10**(-7))

l_2 = l_2 * 10**(-3)
h_2_1 = h_2_1 * 10**(-3)
w_2_1 = w_2_1 * 10**(-3)

E_2_1 = (g * ((l_2)**3)) / (4 * ((h_2_1)**3) * w_2_1 * k_2_1final_new)
print(E_2_1)

k_2_2plus = ufloat(4.7727484765013*10**(-3),  1.7774045017633*10**(-7))
k_2_2minus = ufloat(4.7790613353523*10**(-3),  3.6645865967836*10**(-7))

k_2_2final = (k_2_2plus + k_2_2minus) / 2
print(k_2_2final)

h_2_2 = ufloat(4.99, 0.02)
w_2_2 = ufloat(28.44, 0.08)
k_2_2final_new = ufloat(47759*10**(-7), 8*10**(-7))

h_2_2 = h_2_2 * 10**(-3)
w_2_2 = w_2_2 * 10**(-3)

E_2_2 = (g * ((l_2)**3)) / (4 * ((h_2_2)**3) * w_2_2 * k_2_2final_new)
print(E_2_2)

D_3 = ufloat(97.729, 0.524)
l_3 = ufloat(523.6, 2)
d_3 = ufloat(0.997, 0.012)
T_3 = ufloat(40.544, 2)
m_3 = ufloat(5905, 0)

R_3 = (D_3 / 2) * 10**(-3)
l_3 = l_3 * 10**(-3)
r_3 = (d_3 / 2) * 10**(-3)
T_3 = T_3 / 10
m_3 = m_3 * 10**(-3)

print(R_3)
print(r_3)
print(T_3)

G = (16 * np.pi * m_3 * ((R_3)**2) * l_3) / (5 * ((r_3)**4) * ((T_3)**2))
print(G)