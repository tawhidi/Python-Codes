
# Python Statement, Indentation and Comments


# Python Statement
print('Python Statement : ---------------- \n')


"""
Instructions that a Python interpreter can execute are called statements. 
For example, a = 1 is an assignment statement. 

if statement, for statement, while statement, etc.
"""


# Statements contained within the [], {}, or () brackets
# do not need to use the line continuation character.


# Example
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(days)


# Example
a = 5
print('Single-line-statement : ', a)
print('\n')


# Multi-line statement

"""
In Python, the end of a statement is marked by a newline character. 
But we can make a statement extend over multiple lines with the line continuation character (\)
"""


# Example
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)


# Example
x = (
    2 + 4 * 6 -
    6 + 4 - 2 +
    3 - 3 * 4
)
print("X : ", x)


# Example
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print('Multi-line statement : ', a)
print('\n')


# Example
colors = ['red',
          'blue',
          'green']

print('colors : ', colors)


# Example
a = 1; b = 2; c = 3
print(a)
print(b)
print(c)
print('\n')


# Example
A = B = C = 700
print(A)
print(B)
print(C)
print('\n')


# Python Indentation
print('Python Indentation : ------------- ')

"""
Most of the programming languages like C, C++, and Java use braces { } to define a block of code.
In python Generally, four whitespaces are used for indentation and are preferred over tabs.
"""


# Rules for writing identifiers

""" 
    1. Identifiers can be a combination of letters in lowercase (a to z) 
    or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
    2. An identifier cannot start with a digit.
    3. Keywords cannot be used as identifiers.
    4. We cannot use special symbols like !, @, #, $, % etc. in our identifier.
    5. Identifier can be of any length.
"""


# Example
"""
>>> if True:
   print("True")
else:
   print("False")
"""


# Example
for i in range(1, 11):
    print(i)
    if i == 5:
        break
print('End Program ')
print('\n')


# Example
if True:
    print('Hello')
    a = 5


# Example
if True: print('Hello'); a = 5


# Example
if 5 > 2:
    print("Five is greater then two")
print('\n')


# Python Comments
print('Python Comments : ------------ ')

"""
Comments are very important while writing a program. 
They describe what is going on inside a program, 
so that a person looking at the source code does not have a hard time figuring it out.
"""


# In Python, we use the hash (#) symbol to start writing a comment.

# This is a comment
# print out Hello
print('Hello')
print('\n')


# Multi-line comments

"""
We can have comments that extend up to multiple lines. 
One way is to use the hash(#) symbol at the beginning of each line. 
"""

# This is a long comment
# and it extends
# to multiple lines


# Another way of doing this is to use triple quotes, either ''' or """.
"""This is also a
perfect example of
multi-line comments"""


# Docstrings in Python
print('Docstrings in Python : ------------ ')


"""
A docstring is short for documentation string.
Python docstrings (documentation strings) are the string literals that appear right
after the definition of a function, method, class, or module.
"""


# Example
def double(num):
    """Function to double the value"""
    return 2*num


x = double(2)
print(x)


# The docstrings are associated with the object as their __doc__ attribute.

# Example
def double(num):
    """Function to double the value"""
    return 2*num


print(double.__doc__)   # Mouse point and press ctrl
print('\n')


# Skip Char
print('Skip Char : ', 'c:\some\name')   # \n new line
# or
print('Skip Char : ', 'First name, second \name')
print('\n')


# Row String
print('Row String : ', r'c:\some\name')   # \n new line
print('Row String : ', r'First name, second \name')