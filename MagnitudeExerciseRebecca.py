#!/usr/bin/env python
# Author:Rebecca Li
# Date: 9-9-2014
""" This program is written to find the magnitude and dot product of two vectors"""

from numpy import array  # import the function array from numpy
d_1 = [3.0,-4.0,2.0]     #define vector d_1
d_2 = [2.0,1.0,-1.5]     #define vector d_2
d_1 = array(d_1,float)   #change the type of vecotr from list to array
d_2 = array(d_2,float)

sqsum1 = 0             # give the variable sqrtsum1 an initial valuable 0
for item in d_1:         # This for loop gives the square of the magnitude of d_1
    sqsum1 += item**2
    
from math import sqrt    #import function sqrt from package math
magnitude1 = sqrt(sqsum1)
print "The magnitude of vector d_1 is %f" %(magnitude1)

sqsum2 = 0              #Again, we do the same thing for d_2
for item in d_2:         
    sqsum2 += item**2
    
from math import sqrt
magnitude2 = sqrt(sqsum2)
print "The magnitude of vector d_2 is %f" %(magnitude2)

from numpy import dot      #import the function dot from package numpy
dot_product = dot(d_1,d_2)     # calculate the dot product of vector d_1 and d_2
print 'The dot product of d_1 and d_2 is %f' %(dot_product)

