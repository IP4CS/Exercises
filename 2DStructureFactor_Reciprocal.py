'''
this program is to calculate the structure factor of 2D lattice
in order to illustrate the meaning of the K vectors in Reciprocal space

@ytang Feb 2015
'''

#import necessary packages 
import numpy as np
import matplotlib.pyplot as plt
import sys 

def S_k(lattice):
    '''function to calculate the structure factor of 2D Lattice'''
    #basis in k space
    k1=2.0*np.pi/float(x1) 
    k2=2.0*np.pi/float(y1) 
    
    k_vector = min(k1, k2)
    
    #find the dimension size of the lattice
    sx, sy = lattice.shape
    
    #create 2D structure factor array
    Sk = np.zeros([sy, sx], complex)
    
    #calculate Sk for each [kx, ky] set
    for kj in range(sy): #y axis 
        for ki in range(sx): #x axis
            k = [ki*k_vector, kj*k_vector] # k vector, in x and y direction
            
            #lattice point 1
            for j1 in range(sy):
                for i1 in range(sx):
                  
                  # lattice point 2
                   for j2 in range(sy):
                       for i2 in range(sx):
                           #only count if there is a lattice point
                           if (lattice[i2, j2]==1 and lattice[i1, j1]==1):
                               d=[j2-j1, i2-i1] #d vector, in x and y direction, real space
                               #sum over structure factor over all possible distances
                               Sk[kj, ki] += np.exp(- 1j*np.dot(np.array(k), np.array(d)))
   
    #normalize Sk
    Sk=Sk/n**2

    #make Sk more visible in 2D plot by adding a reciprocal lattice spacing between points
    show_Sk=np.copy(Sk.real)
    #add a space between points in y direction 
    for i in range(sy+1):
        show_Sk=np.insert(show_Sk, 2*i, 0, axis=0)
   
    #add a space between points in x direction          
    for j in range(0, sx+1):
        #print 3*j+1
        if j*3+1 < show_Sk.shape[0] :
            show_Sk=np.insert(show_Sk, (j)*3+1, 0, axis=1)
    
    return show_Sk

############# start of the main program ###########

Lx=4  #number of lattice in x direction
Ly=4  #number of lattice in y direction


#creat a 2D array as the lattice
x1=1  #lattice spacing in x direction
y1=2  #lattice spacing in y direction

n=max(Lx*x1, Ly*y1)*2
lattice = np.zeros([Ly*y1, Lx*x1], float)

for j in range(Ly): #y axis
    for i in range(Lx): #x axis
        #move lattice to the center of the figure
        lattice[y1*j, x1*i]=1
                 
#visualize the lattice in real space
show_lattice=np.copy(lattice)

#add a space between points in x direction
for i in range(Lx*x1+1):
    show_lattice=np.insert(show_lattice, 2*i, 0, axis=1)
 
#add a space between points in y direction          
for j in range(0, Ly*y1+1):
    #print 3*j+1
    if j*3+1 < show_lattice.shape[0] :
        show_lattice=np.insert(show_lattice, (j)*3+1, 0, axis=0)
 
#generate 2D plots
#in real space
plt.figure(1)
plt.subplot(121)   
plt.title("2D lattice in Real Space") 
plt.imshow(show_lattice, cmap=plt.cm.gray)
plt.xlabel('x')
plt.ylabel('y')

#calculate the structure factor of S_k
show_Sk=S_k(lattice)

#in reciprocal space
plt.subplot(122) 
plt.title("Structure factor in K space")
plt.imshow(show_Sk, cmap=plt.cm.gray)
plt.xlabel('kx')
plt.ylabel('ky')
    
#show plots    
plt.show()
