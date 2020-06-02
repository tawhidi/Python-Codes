# Default Argument
print('Default Argument :-')


def my_default_argument(a, b=7):
    print('a                :', a)
    print('default argument :', b)


my_default_argument(2)


#  Example of override existing default value
def person_info(name, age=18):
    print('Name     :', name)
    print('default  :', age)


person_info('Jui', 23)  # override the default age
print('\n')