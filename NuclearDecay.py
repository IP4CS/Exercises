'''
computational physics (M.Newman), example 10.1
This program uses a Monte Carlo method to simulate the nuclear decay.
'''
import random
from numpy import arange
import pylab as plt

# Constants
NTl = 1000            # Number of thallium atoms
NPb = 0               # Number of lead atoms
tau = 3.053*60        # Half life of thallium in seconds
h = 1.0               # Size of time-step in seconds
p = 1.0 - 2.0**(-h/tau)   # Probability of decay in one step
tmax = 1000           # Total time

# Lists of plot points
tpoints = arange(0.0,tmax,h)
Tlpoints = []
Pbpoints = []

# Main loop
for t in tpoints:
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)

    # Calculate the number of atoms that decay
    decay = 0
    for i in range(NTl):
        if random.random()<p:
            decay += 1
    NTl -= decay
    NPb += decay

# Make the graph
plt.plot(tpoints,Tlpoints, 'o', label='Tl')
plt.plot(tpoints,Pbpoints, '+', label='Pb')
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.legend(bbox_to_anchor=(1,0.5))
plt.show()