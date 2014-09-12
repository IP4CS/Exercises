'''
09/11/2014  @ytang

Problems:
calculate the magnitude of vector d1=3i-4j+2k and d2=2i+1j-1.5k and their dot product

'''

#import packages
import numpy as np

def magnitude(vec):
#calculate the magnitude of a vector
	dist = np.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)
	return dist

def dotproduct(d1, d2):
#calculate the product of a vector
	return np.dot(d1,d2)

#define two arrays as vectors
d1=np.array([3, -4, 2])
d2=np.array([2, 1, -1.5])


print "Two vectors are:\n d1= %fi+%fj+%fk and d2=%fi+%fj+%fk \n" %(d1[0], d1[1], d1[2], d2[0], d2[1], d2[2])

print "The magnitude of vector d1 is: %f" %magnitude(d1)
print "The magnitude of vector d2 is: %f" %magnitude(d2)
print "the doc product of d1 and d2 is: %5.1f" %dotproduct(d1,d2)



