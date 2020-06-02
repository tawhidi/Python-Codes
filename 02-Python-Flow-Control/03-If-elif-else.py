
# Syntax of if elif else
print('if elif else : ---------------- \n')

"""
if test expression:
    Body of if
elif test expression:
    Body of elif
else:
    Body of else
"""


# Example
num = 7
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")
print("\n")


# Example
name = "sakib"
if name is 'sakib':
    print("Hi Sakib")
elif name is 'jibon':
    print('Hi, Jibon')
else:
    print("Sakib is not here ! ")
print('\n')


# Now write a program to Academic Result

mark = int(input('Enter your mark :'))

if mark >=80 and mark <=100:
    print('A + Grade ')

elif mark >=75 and mark <=79:
    print('A Grade ')

elif mark >=70 and mark <=74:
    print('A- Grade')

elif mark >=65 and mark <=69:
    print(' B+ Grade')

elif mark >=60 and mark <=64:
    print('B Grade')

elif mark >=55 and mark <=59:
    print('B- Grade')

elif mark >=50 and mark <=54:
    print('C+ Grade ')

elif mark >=45 and mark <=49:
    print('C Grade')

elif mark >=40 and mark <=44:
    print('D Grade')

elif mark >=00 and mark <=39:
    print('Fail try again')

else:
    print('\n Number in not in range')

print('\n')