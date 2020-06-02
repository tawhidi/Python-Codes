# Chained Comparison Operators

# এই Operators এর কাজ হোল একশাথে multiple Comparison চেক করতে পারি ।
print("Chained Comparison Operators : \n")


# Example
a = 1 < 2 and 2 > 4
print(a)


# Example
x = 1 < 3 > 2
print(x)
print('\n')


# Example

"""
 >>>
>>> 1 < 2
True
>>> 2 < 3
True
>>> 1 < 2 < 3
True
>>> 1 < 2 and 2 < 3
True
>>> 1 < 2 and 4 < 3
False
>>> 1 < 3 > 2
True
>>> 1 == 2
False
>>> 1 == 2 or 2 > 1
True
>>> 1==1 or 100==1
True
>>>
"""