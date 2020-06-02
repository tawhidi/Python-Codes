# Python Variables, Constants and Literals
print('Python Variables : -------------- \n')


# What is Variable ?

"""
Variables are nothing but reserved memory locations to store values.
Variable হোল একটি বক্স যার মধ্যে আমারা আনেক কিছু রাখতে পারি ।
Normally when you say variable this terms simply means you can change the value.

    1. Number =( int, float, double )
    2. Name = ( String, char, Boolean)
"""


# Rules of variable decelerations

"""
    1. A variable name must start with a letter or the underscore character
    2. A variable name cannot start with a number
    3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    4. Variable names are case-sensitive (age, Age and AGE are three different variables)
    5. There are some reserved words which you cannot use as a variable name because Python uses them for other things.
    6. Not override a built-in function
    7. Variable should not have space in between

    # Or

     ১. প্রতিটি ভেরিয়েবল এর একটি নাম থাকতে হবে ।
    ২. প্রথম লিটার আবশ্যই alphabetic letter আথাৎ uppercase or lowercase or underscore হতে হবে । A, a, _variable ।
    ৩. Symbols দ্বারা শুরু হতে পারবেনা । @, #, $, %, ! ... ।
    ৪. কোন স সংখ্য দ্বারা হতে পারবেনা ।
    ৫. এর শেষে ; দিতে হয় না ।
    ৬. Python case sensitive আথাৎ a = 4 and A = 4 same না ।
    ৭. Python data type  বলে দিতে হয় না । 
    ৮. Reserved keyword দ্বারা শুরু হতে পারবেনা । 
"""


# Example
"""
Here, we have created a variable named number. We have assigned the value 10 to the variable.
"""

number = 10
number = 1.1    # Initially, the value of number was 10. Later, it was changed to 1.1.
print(number)
print('\n')


# How to Assigning Values to Variables ?
"""
 The equal sign (=) is used to assign values to variables.
"""


# Here x is variable and values is "My variable"
x = "My variable"
print(x)
print('\n')


# Can't assign to literal
"""
>>> a = 12
>>> 12 = a
SyntaxError: can't assign to literal
>>>
"""


# Assigning values to Variables
website = "hello.com"
print(website)


# Changing the value of a variable
website = "website.com"
print(website)
print('\n')


# Assigning multiple values to multiple variables
print('Assign Value to Multiple Variables :')
a = b = c = 69
print(a)
print(b)
print(c)


# Multiple Variables
a, b, c = 1, 2, "jibon"
print(a)
print(b)
print(c)
print('\n')


# Example
x = y = z = "same"
print(x)
print(y)
print(z)
print('\n')


# Python creates an Objects
print('Creates an Objects : ------------- ')
"""
id : 
'off' : value
type  : String

"""
status = "off"
print('value :', status)
print('id    :', id(status))
print('type  :', type(status))
print('\n')


# List of some different variable types
"""
x = 123 			# integer
b = 123333333	    # long integer
c = 3.14 			# double float
d = "hello" 		# string
e = [0, 1, 2] 		# list
f = (0, 1, 2) 		# tuple
g = open('hello.py', 'r') 	# file
print('\n')
"""

# Example of case-sensitive
print('Variable are case-sensitive : ')
a = 4
print("a : ", a)
print(id(a))

# Example
A = 4
print("A : ", A)
print(id(A))
print("\n")


# You can also use the + character to add a variable to another variable:
print('Add a variable to another variable :')

x = "Youtube"
print(x)
c = x + " rocks"
print(c)
print(x[0])
# print(x[10])    # string out of the range


# Example
x = "Python is "
y = "awesome"
z = x + y
print(z)


# Example
x = (
    2 + 4 * 6 -
    6 + 4 - 2 +
    3 - 3 * 4
)
print("X : ", x)
print('\n')


# Example
myNumber = 69
name = "Jibon"
fullName = "Jibon Ahmed"
_newName = "Jayed"
salary = 30.20
address = "Dhaka/Bangladesh"
COUNTRY = "Bangladesh"
A = True
B = True

print(myNumber)
print(name)
print(fullName)
print(_newName)
print(salary)
print(address)
print(COUNTRY)
print(A)
print(B)
print("\n")


# Python memory efficient
print("Python memory efficient : ")
a = 10
print('a :', a)
print('id a:', id(a))
b = a
print('b    :', b)
print('id b :', id(10))

k = 10
print('k :', k)
print('k :', id(k))
print('\n')


# How to swap variable
print('swap variable :')
# Solve 1 :
a = 5
b = 6
a, b = b, a
print('swap a :', a)
print('swap b :', b)
print('\n')


# Constants
# A constant is a type of variable whose value cannot be changed.

PI = 3.14
print("PI : ", PI)


# Example
GRAVITY = 9.8
print("GRAVITY : ", GRAVITY)
print('\n')


# Example of Numeric Literals
print('Numeric Literals : -------- ')

a = 0b1010  # Binary Literals
b = 100     # Decimal Literal
c = 0o310   # Octal Literal
d = 0x12c   # Hexadecimal Literal

print("Binary Literals     : ", a)
print("Decimal Literal     : ", b)
print("Octal Literal       : ", c)
print("Hexadecimal Literal : ", d)
print('\n')


# Example of Complex Literal
x = 3.14j
print(x)
print(x, x.imag, x.real)


# Example of Float Literal
float_1 = 10.5
float_2 = 1.5e2

print(float_1)
print(float_2)
print('\n')


# String literals
# How to use string literals in Python?
print('String literals : ----------- ')

"""
A string literal is a sequence of characters surrounded by quotes. 
We can use both single, double, or triple quotes for a string.
"""


strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
print('\n')


# Boolean literal
print('Boolean literal : -------------- ')
"""
A Boolean literal can have any of the two values: True or False.
"""

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
print('\n')


# Special literals
print('Special literals : ----------- ')
"""
Python contains one special literal i.e. None.
We use it to specify that the field has not been created.
"""

# How to use special literals in Python ?
drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)
print('\n')


# Literal Collections
print('Literal Collections : -------------- ')
"""
There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
"""

# How to use literals collections in Python?
fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
print('\n')


# How to print output the previous operations
"""
>>> a = 5
>>> a
5
>>> _+a # underscore means output of the previous operations
10
>>>
"""


# Example area of length
length = 1.10
width = 2.20
area = length * width
print("The area is: ", area)

