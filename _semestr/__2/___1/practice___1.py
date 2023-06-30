import pandas as pd
import numpy as np
import uncertainties as u 
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

h = ufloat(15.250, 0.008)
D = ufloat(39.828, 0.007)
d = ufloat(10.056, 0.007)
m = ufloat(159.067, 0.001)

h = h * 10**(-3) 
D = D * 10**(-3)
d = d * 10**(-3)
m = m * 10**(-3)

rho = (4 * m) / (np.pi * (D**2 - d**2) * h)
print(rho)