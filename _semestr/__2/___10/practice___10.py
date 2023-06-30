import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

U_1 = ufloat(20.606, 0.04)
U_2 = ufloat(26.318, 0.05)
I_1 = ufloat(1.026, 0.003)
I_2 = ufloat(1.31, 0.003)

P_1 = U_1 * I_1
P_2 = U_2 * I_2
print(P_1, P_2)

k = ufloat(3.7481259370315 * 10**(-1), 1.3671848731790 * 10**(-2))
a = ufloat(20.3 * 10**(-2), 0.2 * 10**(-2))
b = ufloat(21.3 * 10**(-2), 0.1 * 10**(-2))
d = ufloat(12.6 * 10**(-3), 0.03 * 10**(-3))

lam = d / (a*b*k*2)
print(lam)