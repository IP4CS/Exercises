import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import cm

def InitialConfiguraiton(Nx, Ny):
    #input the site number in x and y, return a 2D spin configuration
    N=Nx*Ny
    #create a 1D array to store 2D spins. 
    spin=np.zeros((Nx,Ny), int)
    for j in range(Ny):
        for i in range(Nx): 
            spin[i,j]=np.sign(random.random()-0.5)        
    return spin

def ChooseSpin(Nx, Ny):
    #input two integers
    x = int(Nx*random.random())
    y = int(Ny*random.random())
    return x, y

def Energy(Nx, Ny, spin):
    #calculate the total energy of the system
    eng = 0.0
    for j in range(Ny):
        for i in range(Nx):
            eng += spin[i,j]*(spin[(i-1+Nx)%Nx, j] + spin[(i+1)%Nx, j] \
                            +spin[i, (j-1+Ny)%Ny] + spin[i, (j+1)%Ny])
    eng = eng/2.0
    return J*eng
    
def DeltaEnergy(sx, sy, Nx, Ny, spin):
    #return the half of the change of energy 
    delta_eng = -1.0*(spin[sx,sy]*(spin[(sx-1+Nx)%Nx, sy] + spin[(sx+1)%Nx, sy] \
                            +spin[sx, (sy-1+Ny)%Ny] + spin[sx, (sy+1)%Ny]))
    return J*delta_eng

def Prob(beta):
    #E= -J sum(S_i S_j)
    PE=np.zeros(10, float)
    PE[4+0]=np.exp(0.0)
    PE[4+2]=np.exp(-beta*2.0*2.0)
    PE[4+4]=np.exp(-beta*4.0*2.0)
    PE[4-4]=np.exp(beta*4.0*2.0) 
    PE[4-2]=np.exp(beta*2.0*2.0)
    return PE

def Magnetization(Nx, Ny, spin):
    M=0
    for j in range(Ny):
        for i in range(Nx):
            M += spin[i, j]
            
    return float(M)/float(Nx*Ny)

def MonteCarloSweep(MCstep, spin, Nx, Ny):
    E = Energy(Nx, Ny, spin)
    M=Magnetization(Nx, Ny, spin)
    #subroutine for Monte Carlo Sweep
    for i in range(MCstep):
        #pick a random spin with position x and y
        sx, sy=ChooseSpin(Nx, Ny)
        #the change of energy value 
        deltaE= DeltaEnergy(sx, sy, Nx, Ny, spin)

        #Metropolis Algorithm acceptance: 
        if random.random()<PE[4+deltaE]:
            spin[sx, sy]=-spin[sx, sy]
            E += 2.0*deltaE
            M += 2.0*float(spin[sx, sy])/float(Nx*Ny)
    return E, M, spin 
        
Nx = int(raw_input('Give Nx: \n'))
Ny = int(raw_input('Give Ny: \n'))
global J
J=-1.0
beta= 1.0 #1/T
MCstep=100000
Nbin=10 #bin steps
#Precalculated Probability Distribution
PE=Prob(beta)

#initial configuration of the 2D ising model
spin = InitialConfiguraiton(Nx,Ny)

Mlist=[]
Elist=[]

for i in range(Nbin):
    E, M, spin = MonteCarloSweep(MCstep, spin, Nx, Ny)
    Mlist.append(M)
    Elist.append(E)

Mlist=np.array(Mlist) 
Mlist=abs(Mlist) #take the absolute value of Magnetization
print "Magnetization: %f  "  %np.average(Mlist)
print "Errorbar of Magnetization: %f"  %(np.std(Mlist)/np.sqrt(Nbin-1))

plt.figure(1)
plt.subplot(211)
plt.plot(Mlist, label='Magnetization')
plt.legend()
plt.subplot(212)
plt.plot(Elist, label='Energy')
plt.xlabel('bin step')
plt.legend()
plt.matshow(spin, cmap=cm.gray)
plt.show()