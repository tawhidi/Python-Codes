
# if else statement
print("If else statement : ----------------- \n")

"""
if কন্ডিশন সত্য হলে তার আওতাভুক্ত কোড ব্লকটি রান হয়। else বস্তুত if এর সাথেই সম্পর্কিত।
যদি if কন্ডিশনটি সত্য না হয় তাহলে else এর আওতাভুক্ত কোডব্লক রান বা এক্সিকিউট হয়।

মজার ব্যাপার হচ্ছে এরকম if else if এর চেইনকে একটু সংক্ষেপে elif দিয়েও লেখা যায়।
"""


# Syntax if else
"""
if test expression:
    Body of if
else:
    Body of else

Or

if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false
"""


# Example
x = 4
if x == 5:
    print("it's 5")
else:
    print("it's not 5")
print("End program")
print('\n')


# Boolean Check
x = False
if x:
    print("x was True")
else:
    print("I will print when x is anything not True")


# Boolean Check
x = False
if x:
    print("x was True")
else:
    print("I will print when x is anything not True")


# Example
a = 10
b = 20
if a > b:
    print('a is getter than b')
else:
    print('a is less than b')
print('\n')


# Example
i = 20
if i < 15:
    print(i, "is smaller than 15")
    print("i'm in if Block")

else:
    print(i, "is greater than 15")
    print("i'm in else Block")

print("i'm not in if and not in else Block")
print('\n')


# Example
loc = "bank"
if loc == "Auto Shop":
    print('Welcome to Auto Shop')

elif loc == "bank":
    print("Welcome to the bank")

else:
    print("Where are you ?")

print('\n')


# Example
person = "shampa"

if person == "shampa":
    print("hi, Shampa")
else:
    print("What's your name ?")

# Condition is true
print(person == "shampa")
print('\n')


# Example
status = 'password'
mess = "Logout" if status == 'password' else "Login"
print(mess)

status = 7
mes = "Logout" if status == 5 else "Login"
print(mes)
print("\n")


# Example
a = int(input('a = '))
b = int(input('a = '))
if a > b:
    print('a is getter than b')
else:
    print('a is less than b')
print('\n')


# Example of Password Match
username = ["jon", "joy", "wood"]
password = ['jon123', '123joy', 'wood260']

n = input('Username: ')
p = input('Password: ')
if n in username and p in password:
    print('Log in')
else:
    print('Username or password incorrect')
print("try again !")
print('\n')


# Nested if else

a = 109
b = 208
c = 307

if a > b:
    if a > b:
        print("A is Large Number ", a)
    else:
        print("B is large number", b)
else:
    if b > c:
        print('Large Number is ', b)
    else:
        print("Large number is ", c)
print('\n')


# Write a program to take three number and which are are large
print('Which number is large : ')

a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter third  Number : "))

if a > b:
    if a > b:
        print("A is Large Number : ", a)
    else:
        print("B is large number : ", b)
else:
    if b > c:
        print('B is Large number  :  ', b)
    else:
        print("C is Large number : ", c)

print('\n')