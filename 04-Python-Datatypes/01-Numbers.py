"""
    Number Data Type in Python
    Type Conversion
    Python Decimal
    Python Fractions
    Python Mathematics
"""
print('Number : ------------------- ')


'''
Python supports integers, floating point numbers and complex numbers. 
They are defined as int, float and complex class in Python.
Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

'''


# Example of integers

a = 5
print(a)
print(type(a))
print("\n")


# floating point numbers
x = 7.0
print(x)
print(type(x))
print("\n")


# Example Complex numbers
y = 7 + 6j
print(y)
print("real number       : ", y.real)
print("imaginary number  : ", y.imag)
print(isinstance(y, complex)) # isinstance() function to check if it belongs to a particular class
print("\n")


# Type Conversion
'''
We can convert one type of number into another. This is also known as coercion
'''

a = 1 + 4.6
print(a)


# Float
a = 2.4
x = int(a)
print(a)


# int
b = 69
print(float(b))


# Complex
a = 4.7
x = int(a)
print(x+2j)
print("\n")


# Python Decimal

x = (1.1 + 2.2) == 3.3
print(x)

y = 1.1 + 2.2
print(y)
print("\n")

# Example
#
# import decimal
# print(3.1)
# print("3.1 Decimal Number : ",decimal.Decimal(3.1))
# print("\n")
#
# #Example
#
# from decimal import Decimal as D # here D is veriable
#
# print(D('1.1') + D('2.2'))
#
# print(D('1.2') * D('2.50'))
#
# print("\n")


'''
    Python Fractions ভগ্নাংশ
    
'''

# Example of fractions number

# import fractions
# x = fractions.Fraction(9/5)
# print('Fraction(9/5) :', x)
# print("\n")
#
#
# # Example
#
# from fractions import Fraction as F
#
# a = fractions.Fraction(F(1,3) + F(1,3))
# print(a)

# print(1 / F(5,6))
# print(F(-3,10) > 0)
# print(F(-3,10) < 0)
# print("\n")


'''

Python Mathematics
Python offers modules like math and random to carry out different mathematics

'''


# Example of math
import math
print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))
print("\n")


# Example of random
import random
print("Random Number : ", random.randrange(10, 20))
x = ['a', 'b', 'c', 'd', 'e', 'random', 'math']
print("Random Choice : ", random.choice(x))

