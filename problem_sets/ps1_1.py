##############################
#####Problem 1, pset 1########
##############################

import numpy as np


x = 5
eps = 2**-52
dx = eps**(1/5)

x1 = x+dx
x2 = x-dx 
x3 = x+2*dx
x4 = x-2*dx

dx = x1-x

f = np.exp(x)
f1 = np.exp(x1) 
f2 = np.exp(x2) 
f3 = np.exp(x3) 
f4 = np.exp(x4) 

deriv = (8*f1-8*f2-f3+f4)/ (12*dx)
print('derivative is ',deriv,' with fractional error ',deriv/f-1)

f = np.exp(0.01*x)
f1 = np.exp(0.01*x1) 
f2 = np.exp(0.01*x2) 
f3 = np.exp(0.01*x3) 
f4 = np.exp(0.01*x4) 
	
deriv = (8*f1-8*f2-f3+f4)/ (12*dx)
print('derivative is ',deriv,' with fractional error ',deriv/f-1)



