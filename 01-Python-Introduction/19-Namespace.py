
# Python Namespace and Scope
print('Python Namespace and Scope : \n')


# What is Name in Python ?

"""
Name (also called identifier) is simply a name given to objects. 
Everything in Python is an object. Name is a way to access the underlying object.
"""


# Example
a = 3   # here 3 is an object stored in memory . a is the name we associate it with.
print(a)
# Output id(3) =  1831454448
print('id(3) = ', id(3))

# Output id(a) =  1831454448
print("id(a) = ", id(a))
print('\n')


# Example
a = 2
# Output : id(a) =  1831454416
print("id(a) = ", id(a))

a = a + 1
# Output : id(a) =  1831454448
print("id(a) = ", id(a))


# Output : id(a) =  1831454448
print("id(3) = ", id(3))
print('\n')


# Python Variable Scope

"""
Although there are various unique namespaces defined, 
we may not be able to access all of them from every part of the program.
A scope is the portion of a program from where a namespace can be accessed directly without any prefix
"""


# At any given moment, there are at least three nested scopes.
"""
    1. Scope of the current function which has local names
    2. Scope of the module which has global names
    3. Outermost scope which has built-in names
"""


# Example of Scope and Namespace in Python

""" 
def outer_function():
    b = 20  # b is in the local namespace

    def inner_func():
        c = 30  # c is in the nested local namespace


a = 10  # a is in the global namespace
"""


# Example
def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)