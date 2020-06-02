
# Data types in python
print('Data types in python : -------------------------- \n')


# Python has five standard data types

"""
Numeric Types   :	int, float, complex
Text Type       :	str
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
None
complex
unicode
"""


# Python supports four different numerical types
"""
int (signed integers) 
long (long integers, they can also be represented in octal and hexadecimal)
float (floating point real values) 
complex (complex numbers)

"""
print('Numeric Types :')
# Example of integers
a = 5
print(a)
print(type(a))


# floating point numbers
x = 7.0
print(x)
print(type(x))


# Example Complex numbers
y = 7 + 6j
print(y)
print("real number       : ", y.real)
print("imaginary number  : ", y.imag)
print('\n')


# String
"""
String is sequence of Unicode characters. 
We can use single quotes or double quotes to represent strings. 
"""
print('String : -------------------- ')


# How to Declear String in python

# We use it   : '''  '''
#   and       : """  """
# not use it  : '''  """
# """

str = 'Hello World!'
print(str)           # Prints complete string
print(str[0])        # Prints first character of the string
print(str[2:5])      # Prints characters starting from 3rd to 5th
print(str[2:])       # Prints string starting from 3rd character
print(str * 2)       # Prints string two times
print(str + "TEST")  # Prints concatenated string
print('\n')

# Another Example of string
a = "I don't like this"
print("a = ", a)
print(type(a))
print("\n")


# Sequence Types : list, tuple, range
print('Sequence Types : list, tuple, range : ------------------------ \n')


# Python Lists
print('Python list : ------------------- ')
"""
List is an ordered sequence of items.
A list contains items separated by commas and enclosed within square brackets ([]).
"""

list = ['abcd', 786, 2.23, 'Jayed', 70.2]
another_list = [123, 'Hossain']
print(list)                 # Prints complete list
print(list[0])              # Prints first element of the list
print(list[1:3])            # Prints elements starting from 2nd till 3rd
print(list[2:])             # Prints elements starting from 3rd element
print(another_list * 2)     # Prints list two times
print(list + another_list)  # Prints concatenated lists
print(type(list))
print('\n')


# Tuples
"""
Tuple is an ordered sequence of items same as a list. 
The only difference is that tuples are immutable. Tuples once created cannot be modified.
"""
print('Tuples : -------------------------')

tup = ('abcd', 786, 2.23, 'Jayed', 70.2)
another_tup = (123, 'Hossain')

print(tup)                 # Prints complete list
print(tup[0])              # Prints first element of the list
print(tup[1:3])            # Prints elements starting from 2nd till 3rd
print(tup[2:])             # Prints elements starting from 3rd element
print(another_tup * 2)     # Prints list two times
print(tup + another_tup)  # Prints concatenated lists
print(type(tup))
print('\n')

# Example of range
print('Range : -------------- ')

x = range(10)
print(x)
print(type(x))
print('\n')


# Dictionaries Type    :	dict
print('Dictionaries : -------------- ')

"""
Dictionary is an unordered collection of key-value pairs.
t is generally used when we have a huge amount of data. 
Dictionaries are optimized for retrieving data. 
We must know the key to retrieve the value.
"""
dict = { }
dict['one'] = "This is one"
dict[2] = "This is two"
list = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])          # Prints value for 'one' key
print(dict[2])              # Prints value for 2 key
print(list)                 # Prints complete dictionary
print(list.keys())          # Prints all the keys
print(list.values())        # Prints all the values
print(list.get('name'))     # How to get element we can call key
print(type(list))
print('\n')


# Set
print('Set : ----------- ')
"""
Set is an unordered collection of unique items. 
Set is defined by values separated by comma inside braces { }. 
Items in a set are not ordered.
"""

a = {5, 2, 3, 1, 4}
print("a = ", a)
print(type(a))
print('\n')


# Binary Types    :	bytes, bytearray, memoryview
print('Binary Types : ------------------ ')

# Hexadecimal
x = hex(246)
print("Hexadecimal of x :", x)


# Using the function bin() you can convert numbers into their binary format.
x = bin(1234)
print("Binary of 1234 :", x)
print('\n')


# Boolean Type
print('Boolean : -------------- ')
a = True
print("a = ", a)
print(type(a))


# Example
a = False
print("a = ", a)
print(type(a))
print("\n")


# Example of None
print('None : ------------')
x = None
print('None : ', x)
print(type(x))
print('\n')


# Example of complex
print('Complex : -------------')
a = 3 + 4j
print(a)
x = a.real
y = a.imag
print("real = ", x)
print("img = ", y)
print(type(a))
print("\n")


# Example of unicode
print('unicode : ------------- ')

s = u"\U0001F4A9"
print("unicode = ", s)
print("Data type :- ", type(s))
print("\n")

# Escape sequence

"""
\a      ascii(Bel) character
\b      ascii backspace (Bel) character
\f      ascii formatted (FF) character
\n      line break
\       back slash -- new line -- ignore
\'      single quit (')
\"      double quit ("")
\n      {name} character from unicode database with given a name

\r      mac or os newline
\t      tab horizontal
\000    octal value
\v      Vartical tab
\ xhh   hexadecimal value
\ uxxxx unicharacter with 16-bit hex value
\ uxxxx xxxx  unicharacter with 32-bit hex value

"""