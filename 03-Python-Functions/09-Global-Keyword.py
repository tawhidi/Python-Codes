
#  Global Keyword

# Rules of global Keyword

"""
The basic rules for global keyword in Python are:

1 When we create a variable inside a function, it’s local by default.
2 When we define a variable outside of a function, it’s global by default.
You don’t have to use global keyword.
3 We use global keyword to read and write a global variable inside a function.
4 Use of global keyword outside a function has no effect
"""

# Example
c = 0  # global variable


def add():
    global c  # আমরা global keyword দ্বারা  global variable কে only access করতে পাড়বো
    c = c + 2
    print("Inside add():", c)


add()
print("In Main :", c)
print('\n')


# Example of global variable
a = 10


def do_something():
    global a
    a = 15
    print('Inside the function', a)


do_something()
print('Outside of function', a)
print('\n')


# Using a Global Variable in Nested Function

def book():
    x = 69

    def khata():
        global x
        x = 75
    print("Call Book Function :", x)
    khata()
    print("Call Khata Function :", x)


book()
print('X is main :', x)
print('\n')

# Nonlocal Variables

"""
Nonlocal variable are used in nested function whose local scope is not defined
We use nonlocal keyword to create nonlocal variable.
We use nonlocal keyword to create nonlocal variable.
"""


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner :", x)
    inner()
    print("outer :", x)


outer()
