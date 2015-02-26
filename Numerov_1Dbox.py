'''
Solve particle in a 1D box
using Numerov Method 

NOTE: a small bug might be in Numerov/Normalization method

@ytang Feb 2015
'''
import numpy as np
import matplotlib.pyplot as plt
import sys

def Potential(x):
    '''
    Potential energy is zero between [-1, 1], and infinity otherwise
    all that matters is the energy value
    '''
    return 0.0

def Normalization(psi):
    '''normalize the wavefunction'''
    norm = 0.0
    psi = np.array(psi)
   
    for i in range(N):
       norm += psi[i]**2
    #norm = sum(psi**2)
    
    psi = psi/np.sqrt(norm)
    return psi
     
def Numerov(E):
    #initiate psi function
    psi=[0.0, 1.0]
    phi=[]
    
    phi0=psi[0]
    fx = 2.0*(Potential(xpoints[1]) - E)
    phi1=psi[1]*(1.0-delta_x*fx/12.0)
    phi.append(phi0)
    phi.append(phi1)

    dx2=delta_x**2 
    
    for i in range(2,N):
        fx = 2.0*(Potential(xpoints[i]) - E)
        newphi = 2*phi[i-1] - phi[i-2] + dx2*fx*psi[i-1]
        newpsi = newphi/(1.0-dx2*fx/12.0)
        psi.append(newpsi)
        phi.append(newphi)
    
    #normalize psi
    psi = Normalization(psi)
    
    return psi    
 
''' Main Program '''    
delta_x = 0.001
bi=-1
bf=1
#divide x into small grids
xpoints = np.arange(bi, bf, delta_x)
N = len(xpoints)

#create phi function
phi=[]
psi=[]

E= 1.5 #initial energy
dE=0.003 #energy steps

fd = open('energy.dat', 'w')

psi=Numerov(E)

#course search for energy
oldpsi=psi[N-1]
fd.write('%12.8f        %12.8f \n'  %(E, oldpsi))  

for j in range(5000):
    E += dE
    psi=Numerov(E) #Numerov method to find psi at this energy E
    newpsi=psi[N-1]
    fd.write('%12.8f        %12.8f \n'  %(E, newpsi))
    if oldpsi*newpsi < 0 :
        break
    else:
        oldpsi=newpsi      
     
#bisection search between oldE and 0.5(E0+E1)
accuracy=1.0e-10
E1=E-dE
E2=E

oldpsi2=psi[N-1] #with E

psi=Numerov(E1) #lower boundary 
oldpsi1=psi[N-1] #with E-dE

while E2-E1 > accuracy:
    E0=0.5*(E1+E2) #midpoint energy
    #print ('%16.16f   %16.16f' %(E1, E2))
    psi=Numerov(E0)  #with (E-0.5dE)
    newpsi=psi[N-1]  #with (E-0.5dE), mid energy 
    
    if oldpsi1*newpsi <= 0.0 : #true E is between E1 and E1-0.5dE
        E2=E0
        oldpsi2=newpsi
    else: #true E is between E1-dE and E1-0.5dE
        E1=E0
        oldpsi1=newpsi 
    
fd.close()    

plt.plot(xpoints, psi)
plt.ylabel('$\psi(x)$', size=15)
plt.xlabel('x', size=15)
plt.show()
