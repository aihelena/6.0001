###This is my code for 6.0001 pset 0

##Write a program that does the following in order:
##
##    1. asks the user to enter a number "x"
##    2. Asks the user to enter a number "y"
##    3.Prints out number "x" raised to the power "y"
##    4. Prints out the log (base 2) of 'x'

import numpy

print ("Enter number x: ")
x = int(input())
print ("Enter number y: ")
y = int(input())
print ("X**y = "+ str(x**y))
print ("log(x) = "+str(int(numpy.log2(x))))
