
# Now learn None

"""
None হোল  NoneType এর একিট object যা দিয়ে আসেল value এর absent  নিধারন  করে  দেয়া যায়।
অনান্য ডাটা টাইেপর যেমন একািধক ভ্যালু থাকতে পারে  Ȳযমন - bool টাইেপর দেু টা  ভ্যালু হেত পাের; True অথবা
False. NoneType এর একটাই  ভ্যালু আর সেটা হল এই None .
None মােন False না। আবার এর মােন 0 , "" , [] এসবও না।
"""

a = None == False
print(a)

# Example
b = None == ""
print(b)


# Example
c = None == []
print(c)


# Example
d = None == 0
print(d)


# Example
e = None == None
print(e)


# Example
x = None
print(x)
y = type(x)
print(y)


def my_func(x = None):
    if x:
        return x * x
    else:
        return 0


print(my_func())
print(my_func(5))
