
# Python array

"""
Python array is a collection of items stored at configures memory locations

"""

# Example

from array import *
vals = array('i', [1, 3, 5, 7, 9])
print(vals)

# buffer_info() function return how many element in array
print(vals.buffer_info())
print(vals[0])

x = vals[0] = 69
print(x)
print('\n')


# Example

from array import *
vals = array('i', [2, 4, 6])
print(vals)

# using loop
for i in vals:
    print(i)
print('\n')


# Example
from array import *
vals = array('u', ['a', 'b', 'c', 'd', 'e'])

for e in vals:
    print(e)
print('\n')


# Example
from array import *
vals = array('i', [4, 6, 8, 10])
new_array = array(vals.typecode, (a for a in vals))
for e in new_array:
    print('new array :', e)
print('\n')


# Array values from user in python search array
from array import *
arr = array('i', [])
n = int(input('Enter the length of array : '))
for i in range(n):
    x = int(input('Enter the next value : '))
    arr.append(x)
print(arr)
print('\n')


