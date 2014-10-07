'''
@Author YTang  10/09/2014
In class Exercise on Derivatives and Euler's Method

Part I
Use Forward Difference and Central Difference to find the derivative of f(x)=x**3-sin(x) at x=2. Calculate the relative error and find the smallest error that you can obtain. 

Part II
At t=1.5, find the force exerted on a box m=0.8kg, which position is changing as: x(t)=3*t**2-2t+1 

#Part III
#Use Euler Method to find x(t), where dx/dt = -x**3 + x*sin(t)+1 with initial condition: x=0 at t=0. 
'''

import numpy as np
import pylab as pl

#define a function for Part I
def f1(x):
    return x**3 - np.sin(x)

#define a function for Part II
def f2(x):
    return 3*x**2-2*x+1
    
#define a function for Part III
def f3(x, t):
    return -x**3+x*np.sin(t)+1
    
def ForwardDiff(f, x, h):
    devf = f(x+h)-f(x)
    devf /= h
    return devf
 
def CentralDiff(f, x, h):
    devf = f(x+h/2)-f(x-h/2)
    devf /= h  
    return devf 
    
def SecondDerivative(f, x, h):
    devf = f(x+h)-2*f(x)+f(x-h)
    devf /= h*h
    return devf

#exact values of part I and part II
exact_f1 = 3*2.0**2 - np.cos(2)
exact_f2 = 6.0*0.8


#part I, use forward and central derivative to compute 
print "~~~~Part I~~~~"
h = 0.000001
#forward diffence, (function, x position, step size)
print "step size: %2.18f \n" %h
print 'Forward Difference'
devf = ForwardDiff(f1, 2.0, h)
print "calculated derivative: %2.18f, exact derivative: %2.18f \nError %2.18f, relative error %2.18f \n"  %(devf, exact_f1, devf-exact_f1, (devf-exact_f1)/exact_f1)

print 'Central Difference'
#central difference
devf = CentralDiff(f1, 2.0, h)
print "calculated derivative: %2.18f, exact derivative: %2.18f \nError %2.18f, relative error %2.18f \n"  %(devf, exact_f1, devf-exact_f1, (devf-exact_f1)/exact_f1)

#Part II, use second derivative to compute force
print "~~~~Part II~~~~"
h=0.00001
mass = 0.8
secDevf=SecondDerivative(f2, 1.5, h)
force = secDevf*mass
print "The force on the box is: %2.18f, the exact value is %2.18f \nError %2.18f, relative error %2.18f \n" %(force, exact_f2, force-exact_f2, (force-exact_f2)/exact_f2)

#Part III, use Euler method to find the solution for differential eq: 
#dx/dt = -x**3 + x*sin(t)+1
print "~~~~Part III~~~~"
a=0.0    #left boundary
b=10.0   #right boundary
N=1000   #step number
h = (b-a)/N #step size
x = 0.0  #initial value of x 

tpoints = np.arange(a,b,h) #divide range [a,b] evenly by step size h
xpoints = []

for t in tpoints: 
    xpoints.append(x)
    x += h*f3(x,t) #update x for each step

#plot the solution
pl.plot(tpoints, xpoints)
pl.xlabel("t", fontsize=20)
pl.ylabel("x(t)", fontsize=20)
pl.text(4.0, 0.2, 'dx(t)/dt = -x^3+xsin(t)+1', fontsize=15) #write down the ODE on the figure
pl.show()

