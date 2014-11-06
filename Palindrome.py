'''
This python program is to test if a string is a Palindrome.
@ytang 11/06/2014
'''
import string
    
import time
def ifPal(sample):
    if len(sample) <= 1:
        return True
    else:
        return sample[0]==sample[-1] and ifPal(sample[1:-1])

#parse the input string to make all letters be small 
a=raw_input("Please input a string: ")
a=a.lower()
sample=str()
for w in a:
    if w in string.lowercase:
        sample += w
              
time1=time.clock()

ifPal(sample)    

time2=time.clock()
#check the computational time
print time2-time1
