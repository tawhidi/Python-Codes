
# Python Input Function
print('Python Input Function : ------------------ \n')

# Input Function কেন ব্যবহার করব ? ইউজার এর কাজ থেকে data input নেওয়ার জন্য আমারা ব্যবহার  করবো ।


# Example of input all type of data. এখন আমি চাই ইউজার যাই ইনপুট দিবে তাই দেখাব... Symbols @
x = input("Enter everything you want : ")
print(x)


# Input only integer value
"""
এইখানে ও integer নাম্বার ছাড়া আর  কিছুই ইনপুট নিবেনা । কারন আমি বলে দিছিয়ে int(input("Enter a integer number : "))
"""
user_input = int(input("Enter only integer number : "))
print(user_input)


# Input only Floating point number
x = float(input("Enter your floating Point number : "))
print(x)
print('\n')


# Example of eval. তবে eval এ শুধু মাত্র নাম্বার স্ট্রিং কে যোগ করা যায় ।
z = eval("2+3")
print("Eval means string addition : ", z)
print('\n')


# Example of split ()
# split এর কাজ হোল প্রত্যকটি sentence কে string আকারে লিস্ট এর মদ্যে রাখবে ।

x = "How to learn python"
y = x.split()
print("split = ", y)

# split() দ্বারা কোন ওয়ার্ড কে remove করতে পারি ।
a = "How to remove spit"
b = a.split('o')
print('Remove = ', b)
print('\n')


# Example of split
a = "As you can see from this code, the function splits our original string"
b = a.split()
print(b)
print("\n")


# Example of charter input
ch = input('Enter a char ')[0]
print(ch)


"""
# or
myChar = input('Enter a char ')
print(myChar[0])
"""


# Take two number and there sum
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
sum = a + b
print(a, '+', b, '=', sum)  # a + b =
print('{} + {} = {}'.format(a, b, sum))
print(str(a) + ' + ' + str(b) + '=', sum)
print('\n')


# Age calculator
user_input = int(input("Enter your birth year : "))
age = 2019 - user_input
print('your age is ', age)
print('\n')


# Example of Age calculator
user_input = int(input("বাংলা জন্ম সাল : "))
age = 1426 - user_input
print('your age is ', age)
print('\n')

