import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

T_1 = ufloat(1.998, 0.008)
l_1 = ufloat(99.0, 0.3)

g_1 = (4 * (np.pi)**2 * l_1) / T_1**2
print(g_1)

M_2 = ufloat(1.5, 0)
m_2 = ufloat(38.3, 0)
p_2 = ufloat(8.19, 0)
d_2 = ufloat(50, 0)
r_2 = ufloat(46.5, 0)

m_2 = m_2 * 10**(-3)
p_2 = p_2 * 10**(-3)
d_2 = d_2 * 10**(-3)
r_2 = r_2 * 10**(-3)

J_2 = 2*m_2*((2/5)*(p_2**2) + (d_2**2))
print(J_2)

T_2 = ufloat(475, 2)

D_2 = ((2 * np.pi)/T_2)**2 * J_2
print(D_2)

L_2 = ufloat(5280, 3)
df = ufloat(177, 1)
ab = ufloat(612.1, 1)
df_2 = (df / ab) * 0.5
f_2 = (df_2 * 10**3) / L_2
print(f_2)
f_2_final = f_2 / 4
print(f_2_final)

M_2_gr = f_2_final * D_2
print(M_2_gr)

G_2 = M_2_gr / (2*(M_2*m_2)*d_2*((1/(r_2**2))-(r_2/((4*(d_2**2)+(r_2**2))**(3/2)))))
print(G_2)