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
		x_comp =np.linspace(x0,x1,npt)
		y = fun(x_comp)
		print('first run')

	#for next few runs want to reuse function values 
	#for x values in the previous x 
	else: 
		y = np.empty([npt])
		y.fill(np.nan)
		x_comp = np.linspace(x0,x1,npt)

		for i in range(npt):
			for j in range(npt):
				if extra[0][i] == x_comp[j]:
					print(i,j,extra[0][i],x_comp[j])
					print('Repeated x value')
					y[j] = extra[1][i]
				else:
					print('new y')

		#fill the values that didn't have from previous run 
		print(np.isnan(y))
		y[np.isnan(y)] = fun(x_comp[np.isnan(y)])


	dx=(x1-x0)/(len(x_comp)-1)
	area1=2*dx*(y[0]+4*y[2]+y[4])/3 #coarse step
	area2=dx*(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/3 #finer step
	err=np.abs(area1-area2)
	#print('err', err)
	if err<tol:
		return area2
	else:
		xmid=(x0+x1)/2
		#next time calling the function include the x and y values used for the previous run
		left=integrate_adaptive(fun,x0,xmid,tol/2,extra=(x_comp,y))
		right=integrate_adaptive(fun,xmid,x1,tol/2,extra=(x_comp,y))
		return left+right


x0=-100
x1=100

ans=integrate_adaptive(lorentz,x0,x1,1e-7)
print(ans-(np.arctan(x1)-np.arctan(x0)))

print(lorentz.counter)


