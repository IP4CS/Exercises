''' 
09/11/2014 @ytang 

This script is to upload data  and calculate all prime numbers in it.
For the data given on GitHub, the result is 1161. 
'''

import numpy as np  #import numpy and name it np

'''IsitaPrime is to test if number x is a prime. if it is a prime number, the function
 returns True to the main program; if not, False.''' 
def IsitaPrime(x):
	R = True
	for iter in range(2,x):
		if number%iter==0:
			#print "The number %d is not a prime number." %x
			R = False
			break
	return R
		
#upload the data from local computer; indicate the data type is Integer. 
data = np.loadtxt('/Users/ying.tang/GitHub/Exercises/Data/SumAllPrimes.txt', int)
 
'''For code testing, i generated a small data file called data.txt to test if my
 code gives the correct sum, e.g. data.txt has [1,3, 10, 15, 101], the sum of all prime numbers
should be 4. 
'''
#data = np.loadtxt('data.txt', int) 

#the sum of all prime numbers
summation = 0 #initiate the summation be zero
for number in data:
	if IsitaPrime(number) == True:
		summation += number  # add all prime numbers together

print "the sum of all prime number in this data set is: %d" %summation 
