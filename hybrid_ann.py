import numpy as np
from numpy import *
from scipy import interpolate
from scipy.interpolate import RectBivariateSpline

# repurpose logR, logP, & class probability data into a lookup table that can be interpolated
logR2 = []
logP2 = []
logR3 = []
logP3 = []
val2 = []
val3 = []
ann2 = loadtxt('ANN2_grid.dat')
ann3 = loadtxt('ANN3_Minner=1_grid.dat')

for row in ann2:
    logR2.append(row[0])
    logP2.append(row[1])
    val2.append(row[2])
for row in ann3:
    logR3.append(row[0])
    logP3.append(row[1]) 
    val3.append(row[2])

square2 = np.reshape(val2, (100,100))
square3 = np.reshape(val3, (100,100))

X2 = np.linspace(min(logR2),max(logR2),100)
Y2 = np.linspace(min(logP2),max(logP2),100)
X3 = np.linspace(min(logR3),max(logR3),100)
Y3 = np.linspace(min(logP3),max(logP3),100)

# create interpolant
f = RectBivariateSpline(X2,Y2,square2,ky=2,s=0)
g = RectBivariateSpline(X3,Y3,square3,ky=2,s=0) 

# log inputs, calculate M_inner, and feed into hybrid ANN equation
def output(N_inner, R, P):
    logR = np.log(R)
    logP = np.log(P)
    M_inner = min(N_inner - 1, 1)
    P_outer = (1 - M_inner) * f(logR,logP) + M_inner * g(logR,logP) 
    return P_outer

# a few interpolant test cases; note that inputs are unlogged for user convenience
P_outer3 = output(2, 4.214, 0.878)
P_outer2 = output(1, 0.975, 3.065)

#print P_outer3: yields 0.25242456
#print P_outer2: yields 0.08866211
#reference ANN3 and ANN2 results, respectively, to see that these are fairly accurate