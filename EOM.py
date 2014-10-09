'''
Author @ytang 10/09/2014
This script is to solve non-linear pendulum motion
The initial condition is: Theta = 30 degree, Omega=0 when the pendulum is released 
We assume the length of the string is L=1.0m and the 

theta is the angle,
omega is the angular velocity 
acc is the angular acceleration 
'''
import numpy as np
import pylab as pl

#define the acceleration of the pendulum motion 
def acc(theta):
    return -9.8*np.sin(theta)

#the LeapFrog Algorithm 
def LeapFrog(Theta, Omega, h):
    Omega += h*acc(Theta)
    Theta += h*Omega
    return Theta, Omega 

#the second order Runge-Kutta Algorithm 
def RK2(Theta, Omega, h):
    k1=h*acc(Theta)
    l1=h*Omega
    k2=h*acc(Theta+0.5*l1)
    l2=h*(Omega+0.5*k1)
    Omega += k2
    Theta += l2
    return Theta, Omega
    
#the forth order Runge-Kutta Algorithm
def RK4(Theta, Omega, h):
    k1 = h*acc(Theta)
    l1 = h*Omega
    k2 = h*acc(Theta+0.5*l1)
    l2 = h*(Omega + 0.5*k1)
    k3 = h*acc(Theta+0.5*l2)
    l3 = h*(Omega + 0.5*k2)
    k4 = h*acc(Theta+l3)
    l4 = h*(Omega+k3)
    Omega += (k1+2.0*k2+2.0*k3+k4)/6.0
    Theta += (l1+2.0*l2+2.0*l3+l4)/6.0
    return Theta, Omega
    
#initial conditions
theta = np.radians(30.0) #for leapfrog
omega = 0.0

#for each algorithms: 0 for Leap Frog, 1 for RK2, 2 for RK4
theta0=theta1=theta2=theta
omega0=omega1=omega2=omega
#create list for each algorithms
thetaLeapFrog = []
thetaRK2 = []
thetaRK4 = []
omegaLeapFrog = []
omegaRK2 = []
omegaRK4 = []

#define time steps: we observe the pendulum motion for 10 seconds
#N is the number of steps, h is the time interval 
totalTime=40.0
N=10000
h=totalTime/float(N)
#evenly distributed time points
tpoints = np.linspace(0.0, totalTime, N)

omega0=omega - 0.5*h*acc(theta0)
for t in tpoints:
    #for Leap Frog
    thetaLeapFrog.append(theta0)
    theta0, omega0 = LeapFrog(theta0, omega0, h)
    omegaLeapFrog.append(omega0)
    
    #RK2
    thetaRK2.append(theta1)
    theta1, omega1 = RK2(theta1, omega1, h)
    omegaRK2.append(omega1)
    
    #RK4
    thetaRK4.append(theta2)
    theta2, omega2 = RK4(theta2, omega2, h)
    omegaRK4.append(omega2)

pl.plot(tpoints, thetaLeapFrog, label='Theta Leap-Frog')
pl.plot(tpoints, thetaRK2, label='Theta RK2')
pl.plot(tpoints, thetaRK4, label='Theta RK4')
pl.plot(tpoints, omegaLeapFrog, label='Omega Leap-Frog')
pl.plot(tpoints, omegaRK2, label='Omega RK2')
pl.plot(tpoints, omegaRK4, label='Omega RK4')
pl.xlabel('t', fontsize=20)
pl.ylabel('Theta/Omega', fontsize=20)
pl.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fancybox=True, shadow=True)
#pl.show()

#showing theta-omega phase diagram
figure2=pl.figure(2)
pl.plot(omegaLeapFrog, thetaLeapFrog, marker='o', color='blue')
pl.xlabel('Omega')
pl.ylabel('Theta')

#compute the total energy: kinetic energy + potential energy 
E_LF=np.zeros(len(tpoints))
E_RK2=np.zeros(len(tpoints))
#E_RK4=np.zeros(len(tpoints))

#assume the mass = 1kg
#conver lists to arrays
omegaLeapFrog=np.array(omegaLeapFrog)
omegaRK2=np.array(omegaRK2)
omegaRK4=np.array(omegaRK4)
thetaLeapFrog=np.array(thetaLeapFrog)
thetaRK2=np.array(thetaRK2)
thetaRK4=np.array(thetaRK4)

#compute the energy calculated by three methods
E_LF=0.5*omegaLeapFrog**2.0+9.8*(1.0-np.cos(thetaLeapFrog))
E_RK2=0.5*omegaRK2**2.0+9.8*(1.0-np.cos(thetaRK2))
E_RK4=0.5*omegaRK4**2.0+9.8*(1.0-np.cos(thetaRK4))

#the total energy of the system
exact_energy=[9.8*(1.0-np.cos(np.pi/6.0))]*len(tpoints)
exact_energy=np.array(exact_energy)

figure3=pl.figure(3)
pl.plot(tpoints, E_RK2-exact_energy, label='RK2')
pl.plot(tpoints, E_RK4-exact_energy, label='RK4')
pl.plot(tpoints, E_LF-exact_energy, label='Leap Frog')
#pl.ylim(-1.0, 1.0)
pl.xlabel('time', fontsize=15)
pl.ylabel('Calculated Energy - Exact Energy', fontsize=15)
pl.legend()
pl.show()
    