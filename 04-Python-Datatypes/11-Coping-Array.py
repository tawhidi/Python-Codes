
# Copying array in python

from numpy import *
arr = array([12, 2, 4, 6, 7])
arr = arr + 4  # Each element added 4
print(arr)
print('\n')


# Example of vectorized operations

from numpy import *
arr1 = array([1, 2, 3, 4])
arr2 = array([2, 4, 6, 8])
arr3 = arr1 + arr2
print(arr3)
print('\n')


# Example Math
from numpy import *
arr = array([2, 3, 4, 5])
print(sin(arr))
print('\n')


# Example
from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([3, 5, 6, 5, 2])
print(concatenate([arr1 + arr2]))
print('\n')


# Example of shallow copy and deep copy

x = array([2, 4, 5])
y = x.view()  # shallow copy
print(y)

z = x.copy()  # deep copy
print(z)

x[1] = 7
print(x)
print(id(x))

