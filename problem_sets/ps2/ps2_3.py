import numpy as np
from numpy.polynomial import chebyshev
import matplotlib.pyplot as plt 


##########################
#Do chebyshev fit for log2 

x = np.linspace( 0.5,0.9999,1000)
y_orig = np.log2(x)

#split up x to mantiss (m) and exponent (n)
##adjusts the x scale to fit the full range of the chebyshev polynomials
m,n = np.frexp(x)
y = n + np.log2(m)


#obtain coefficients for the chebyshev polynomials
#and fit it to the data
order = 10
cc =chebyshev.chebfit(x,y,deg=order)
cc[np.abs(cc)<1e-5] = 0
fit = chebyshev.chebval(m,cc)

#plot original and the fit 
plt.scatter(x,y_orig,color='k',label='True values')
plt.plot(x,fit,color='r',label='Chebyshev fit of order {}'.format(order))
plt.ylabel('log2(x)')
plt.xlabel('x')
plt.legend()
plt.show()

#plot residuals
plt.scatter(x, (y_orig-fit),color='k',label='residuals')
plt.xlabel('x')
plt.legend()
plt.show()

############################
#create function for ln(x)

def mylog2(x):
	m,n = np.frexp(x)
	a,b = np.frexp(np.e)

	fit = chebyshev.chebval(m,cc)
	fit_e = chebyshev.chebval(a,cc)
	ln = (n+fit)/(b+fit_e)

	return ln

#graph original and fit 
x_check = np.linspace(0.5,3,100)
y = mylog2(x_check)
y_true = np.log(x_check)

plt.scatter(x_check,y,color='k',label='True value')
plt.plot(x_check,y_true,color='r',label='Chebyshev fit of order {}'.format(order))
plt.ylabel('ln(x)')
plt.xlabel('x')
plt.legend()
plt.show()



