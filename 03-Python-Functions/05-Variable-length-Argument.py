# Variable length Argument


# * argument দিয়ে আমারা tuple অকারে ভালু গুলো পাব ।
print('Variable length Argument :-')


def my_sum(a, *b):
    print('a  :', a)
    print('*b :', b)
    print(type(b))


my_sum(2, 3, 4, 5, 6)
print('\n')


# Example
def total_sum(a, *b):
    c = a
    for i in b:
        c = c + i
        print('total sum :', c)


total_sum(5, 1, 2, 3, 4)
print('\n')


# Example
def calculate(*b):
    c = 0
    for i in b:
        c = c + i
    print('Calculate sum :', c)


calculate(1, 4, 6, 7, 89, 82, 48, 45)
print('\n')


# Keyword Variable length Arguments
print('Keyword Variable length Arguments :- \n')

"""
** kwargs আমারা multiple নিতে পারবো । আর এই data গুলো dictionary হিসাবে থাকবে । 
"""


def personal_details(name, **other):
    print('name       :', name)
    print('other info :', other)
    print(type(other))


personal_details('Jibon', age=24, dept='Swe', roll=969)
print('\n')


# Mixed Argument
print('Mixed Argument :-')


def mixed_argument(a, *args, **kwargs):
    print('a        :', a)

    print('*args    :', args)
    print('type     :', type(args))

    print('**kwargs :', kwargs)
    print('type     :', type(kwargs))


mixed_argument('Hello', 7, 8, 9, id=69, address='dhaka')
print('\n')


# Example একটি Function return করতে পারবে multiple value.
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(23, 1)
print(result1)
print(result2)
print('\n')
