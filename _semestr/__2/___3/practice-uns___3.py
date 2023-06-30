import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

R_1 = ufloat(0.570, 0.001)
L_1 = ufloat(165.0, 0.5)
m_1_0 = ufloat(22.229, 0.001)
m_1 = ufloat(72.470, 0.001)
h_1_1 = ufloat(5.02, 0.02)
h_1_2 = ufloat(15.92, 0.02)
t_1 = ufloat(170, 0.5)

rho_w = ufloat(997.66, 0)
g = ufloat(9.809980, 0)

R_1 = R_1 * 10**(-3)
L_1 = L_1 * 10**(-3)
m_1_0 = m_1_0 * 10**(-3)
m_1 = m_1 * 10**(-3)
h_1_1 = h_1_1 * 10**(-2)
h_1_2 = h_1_2 * 10**(-2)

n_1 = (np.pi * R_1**4 * rho_w**2 * g * (h_1_2 - h_1_1) * t_1) / (8 * (m_1 - m_1_0) * L_1)
print(n_1)

t_2_1 = ufloat(1082, 0)
t_2_2 = ufloat(663, 0)
t_2_3 = ufloat(1521, 0)

K_2 = ufloat(1.002 * 10**(-3), 0.007  * 10**(-3))

v_2_1 = K_2 * t_2_1
print(v_2_1)
v_2_2 = K_2 * t_2_2
print(v_2_2)
v_2_3 = K_2 * t_2_3
print(v_2_3)

m_2_0 = ufloat(20.392, 0.001)
m_2_i = ufloat(74.539, 0.001)
m_2 = ufloat(64.121, 0.001)
rho_2_v = ufloat(1.157, 0)

m_2_0 = m_2_0 * 10**(-3)
m_2_i = m_2_i * 10**(-3)
m_2 = m_2 * 10**(-3)

rho_2 = (rho_w - rho_2_v)*((m_2 - m_2_0)/(m_2_i - m_2_0)) + rho_2_v
print(rho_2)

m_3 = ufloat(38.1, 0.1)
m_3_i = ufloat(45.5, 0.1)

rho_3 = (m_3 / m_3_i) * rho_w
print(rho_3)

f_4 = ufloat(0.77, 0)
D_4 = ufloat(58.0, 0.1)
F_4_v = ufloat(35.10, 0.08)
F_4_m = ufloat(12.19, 0.07)

D_4 = D_4 * 10**(-3)

sigma_4_v = (F_4_v / (2 * np.pi * D_4)) * f_4
print(sigma_4_v)
sigma_4_m = (F_4_m / (2 * np.pi * D_4)) * f_4
print(sigma_4_m)