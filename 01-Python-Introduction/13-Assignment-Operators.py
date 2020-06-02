# Assignment Operators
print("Assignment Operators : \n")


"""
=   এটি হল a = 5

+=  এটি হল  c += a is equivalent to c = c + a

-=   এটি হল  c -= a is equivalent to c = c - a

*=   এটি হল  c *= a is equivalent to c = c * a

/=   এটি হল  c /= a is equivalent to c = c / a

%=   এটি হল  c %= a is equivalent to c = c % a

**=  এটি হল  c **= a is equivalent to c = c ** a

//=  এটি হল  c //=  a is equivalent to c = c //=  a

"""


a = 10
b = 5
c = a + b
print("10 + 5:", c)


#  += Add AND
c += a
print('15 += 10  : ', c)


# -= Subtract AND
c -= a
print('10 -= 5   : ', c)


# *= Multiply AND
c *= a
print('15 *= 10  : ', c)


#  /= Divide AND
c /= a
print('15 /= 10  : ', c)


# %= Modulus AND
c %= a
print('15 %= 10  : ', c)


# **= Exponent AND
c **= a
print('15 **= 10 : ', c)


#  //= Floor Division
c //= a
print('15 //= 10 : ', c)
print("\n")