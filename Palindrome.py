'''This python program is for testing a string is a Palindrome.
'''

import string
    
import time
def ifPal(sample):
    if len(sample) <= 1:
        return True
    else:
        return sample[0]==sample[-1] and ifPal(sample[1:-1])

time1=time.clock()
a=raw_input("Please input a string: ")
a=a.lower()
sample=str()
for w in a:
    if w in string.lowercase:
        sample += w
              
ifPal(sample)    


time2=time.clock()
#check the computational time
print time2-time1
