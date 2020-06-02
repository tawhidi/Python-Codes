
# Python List

"""
1. Creating List
2. Nesting list
3. How to access elements from a list.
4. indexing and slicing List
5. Basic list Method
6. Built-in Functions with List
"""

"""
    list এ আমার বিভিন্ন ধরনের ডাটা রাখাতে পারি । 
    লিস্ট এর ভেলু কে পাওয়ার জন্য আমারা index কে call করতে হবে । 
    আর index শুরু হয় [0] and  [-1] end.
"""


# Creating List
print('How to Creating List :\n')
a = list()
b = []
c = [1, 2, "List", 1.5, ]
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print('\n')


# Example of nested list
print("Nested list :\n")
my_list = ["python", [8, 4, 6], ['a']]
print(my_list)
print('\n')


# How to access elements from a list.
"""
    We can use the index operator [] to access an item in a list. 
    Positive indexing start from  :   0
    Negative indexing  start from : - 1
"""

print('How to access elements from a list :\n')
my_list = [1, 2, 3, 'hello', 6.7, 'world']
print('all index   :', my_list)
print('first index : ', my_list[0])
print('2nd index   :', my_list[2])
print('4th index   :', my_list[4])
print('Negative last index  :', my_list[-1])
print("\n")


# Nested List to access element
print("Nested List to access element :\n")

true = 'This is true'
d = [1, 2, 3, 4, ['hello', 'world', 6.9, 5, True], True, true]
print('all list             :', d)         # all list
print('1st index            :', d[1])      # 1st index
print('4th index            :', d[4])      # 4th index
print('4th index 2nd index  :', d[4][2])   # 4th index 2nd index  nested list
print('4th index 4th index  :', d[4][4])   # 4th index 4th index  nested list
print("\n")


# List indexing and slicing
print('list indexing and slicing :\n')
list1 = ['one', 2, 3, 4, 5, 6, 'Seven', 8, 9, 10, 'end', True]
print('All list         :', list1)          # Print all list
print('all list         :', list1[:])       # Print all list
print('Length list      :', len(list1))     # Length of the list
print('first index      :', list1[0])       # First index value
print('last index       :', list1[-1])      # last index value
print('1st to 3 index   :', list1[0:3])     # 1st to 3 index value
print('2nd to 5 index   :', list1[2:5])     # 2nd to 5 index value
print('6th to all index :', list1[6:])      # 6th index এর পর সব গুলো পাবো ।
print('Skipping 2 index :', list1[::2])     # ২ ওয়ার্ড পর পর value গুলো পাবো । For Skipping 2 index each time
print('Reverse word     :', list1[::-1])    # উল্টে দিক থেকে সবগুলো ভালু পাবো ।
print('Skipping 2 index :', list1[0:17:2])  # For Skipping 2 index each time start 0 end 27
print('\n')


# How to change or add elements to a list ?
print("Change or add elements to a list :\n")
even = [2, 4, 6, 8, 10]
print(even)
even[4] = 14    # change 4 and replace 14
print("change element :", even)


# Change 2nd to 4th items
even[1:4] = [3, 5, 7]
print("change element :", even)
print("\n")


# Example
c = [1, 2, 3, 4, ['a', 'b', 'c', 'd'], True, true]
c[1] = ['Jibon', '12', 13]
print(c[3], c[1][1])
print(str(c[3])+c[1][1])
print(str(c[3])+" "+c[1][1])
print('\n')


my_list = [3, 8, 1, 6, 0, 8, 4]

print(my_list.index(8))
print(my_list.count(8))

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print("\n")


# Basic list Method
print('Basic list Method :\n')
list2 = [1, 3, 5, 3]
list2.append(7)                 # append() we can add one item at a time
print("append    :", list2)

list2.extend(['one', 'two'])    # extend() we can add multiple item
print("extend    :", list2)

list2.remove('two')             # remove elements from a list
print('Remove    :', list2)

list2.reverse()                 # reverse() সবগুলো উল্টো দিকথেকে print করবে ।
print('reverse   :', list2)
print("\n")


# list Method
l = [1, 2, 4]
print(l)

# append() হোল অ্যাড করা ।
x = l.append(57)
print(l)
print('\n')


# pop() সে return করবে last element of the list
list = [2, 4, 6]
ab = list.pop()
print(ab)
print('\n')

#  pop(0) এখন যেই লিস্ট বা index চাই
xy = list.pop(0)
print(xy)
print('\n')


# reverse() সবগুলো উল্টো দিকথেকে print করবে ।
new_list = ['a', 'b', 'c', 'd', 'e']
x = new_list.reverse()

print(new_list)
print('\n')

# আগের মতো হবে ।
x = new_list.sort()
print('\n')


list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

print("list : ", list)

list.remove('p')# Remove 'p'
print("list : ", list)

list.pop(2)# Remove 'g'
print("List : ", list)

list.clear()
print(list)
print("\n")

'''
How to delete or remove elements from a list ?
We can delete one or more items from a list using the keyword del. 
'''


my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# delete one item o is delete
del my_list[2]
print("my_list : ", my_list)

# delete multiple items
del my_list[1:5]
print("my_list : ", my_list)


# delete entire list
del my_list
print("\n")

# List matrix
print('list matrix :\n')
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]
matrix = [l_1, l_2, l_3]
print(matrix)
x = matrix[0]
print(x)

# print first list last value
x = matrix[0][2]
print(x)
print('\n')


# Built-in Functions with List
"""
Function	    Description
all()	        Return True if all elements of the list are true (or if the list is empty).
any()	        Return True if any element of the list is true. If the list is empty, return False.
enumerate()	    Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	        Return the length (the number of items) in the list.
list()	        Convert an iterable (tuple, string, set, dictionary) to a list.
max()	        Return the largest item in the list.
min()	        Return the smallest item in the list
sorted()	    Return a new sorted list (does not sort the list itself).
sum()	        Return the sum of all elements in the list.
"""



"""
লিস্টের যোগ ও গুন
মজার ব্যাপার হচ্ছে string এর মত করে লিস্ট নিয়েও যোগ বা গুনের কাজ করা যায়।
"""

first_list = [1, 2, 3]
print("List addition : ",first_list + [4, 5, 6])
print("List multiplication : ",first_list * 3)
print("\n")


"""
List element check 
"""

fruits = ["apple", "orange", "pineappe", "grape"]

print("orange" in fruits)
print("rice" in fruits)
print("apple" in fruits)
print("\n")



"""
একই ভাবে এর সাথে not অপারেটর ব্যবহার করে কোন এলিমেন্টের অনুপস্থিতিও চেক করা যাতে পারে।
"""


fruits = ["apple", "orange", "pineappe", "grape"]

print("orange" not in fruits)
print(not "rice" in fruits)
print("\n")



"""
Example 
"""

a = [12, 'python', 16.2, 4,['jibon', 6.9, 'A'], True, [1, 'B'], 9, '12']

print("a: ",a)
print("A ",a.index(True))


print("Negative indexing")

my_list = ['p', 'y', 't', 'h', 'o', 'n']

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])

print("\n")




"""
We can use remove() method to remove the given item or pop() method to remove an item at the given index.

The pop() method removes and returns the last item if index is not provided.

We can also use the clear() method to empty a list.

"""

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)

print("\n")

print('Count in list :')
l = [4, 5 , 6, 5, 7, 5]
x = l.count(5)
print(x)
print('\n')





'''

Built-in Functions with List

Function	        Description

append() -          Add an element to the end of the list
extend() -          Add all elements of a list to the another list
insert() -          Insert an item at the defined index
remove() -          Removes an item from the list
pop() -             Removes and returns an element at the given index
clear() -           Removes all items from the list
index() -           Returns the index of the first matched item
count() -           Returns the count of number of items passed as an argument
sort() -            Sort items in a list in ascending order
reverse() -         Reverse the order of items in the list
copy() -            Returns a shallow copy of the list


all()	            Return True if all elements of the list are true (or if the list is empty).
any()	            Return True if any element of the list is true. If the list is empty, return False.
enumerate()	        Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	            Return the length (the number of items) in the list.
list()	            Convert an iterable (tuple, string, set, dictionary) to a list.
max()	            Return the largest item in the list.
min()	            Return the smallest item in the list
sorted()	        Return a new sorted list (does not sort the list itself).
sum()	            Return the sum of all elements in the list.

'''


