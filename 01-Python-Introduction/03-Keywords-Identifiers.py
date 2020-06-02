# Python Keywords
print('Python Keywords : ---------------- ')


# Keywords are the reserved words in Python.

"""
We cannot use a keyword as a variable name, function name or any other identifier. 
They are used to define the syntax and structure of the Python language.
In Python, keywords are case sensitive.
"""


# Reserved keywords Words

"""
    and         exec        not
    assert      finally     or
    break       for         pass
    class       from        print
    continue    global      raise
    def         if          return
    del         import      try
    elif        in          while
    else        is          with
    except      lambda      yield

"""

# How to see all keyword in IDLE --> Go to IDLE >>> help() then >>> keywords
print(help('keywords'))
print('\n')

# or

""" 
import keyword
print(keyword.kwlist)  # kwlist  দ্বারা আমরা keyword এর সব লিস্টগুলো দেখতে পাড়বো

"""


# Python Identifiers
print('Python Identifiers : ------------------ ')

"""
An identifier is a name given to entities like class, functions, variables, etc. 
It helps to differentiate one entity from another.
"""


# Rules for writing identifiers

"""
    1. Identifiers can be a combination of letters in lowercase (a to z) 
        or uppercase (A to Z) or digits (0 to 9) or an underscore _. 
        Names like myClass, var_1 and print_this_to_screen, all are valid example.
        
    2. An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
    
    3. Keywords cannot be used as identifiers.
    
    # Example
    '''
        >>> global = 1
            File "<stdin>", line 1
            global = 1
                     ^
        SyntaxError: invalid syntax
        >>>
    '''
    
    4. We cannot use special symbols like !, @, #, $, % etc. in our identifier.
    
    # Example 
    '''
    >>> a@ = 0
      File "<stdin>", line 1
        a@ = 0
           ^
    SyntaxError: invalid syntax
    >>>
    '''
    
    5. An identifier can be of any length.
    
"""


# Naming conventions for Python identifiers.

"""
    1. Class names start with an uppercase letter. and All other identifiers start with a lowercase letter.
    2. Starting an identifier with a single leading underscore indicates that the identifier is private.
    3. Starting an identifier with two leading underscores indicates a strongly private identifier.
"""


# Things to Remember

"""
Python is a case-sensitive language. This means, Variable and variable are not the same.

Always give the identifiers a name that makes sense. 
While c = 10 is a valid name, writing count = 10 would make more sense, 
and it would be easier to figure out what it represents when you look at your code after a long gap.
"""

# Multiple words can be separated using an underscore, like this_is_a_long_variable.

