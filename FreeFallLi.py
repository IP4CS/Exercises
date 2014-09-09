#!/usr/bin/env python3
"""This program is wriiten by Rebecca Li, to help solve the free fall problem. It gives the time an object need to reach
the ground from height h. """
import math
h = input('Type the height in meters')  #define the variable h
a = 9.8                                 #define the gravitational acceleration
t = math.sqrt(2.0*float(h)/a)
print ('It takes the ball %s s to reach the ground' %(t))
