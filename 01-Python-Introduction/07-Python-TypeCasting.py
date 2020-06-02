#  Type Conversion or Type casting

"""
Python data type conversion or type casting in python.
Type Conversion : এক টাইপ থেকে অন্য টাইপ এ কনভার্ট করা বুঝায়। একে টাইপ কাস্টিং ও বলা হয়ে থাকে।
"""
print("Type casting : --------------- \n")


# Example of integer to float convert

x = 123
print("x = ", x)
print(type(x))

y = float(x)
print("int to float = ", y)
print(type(y))
print('\n')


# Example of float to integer convert

x = 123.344
print("x = ", x)
print(type(x))

y = int(x)
print("float to int = ", y)
print(type(y))
print('\n')


# How to convert string to integer

"""
a = "Hello World"
print(type(a))

b = int(a)
print("str to int = ", b)
print(type(b))

Output : ValueError: invalid literal for int() with base 10: 'Hello World'

"""


# স্ট্রিং থেকে ইন্টেজার এ কনভার্ট এর সময় খেয়াল রাখতে হবে স্ট্রিং এ যাতে কোনো নননিউমেরিক ক্যারেকটার না থাকে।
# যেমন :- a = "123x" ValueError: invalid literal for int() with base 10: '123x'

a = "12345"
print(a)
print(type(a))

b = str(a)
print("str to int = ", b)
print("\n")


# Example of number to string
a = 100
print("a = ", a)
print(type(a))

c = str(a)
print("number to str = ", c)
print(type(c))
print("\n")


# Example of convert integer to binary string
a = 123
print('a =', a)
b = bin(a)

print("int to bin = ", b)
print("\n")


# Rounding Number
# round(number[n digit]

print("Round Number ")

x = 69.23456789
y = round(x, 2)
print("round : ", y)
print('\n')


# Demonstrate Type conversion using  ord(), hex(), oct(), bin()


# Example of ascii character,
# python use ord() function to know ascii character.

x = 'a'
print('x = ', x)

y = ord(x)
print('ascii character =', y)
print('\n')

# Example

a = '@'
print('x =', a)

b = ord(a)
print('ascii character =', b)
print("\n")


# Example

print('ascii character of  =', ord('z'))
print('\n')


# Example of hex()

a = 97
print("a = ", a)

b = hex(56)
print('hex of 97 =', b)
print('\n')


# Example of hex

print("hex of 234 =", hex(234))
print('\n')


# Example of binary

x = 123
print('x =', x)
y = bin(x)
print('binary of 123 =', y)


# More Example of binary
print('binary of 55 =', bin(55))
print('\n')


# Example of  oct

c = oct(97)
print(c)

# Example of oct
print('oct ot 11 =', oct(11))
