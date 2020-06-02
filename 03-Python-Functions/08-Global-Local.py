# Global and local variable in python

""""
    Function এর ভিতরের  variable -- > Local
    Function এর বাইরের  variable  -- > Global
"""


# Example of  global variable

a = 10  # global variable


def something():

    a = 15  # local variable
    print(a)


print(a)
something()
print('\n')




# Function using for global and local variable
a = 23
print(id(a))


def hello_something():
    a = 9
    x = globals()['a']
    print(id(x))
    print('inside the function', a)
    globals()['a'] = 15


hello_something()

