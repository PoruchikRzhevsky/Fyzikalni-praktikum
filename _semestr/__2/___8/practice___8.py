import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

b = ufloat(0.217, 0.002)

t = 1/b 
print(t)

d = ufloat(9.8 * 10 **(-2), 0.1 * 10 **(-2))
h = ufloat(19.7 * 10 **(-2), 0.2 * 10 **(-2))
m = ufloat(2.055, 0.002)

v = np.pi * (d/2)**2 * h
rho = m / v
print(rho)

m = ufloat(28.988 * 10 **(-3), 0.002 * 10 **(-3))
R = ufloat(0.570 * 10 **(-3), 0.006 * 10 **(-3))
L = ufloat(165.0 * 10 **(-3), 0.4 * 10 **(-3))
t = ufloat(163.19, 0.05)
h = ufloat(7.6 * 10 **(-2), 0.1 * 10 **(-2))
rho = 988.2
g = 9.81

n = ((np.pi * R**4 * h * rho**2 * g * t) / (8 * m * L)) * 10**3
print(n)

ch1_A = ufloat(3.6789705578188, 1.2697885827453*10**(-2))
ch1_B = ufloat(1.0088949125503*10**(3), 6.8769144055974*10**(-1))

ch2_A = ufloat(5.7802548464249, 1.2697885827453*10**(-2))
ch2_B = ufloat(9.9154740006834*10**(2), 2.4342116117969)

U_A = ufloat( 4.5259478809237*10**(-5), 1.9806681087018*10**(-7))
U_B = ufloat(-2.3374196976723*10**(-4), 1.0726892046856*10**(-5))

alpha_1 = ch1_A / ch1_B
print(alpha_1)
alpha_2 = ch2_A / ch2_B
print(alpha_2)

U_0 = ufloat(2.1953, 0)
alpha_coeff = ufloat(3.85*10**(-3), 0.04*10**(-3))

U_1 = ufloat(0.53822252*10**(3), 0)
U_2 = ufloat(-0.24239068*10**(3), 0)

dt_1 = (4 * U_1) / (alpha_coeff * U_0)
print(dt_1)
dt_2 = (4 * U_2) / (alpha_coeff * U_0)
print(dt_2)

epsilon_1 = (ufloat(620.7, 0.1) / ufloat(608.4, 0.1))**4
epsilon_2 = (ufloat(494.4, 0.1) / ufloat(662.8, 0.1))**4
epsilon_3 = (ufloat(648.1, 0.1) / ufloat(631.8, 0.1))**4
print(epsilon_1, epsilon_2, epsilon_3)

tau_1 = ufloat(507.1, 0.1)**4 / ufloat(550.2, 0.1)**4
tau_2 = ufloat(456.9, 0.1)**4 / ufloat(568.7, 0.1)**4
tau_3 = ufloat(444.3, 0.1)**4 / ufloat(536.3, 0.1)**4
tau_4 = ufloat(442.3, 0.1)**4 / ufloat(524.3, 0.1)**4
tau_5 = ufloat(455.2, 0.1)**4 / ufloat(527.1, 0.1)**4
tau_6 = (ufloat(302.1, 0.1)**4 - ufloat(298.4, 0.1)**4) / ufloat(579.7, 0.1)**4
tau_7 = (ufloat(300.8, 0.1)**4 - ufloat(298.4, 0.1)**4) / ufloat(574.3, 0.1)**4
tau_8 = (ufloat(298.1, 0.1)**4 - ufloat(298.4, 0.1)**4) / ufloat(556.2, 0.1)**4
tau_9 = (ufloat(299.4, 0.1)**4 - ufloat(298.4, 0.1)**4) / ufloat(530.2, 0.1)**4

print(tau_1)
print(tau_2)
print(tau_3)
print(tau_4)
print(tau_5)
print(tau_6)
print(tau_7)
print(tau_8)
print(tau_9)

print(ufloat(233.9, 0.1) + 273.15) 
print(ufloat(277, 0.1) + 273.15)
print(ufloat(183.6, 0.1) + 273.15) 
print(ufloat(295.5, 0.1) + 273.15)
print(ufloat(171.1, 0.1) + 273.15) 
print(ufloat(263.1, 0.1) + 273.15)
print(ufloat(169.1, 0.1) + 273.15) 
print(ufloat(251.1, 0.1) + 273.15)
print(ufloat(182, 0.1) + 273.15) 
print(ufloat(253.9, 0.1) + 273.15)
print(ufloat(28.9, 0.1) + 273.15) 
print(ufloat(306.5, 0.1) + 273.15)
print(ufloat(27.6, 0.1) + 273.15) 
print(ufloat(301.1, 0.1) + 273.15)
print(ufloat(24.9, 0.1) + 273.15)
print(ufloat(283, 0.1) + 273.15)
print(ufloat(26.2, 0.1) + 273.15)
print(ufloat(257, 0.1) + 273.15)
print(ufloat(25.3, 0.1) + 273.15)

epsilon_2_1 = (ufloat(253.6, 0.1) / ufloat(260.2, 0.1))**4
epsilon_2_2 = (ufloat(257.6, 0.1) / ufloat(271, 0.1))**4
print(epsilon_2_1)
print(epsilon_2_2)