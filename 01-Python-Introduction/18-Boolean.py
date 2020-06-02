# Boolean
print('Boolean : \n')


"""
বুলিয়ান হলো এক প্রকারের ডাটাটাইপ যার মান সবসময় কোন কিছু সত্য অথবা মিথ্যা বুঝায়।
সত্য ও মিথ্যাকে যথাক্রমে 1 ও 0 দ্বারা প্রকাশ করা হয়। পাইথনে এই Boolean টাইপটির দুটি ভ্যালু আছে True এবং False
"""


# Boolean expression

'''
বুলিয়ান এক্সপ্রেশন হলো এমন কিছু এক্সপ্রেশন যেগুলো সত্য অথবা মিথ্যা মান রিটার্ন করে।
একাধিক বুলিয়ান এক্সপ্রেশন মিলেও একটি বুলিয়ান এক্সপ্রেশন বানানো যায়।
'''


# Boolean Operator
# বুলিয়ান টাইপের তিনটি বেসিক অপারেটর আছে। এরা হলো AND , OR , NOT

"""
AND এর বেলায় যদি সবগুলো ভ্যারিয়েবল এর মান সত্য হয় তবে এক্সপ্রেশন টি সত্য হয়, অন্যথায় এক্সপ্রেশন টি মিথ্যা হয়।
OR এর বেলায় যদি কমপক্ষে একটি ভ্যারিয়েবল এর মান সত্য হয় তবে এক্সপ্রেশন টি সত্য হবে, আর অন্যথায় এক্সপ্রেশন টি মিথ্যা ।
NOT একটি ইউনারি অপারেটর। এটি সাধারনত কোনো ভ্যারিয়েবল অথবা এক্সপ্রেশন এর বিপরীত ভ্যালু রিটার্ন করে।

# এই বেসিক এপারেটর ছাড়াও আরো কিছু অপারেটর আছে যেগুলো হল যেমনঃ XOR, XAND, NAND, NOR
"""


# Truth table

"""
A	B    A AND B	A OR B	 NOT A

0	0	   0	       0	     1
0	1	   0	       1	     1
1	0	   0	       1	     0
1	1	   1	       1	     0
"""


# AND Operator
x = 5
y = 6
z = x == 5 and y == 6
print("And :", z)


# OR Operator
x = 5
y = 6
z = x == 2 or y == 9
print("Or  :", z)
print("\n")


# NOT Operator
a = not 13 > 7
print("not 3 > 2 : ", a)


# Some Example of Boolean Operator

# Example
x = bool(28)
print("bool(28)    : ", x)


# Example
y = bool(-2.1996)
print("bool(-2.69) : ", y)


# Example
z = bool(0)
print("bool(0)     : ", z)
print("\n")


# Boolean String
x = bool("Python")
print(x)


# int Boolean
a = int(True)
print(a)
print('\n')


# Example
b = int(False)
print(b)
print('\n')


# Example
c = 5 + True
print("5 + True   : ", c)
print('\n')


# Example
d = 10 * False
print("10 * False : ", d)


# None
a = None
print(a)

# Boolean Logic
"""
if স্টেটমেন্টের জন্য জটিল কন্ডিশন তৈরির ক্ষেত্রে বুলিয়ান লজিক ব্যবহৃত হয়ে থাকে।
একটি if স্টেটমেন্ট যদি একাধিক কন্ডিশনের উপর নির্ভর করে সেখানে আমরা বুলিয়ান লজিক ব্যবহার করতে পারি।
পাইথনে and, or এবং not এই তিন ধরণের বুলিয়ান অপারেটর আছে।
অন্যান্য প্রোগ্রামিং ল্যাঙ্গুয়েজে এ ধরণের AND, OR বা NOT অপারেটরকে সাধারণত &&, ||, ! দিয়ে প্রকাশ করা হয় 
"""
