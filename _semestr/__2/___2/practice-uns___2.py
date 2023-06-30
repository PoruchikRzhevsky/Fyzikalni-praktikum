import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

U_1_A = ufloat(5.35, 0.007)
U_2_A = ufloat(19.31, 0.08)
I_1_A = ufloat(54.5, 0.09)
I_2_A = ufloat(21*10**(-3), 0.08*10**(-3))

U_1_B = ufloat(5.31, 0.007)
U_2_B = ufloat(17.78, 0.08)
I_1_B = ufloat(53.0, 0.09)
I_2_B = ufloat(17*10**(-3), 0.08*10**(-3))

R_V = ufloat(10**7, 0)
R_A = ufloat(1, 0)

I_1_A = I_1_A * 10**(-3)
I_2_A = I_2_A * 10**(-3)
I_1_B = I_1_B * 10**(-3)
I_2_B = I_2_B * 10**(-3)

R_1_A = U_1_A / I_1_A
print(R_1_A)
R_1_A_correct = U_1_A / (I_1_A - (U_1_A / R_V))
print(R_1_A_correct)

R_2_A = U_2_A / I_2_A
print(R_2_A)
R_2_A_correct = U_2_A / (I_2_A - (U_2_A / R_V))
print(R_2_A_correct)

R_1_B = U_1_B / I_1_B
print(R_1_B)
R_1_B_correct = (U_1_B / I_1_B) - R_A
print(R_1_B_correct)

R_2_B = U_2_B / I_2_B
print(R_2_B)
R_2_B_correct = (U_2_B / I_2_B) - R_A
print(R_2_B_correct)