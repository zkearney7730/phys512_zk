import numpy as np


def lorentz(x):
    lorentz.counter += 1
    return 1/(1+x**2)
lorentz.counter = 0

def integrate_adaptive(fun,x0,x1,tol,extra=None):
	print('')
	print('integrating between ',x0,x1)
    #hardwire to use simpsons
	npt= 5


    # for the first run evaluate the function
	if extra is None: 
		x_final=np.linspace(x0,x1,npt)
		y_final = fun(x_final)
		y = fun(x_final)
		extra =(x_final,y_final)
		print('first run')

	#for next few runs want to reuse function values 
	#for x values in the previous x 
	else: 
		y = np.empty([npt])
		y.fill(np.nan)
		x_new = np.linspace(x0,x1,npt)

		for i in range(npt):
			for j in range(npt):
				if extra[0][i] == x_new[j]:
					print('Repeated x value')
					y[j] = extra[1][i]

		#fill the values that didn't have from previous run 
		y[np.isnan(y)] = fun(x_new[np.isnan(y)])

		#add this round of x and y values to all previous ones
		xx = np.concatenate((extra[0],x_new))
		yy = np.concatenate((extra[1],y))

		extra = (xx,yy)


	dx=(x1-x0)/((npt)-1)
	area1=2*dx*(y[0]+4*y[2]+y[4])/3 #coarse step
	area2=dx*(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/3 #finer step
	err=np.abs(area1-area2)
	if err<tol:
		return area2
	else:
		xmid=(x0+x1)/2

		#next time calling the function include the x and y values used for the previous run
		left=integrate_adaptive(fun,x0,xmid,tol/2,extra=extra)
		right=integrate_adaptive(fun,xmid,x1,tol/2,extra=extra)
		return left+right


x0=-100
x1=100

ans=integrate_adaptive(lorentz,x0,x1,1e-7)
print('Difference', ans-(np.arctan(x1)-np.arctan(x0)))

print('number of function calls',lorentz.counter)


