''' 
MC simulation of gas. 

Adopted from M. Newman's text book
'''
import random
from math import exp,pi
import numpy  as np
import pylab as pl

T = 10.0  #kB * T
N = 1000  #number of particles
steps = 200000  #total MC steps

# Create a 2D array to store the quantum numbers
n = np.ones([N,3],int)

# Main loop
eplot = []
E = 3*N*pi*pi/2 #initial energy

#MCMC
for k in range(steps):

    # Choose a particle out of N
    i = random.randrange(N)
    # move the particle 
    j = random.randrange(3)
    if random.random()<0.5: 
        #move forward
        dn = 1
        dE = (2*n[i,j]+1)*pi*pi/2
    else:     
        #move backward
        dn = -1
        dE = (-2*n[i,j]+1)*pi*pi/2

    # Decide whether to accept the move
    if n[i,j]>1 or dn==1:
        if random.random()<exp(-dE/T):
            n[i,j] += dn
            E += dE

    eplot.append(E)

# Make the graph
pl.plot(eplot)
pl.xlabel("steps")
pl.ylabel("Energy")
pl.show()
