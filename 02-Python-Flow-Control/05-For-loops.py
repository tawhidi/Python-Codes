
# For loop in python

"""
The for loop used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
"""


# Syntax of for Loop
"""
for val in sequence:
    Body of for
    
    
# Example
for i in range(10)
    print(i)
"""

# Example
for i in range(10):  # Python default 0 to start for loop
    print(i)
print('\n')

# Example
for i in range(1, 10):
    print(i, end=' ')

print("\n")


# Example
for i in range(1, 10, 2):   # Here 1 start point, 10 end point, 2 step কতঘর পর প্রিন্ট হবে ।
    print(i, end=" ")
print("\n")


# How to print letter
print('How to print letter : ')
for letter in 'word':
    print(letter)
print('\n')


# Example of list using for loop
print('List using for loop : ')
myList = ["Python", "Django", "Php", "html", 'css']
for item in myList:
    print(item)
print("\n")


# Example of string using for loop
print('string using for loop : ')

s = "Hi, there how are you"
for st in s:
    print(st, end=' ')
print('\n')


# Example of tuple using for loop
print('tuple using for loop : ')

tup = (1, 3, 5, 7, 9)
for t in tup:
    print(t)
print('\n')


# Example of dictionary using for loop
print('Dictionary using for loop : ')
d = {'k1': 1, 'k2': 3, 'Name': 'Hello', 'Age': 23}
for k, v in d.items():
    print(k, end=' ')    # print for all key
    print(v, end=' ')    # print all value
print('\n')


# Example
number = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sum = 0
# iterate over the list
for val in number:
    sum = sum + val
print(sum)
print('\n')


# Example of break
print('for loop using break : ')
for number in range(1, 20):
    if number == 5:
        break
    print(number)
print('\n')


# Example of continue
print('for loop using continue : \n')
for number in range(1, 10):
    if number == 5:
        continue
    print(number, end=' ')

print('\n')


# Python pass statement
"""
In Python programming, pass is a null statement.

The difference between a comment and pass statement ?
The interpreter ignores a comment entirely, pass is not ignored.
However, nothing happens when pass is executed. It results into no operation (NOP).
"""

# Pass Statement
sequence = {'p', 'a', 's', 's'}
for var in sequence:
    pass

"""
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. 
They cannot have an empty body. The interpreter would complain. 
So, we use the pass statement to construct a body that does nothing.
"""

# We can do the same thing in an empty function or class as well.
"""
def function(args):
    pass

class example:
    pass

"""


# Example of  continue, pass, break
print('continue, pass, break using for loop : ')
for i in range(10):
    if i == 5:
        continue
    if i == 7:
        pass
    if i == 9:
        break
    print(i, end=' ')
print('\n')


# Print all the perfect sequence number between 1 to 50 who divided 3 or 5 == 0
# 1 থেকে 50 প্রজন্ত যারা ৩ ও ৫ দ্বারা ভাগকরলে ভাগফল ০ হবে ।
print('Perfect sequence number : \n')
for number in range(1, 50):
    if number % 3 == 0 or number % 5 == 0:
        continue
    print(number, end=' ')
print('\n')


# Example
print("How to print : \n")

# # # #
# # # #
# # # #
# # # #

for i in range(4):
    for j in range(4):
        print('#', end=' ')
    print('#')
print('\n')


# Example of star

"""
*
* *
* * *
* * * * 
* * * * * 
"""
for i in range(5):
    for j in range(i + 0):
        print('*', end=' ')
    print('*')

print('\n')


# Example
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(7):
    for j in range(6 - i):
        print('*', end=' ')
    print('*')
print('\n')


# Example of char symbols
print('char symbols :\n')
for i in range(100):
    print(i, '-', chr(i))
print('\n')


