##############################
#####Problem 3, pset 1########
##############################


import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
from numpy import random 

data = np.loadtxt('lakeshore.txt')
V = np.array ([0.3,0.4,0.5,0.6])


def lakeshore(V, data):

	#make data frame of all input data and sort the voltage to smallest to largest 
	orig_data = pd.DataFrame(data={'temp_data':data[:,0], 'voltage_data':data[:,1], 'dV_dT_data':data[:,2]})
	sorted_data = orig_data.sort_values(by='voltage_data', ascending=True)
	npt =1001

	#test the interpolation function for a finer grid
	xx = np.linspace(sorted_data.voltage_data.min(), sorted_data.voltage_data.max(),npt)
	spln=interpolate.splrep(sorted_data.voltage_data, sorted_data.temp_data)
	yy=interpolate.splev(xx,spln)

	#interpolate for the given value of V
	temp_interp = interpolate.splev(V,spln)

	#error calculation 
	small = 25
	large = 119

	vol = np.array(sorted_data.voltage_data)
	temp = np.array(sorted_data.temp_data)


	#25 times do the interpolation on 4/5 of the numbers randomly 
	errors=[]
	for i in range(small):
		indices = list(range(sorted_data.voltage_data.size))
		#choose the indices randomly, ensure the voltage is increasing 
		interp_idx = random.choice(indices,size=large,replace=False)
		interp_idx.sort()

		#identify the indices of the numbers not chosen 
		to_check = [i for i in indices if not (i in interp_idx)]

		#do the interpolation for the chosen points 
		new_spln = interpolate.splrep(vol[interp_idx], temp[interp_idx])
		y_interp= interpolate.splev(vol[to_check],new_spln)
		y_real = temp[to_check]

		#save the difference between the interpolated y values and the known y values for the 25 x points
		errors.append(np.abs(y_interp - y_real))


	error = np.mean(errors) # Average all errors to get mean
	error_std = np.std(errors) # Take standard deviation for uncertainty on mean


	#check on graph 
	fig = plt.figure()
	plt.scatter(sorted_data.voltage_data,sorted_data.temp_data,marker='.', color='r',label='lakeshore values')
	plt.scatter(V,temp_interp,marker='o',color='b',label='New temperature values')
	plt.plot(xx,yy,color='k',label='Spline function fit')
	plt.xlabel('Voltage')
	plt.ylabel('Temperature')
	plt.legend()
	plt.show()


	return temp_interp,error, error_std 


temp_interp, error, error_std =lakeshore(V,data)

print("For voltage {} interpolated temperature values are {} with an average error on the interpolation of {}".format(V,temp_interp,error))
	




