##############################
#####Problem 4, pset 1########
##############################

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

npt = 11
new_grid = 1001

#define x ranges
cos_xi = -np.pi/2
cos_xf = np.pi/2 
cos_x = np.linspace(cos_xi, cos_xf, npt)

Loren_xi = -1
Loren_xf = 1
Loren_x = np.linspace(Loren_xi,Loren_xf, npt)

#define functions 
def cos(x):
	return np.cos(x)

def Loren(x): 
	return 1/(1+x**2)

#polynomial interpolation
def poly_interp(func,x,xi,xf):

	poly_deg = 3
	polynomial_fit_coeff = np.polyfit(x, func, poly_deg)

	xx = np.linspace(xi, xf, new_grid)
	yy = np.polyval(polynomial_fit_coeff,xx)

	plt.scatter(x,func,marker='o',color='r')
	plt.plot(xx, yy, color ='k')
	#plt.plot(xx,np.cos(xx))
	plt.show()

	return yy

#cubic spline interpolation
def cs_interp(func,x,xi,xf):

	xx = np.linspace(xi,xf,new_grid)
	spln=interpolate.splrep(x,func)
	yy=interpolate.splev(xx,spln)

	plt.scatter(x,func,marker='o',color='r')
	plt.plot(xx, yy, color ='k')
	#plt.plot(xx,np.cos(xx))
	plt.show()

	return yy 

#rational function interpolation
def rational_interp(func,x, xi,xf):
	def rat_eval(p,q,x):
	    top=0
	    for i in range(len(p)):
	        top=top+p[i]*x**i
	    bot=1
	    for i in range(len(q)):
	        bot=bot+q[i]*x**(i+1)
	    return top/bot

	def rat_fit(x,y,n,m):
	    assert(len(x)==n+m-1)
	    assert(len(y)==len(x))
	    mat=np.zeros([n+m-1,n+m-1])
	    for i in range(n):
	        mat[:,i]=x**i
	    for i in range(1,m):
	        mat[:,i-1+n]=-y*x**i
	    pars=np.dot(np.linalg.inv(mat),y)
	    p=pars[:n]
	    q=pars[n:]
	    return p,q

	n=3
	m=4
	x_in=np.linspace(xi,xf,n+m-1)
	y_in=func(x_in)
	y = func(x)
	p,q=rat_fit(x_in,y_in,n,m)
	xx=np.linspace(xi,xf,new_grid)
	yy=rat_eval(p,q,xx)
	plt.scatter(x,y,marker='o',color='r')
	plt.plot(xx, yy, color ='k')
	#plt.plot(xx,np.cos(xx))
	plt.show()


poly_interp(cos(cos_x),cos_x,cos_xi,cos_xf)
poly_interp(Loren(Loren_x),Loren_x,Loren_xi,Loren_xf)

cs_interp(cos(cos_x),cos_x,cos_xi, cos_xf)
cs_interp(Loren(Loren_x),Loren_x,Loren_xi,Loren_xf)

rational_interp(np.cos, cos_x, cos_xi, cos_xf)
rational_interp(Loren, Loren_x,Loren_xi,Loren_xf)








