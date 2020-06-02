
# Example different ways to create in numpy

"""
    array()
    linespace()
    logspace()
    arrnge()
    zeros()
    ones()
"""


# Example
from numpy import *
arr = array([12, 13, 14])
print(arr)
print('\n')
# Example


# Example
from numpy import *
x = array([12, 34, 55], int)
print(x)
print('\n')


# Example only float
y = array([2.6, 4.7, 6.9], float)
print(y)
print('\n')


# Example of arange
z = arange(1, 10, 2)
print(z)
print('\n')


# Example of line space
arr = linspace(0, 15, 16)
print(arr)
print('\n')


# Example of zeros
arr = zeros(5)
print(arr)
print('\n')


# Example ones
arr = ones(5, int)
print(arr)

