import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

I_1 = ufloat(100*10**(-6), 1.5*10**(-6))
U_1 = ufloat(158.04*10**(-3), 0.07*10**(-3))

R_1 = U_1 / (I_1)
print(R_1)

R_B_1 = (R_1 * I_1) / (0.5002*10**(-3))
R_B_2 = (R_1 * I_1) / (1.0006*10**(-3))
R_B_3 = (R_1 * I_1) / (1.5002*10**(-3))
R_B_4 = (R_1 * I_1) / (2*10**(-3))
print(R_B_1)
print(R_B_2)
print(R_B_3)
print(R_B_4)

R_P_1 = ((5 / U_1) - 1) * R_1
R_P_2 = ((10 / U_1) - 1) * R_1
print(R_P_1)
print(R_P_2)

print((10.7 - 10.696812 - (-10.7 + 10.674076)) / 21.4)