##############################
#####Problem 2, pset 1########
##############################
import numpy as np


x = 5
def ndiff(func, x, full=False):
	eps = 2**-52
	dx = eps**(1/3) #approximate dx

	x1 = x+dx
	dx = x1-x

	deriv = (func(x+dx)-func(x-dx))/(2*dx) #use a centered derivative 
	total_err = ((func(x)*eps) / (12*dx) )+ dx**2
	frac_err = total_err/deriv *100

	if full == False: 
		return deriv 
	else: 
		return deriv, dx, frac_err


#can use an integer or an array for x 
deriv,dx,frac_err = ndiff(np.exp, x, full=True)
print( 'The derivative approximation is:', deriv, 'with dx value of:',dx,'and a fractional error of',frac_err)