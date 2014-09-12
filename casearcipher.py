''' 
09/11/2014 @ytang

This code is to decode a message in caeser cipher to  english.
(The original problem is from www.ling.gu.se/~lager/python_exercises.html)

the secret message is: 
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!  

'''

import operator 
import numpy as np
import time

#ROT13 and English

#English to ROT13, KEYs TO VALUEs 
English_ROT13 = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
       
#ROT13 to English, VALUEs to KEYs
ER = English_ROT13.copy()

#ROT13_English = dict(zip(ER.values(), ER.keys()))

#print len(English_ROT13)

S='Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

NewS = ''
words=S.split()

for word in words:
	for letter in word:	
		if (letter=='?' or letter=='!'):
			NewS += letter
			break
		NewS += ER.get(letter)
	NewS += ' '
print "******************"	
print "!!!CONFIDENTIAL!!!"
print "******************"
time.sleep(2)
print "the secret message says:"
print "..."
time.sleep(1)
print "..."
time.sleep(1)
print NewS.upper()


