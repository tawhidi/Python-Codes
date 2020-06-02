
# Python Functions
print('Python Functions : --------------- \n')


# কম্পিউটার প্রোগ্রামিং -এ দুটি টার্ম শুনতে পাওয়া যায়। WET এবং DRY.

"""
WET : Write Everything Twice
DRY : Do not Repeat Yourself.
"""


# Function in python

"""
    Function :- Function হোল organized and reusable unit code এর একটি blog.
    Function একটির বেশি data return করতে পারে না । 
    Function : 
    1. built-in and 
    2. user defined
    আর Function শেষ হবে return keyword দ্বারা । 
"""


# Explanation

"""
    একটি ফাংশন আসলে কিছু স্টেটমেন্টের সংকলন ।
    যখনই কোন ফাংশন কল করা হয় তখন এই ফাংশনের ভিতরে থাকা স্টেটমেন্টগুলো এক্সিকিউট করা হয় ।
    পাইথনে আমরা ফাংশন ডিক্লেয়ার করার জন্য def কি-ওয়ার্ডটি ব্যবহার করি ।

    def hello():
        print("Hello World!")

    প্রথমে আমরা def কি-ওয়ার্ডটি লিখেছি । তারপর ফাংশনের একটা নাম দিয়েছি – hello, এবং তারপর একজোড়া প্রথম বন্ধনী ().
    এরপর একটি কোলন তথা : চিহ্ন দিয়ে এর নিচে ফাংশনের আওতাভুক্ত কোড ব্লক বা ফাংশনের কাজ ডিফাইন (নির্ধারণ) করেছি।
    ফাংশনটির কাজ হচ্ছে “Hello world!” বাক্যটি প্রিন্ট করা।

     Note: কিন্তু এভাবে একটা ফাংশনকে প্রোগ্রামের মধ্যে শুধু ডিফাইন করে রেখে দিলে তার মধ্যের কোড বা ইন্সট্রাকশন
     গুলো এমনি এমনি কাজ করবে না। এর জন্য ওই ফাংশনটিকে তার নাম ধরে কল করতে হবে। কল কিভাবে করতে হয়?
"""


# Syntax of Function

""" 
def Function_Name(parentheses / Argument):
        Statement 1
        Statement 2
        return expression

# Called the function
Function_Name( )

"""


# Example
def hello():
    print("Hello World!")


# Calling the function to use it
hello()


# Example
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


greet('Jibon')
print('\n')


# Example
def my_name(name):  # Here name is argument
    print("Given Name", name)
    return name


my_name('Jibon Ahmed')
print('\n')


# We can use variable value not parameter
def variable_value(name):
    print(name)
    return name


variable1 = "Jibon Ahmed"
variable2 = "Jayed Hossain"
variable_value(variable1)
variable_value(variable2)
print('\n')


# Function Argument
print('Function Argument :\n')


def add(a, b, c):
    return a + b + c


temp = add(2, 4, 5)
print('add :', temp)
print('\n')


# Example
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(7, 8)
print('Addition    : ', result1)
print('Subtraction :', result2)
print('\n')


# Example
def make_sum(x, y):
    z = x + y
    print('Sum : ', z)


make_sum(4, 6)
print('\n')


# Example of show double
def show_double(x):
    print(x * 2)


show_double(3)
show_double(200)
print('\n')


# Example
def update(x):
    x = 8
    print(x)


update(10)
print('\n')


# Pass by the value pass by reference
print('Pass by the value pass by reference : ')


def update_now(x):
    x = 8
    print('x :', x)
    return x


a = 10
update_now(a)
print('a : ', a)
print('\n')


# Example
def update_now(x):
    print(id(x))
    x[1] = 25
    print(x)


x = [10, 20, 30, 40, 50]
print(id(x))
update_now(x)
print('x :', x)
print('\n')


"""
    আমরা ফাংশন বা প্যারামিটার যে আর্গুমেন্ট ব্যবহার করি এদেরকে চার ভাগে ভাগ করতে পারি 
    1. Requirement Argument
    2. Keyword Argument
    3. Default Argument
    4. Variable length Argument
"""