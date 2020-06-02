# Example of Keyword Argument
print('Keyword Argument :- ')


def my_keyword_argument(a, b, c):
    return a + b + c


temp = my_keyword_argument(a=7, b=6, c=4)  # keyword argument a=7, b=6, c=4
print('keyword_argument :', temp)


# Example

def person(name, age):
    print('Name :', name)
    print('Age  :', age)


person(name='Hello', age=36)
print('\n')