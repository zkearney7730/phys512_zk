
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt 


#set up problem 
R_val = 5 
sig= 0.01
delt = 0.003631
epsilon0 = 8.854187817e-12
front = (2*np.pi*R_val**2*sig)/(4*np.pi*epsilon0)

#integral to solve 
def fun(u,z,R):
	intgrl = (z-R*u)/((R**2+z**2-2*R*z*u)**(3/2))
	return intgrl

#z values greater than and less than the radius of the sphere 
z_in = np.linspace(0,R_val-0.1,25)
z_out = np.linspace(R_val+0.1,10,25)


######################
#First use Simpsons integrator 
def simps(fun,z,R,x0,x1,tol):
    print('integrating between ',x0,x1)
    #hardwire to use simpsons
    x=np.linspace(x0,x1,5)
    y=fun(x,z,R)
    dx=(x1-x0)/(len(x)-1)
    area1=2*dx*(y[0]+4*y[2]+y[4])/3 #coarse step
    area2=dx*(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/3 #finer step
    err=np.abs(area1-area2)
    if err<tol:
        return area2
    else:
        xmid=(x0+x1)/2
        left=simps(fun,z,R,x0,xmid,tol/2)
        right=simps(fun,z,R,xmid,x1,tol/2)
        return left+right

#Calculate the E field inside and outside sphere
E_in= []
E_out= []
for i in range(25):
	E_in.append(simps(fun,z_in[i],R_val,-1, 1,1e-7))
	E_out.append(simps(fun, z_out[i],R_val,-1, 1,1e-7))

#plot
plt.plot(z_in, E_in, color ='k',label='$z<R$')
plt.plot(z_out,E_out,color='r',label='$z>R$')
plt.vlines(5,ymin=0,ymax=E_out[0], linestyle='--', color='k')
plt.legend() 
plt.xlabel('$z$')
plt.ylabel('${E}$ field')
plt.title('Simpons Integrator')
plt.show() 


#######################
#use quad 
E_in= []
E_out= []
for i in range(25):

	E_in.append(quad(fun, -1, 1, args=(z_in[i],R_val))[0])
	E_out.append(quad(fun, -1, 1, args=(z_out[i],R_val))[0])

E_surface =quad(fun, -1,1, args=(R_val+delt,R_val))[0]

plt.plot(z_in, E_in, color ='k',label='$z<R$')
plt.plot(z_out,E_out,color='r',label='$z>R$')
plt.vlines(5,ymin=0,ymax=E_surface, linestyle='--', color='k')
plt.scatter(R_val+delt,E_surface,marker='o',color='b',label='$z=R$' )
plt.legend() 
plt.xlabel('$z$')
plt.ylabel('${E}$ field')
plt.title('Quad Integrator')
plt.show() 




