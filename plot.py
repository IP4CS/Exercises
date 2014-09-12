''' 
09/11/2014  @ytang 

This code is to do some exercises on plotting functions in python.

we are going to do three plots:
(1) linear plot: y = x^3 - 2x - 6, x is from [0,10]
(2) scatter plot: stars
(3) density plot: densities 

when run this code, user need to input a number [1-3] to choose one of this three plots 
'''

import pylab as pl
import numpy as np
from matplotlib import axes

choice = input("Which plot do you want to see? \n  Input \
1 for the line graph, 2 for the scatter plot and 3 for the density plot: ")

if choice==1 :
	'''
	for the line graph 
	'''
	x=np.linspace(0,10,100)  #a hundred points between 0 to 10	
	y=x**3-2*x-6  

	pl.plot(x,y,color='red', linewidth=2.5, linestyle='-', marker=4)
	pl.title('Plotting x**3 - 2*x -6')
	pl.ylabel('y')
	pl.xlabel('x')

	#for seeing the plot on a log-log scale
	#pl.yscale('log')
	#pl.xscale('log')

	pl.show()

elif choice==2:
	''' 
	for the scatter plot 
	'''
	#upload the file saved in my /Users/ying.tang/GitHub/Exercises/Data dicectory
	Stars = np.loadtxt("/Users/ying.tang/GitHub/Exercises/Data/stars.txt", float)
	Magnitude = Stars[:,0] #first column
	Temperature = Stars[:,1] #second column
	pl.scatter(Magnitude, Temperature)  #scatter plot
	pl.title('Stars')  #make title
	pl.xlabel('Temperature') #label x axis
	pl.ylabel('Magnitude') #label y axis
	pl.xlim(16000,0) #reverse the range, to make the 
	pl.ylim(20,-5)   #reverse the range
	pl.show()
	
elif choice==3:
	#upload the circular.txt file saved in my /Users/ying.tang/GitHub/Exercises/Data dicectory
	Density = np.loadtxt("/Users/ying.tang/GitHub/Exercises/Data/circular.txt", float)
	
	#check the shape and the dimension of the data
	print "density shape %s" %(' '.join(map(str, Density.shape))) 
	#because "Density.shape" is a list, so I use function map to map all elements of the list to string type, and join them with a space in between. 
	
	pl.imshow(Density, origin="lower")  #move origin of the plot [0,0] to the lower corner
	pl.hsv() #change the color to rainbow scheme
	#pl.gray()  #change the color to black and white 
	#pl.hot()   #change the color scheme to black-yellow-red-white
	#pl.bone()   # for mimicking the color of the bone: black and white, with a hint of blue
	
	pl.colorbar()  #plot the color bar as well
	
	pl.xlabel('x')
	pl.ylabel('y')
	pl.title('Density Plot')
	
	#the default color scheme is heat-map
	pl.show()
	
else:
	print "You input a wrong number. Bye bye."
