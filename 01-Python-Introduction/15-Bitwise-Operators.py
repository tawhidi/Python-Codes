# Bitwise Operators
print("Bitwise operators : \n")


"""
Bitwise operator works on bits and performs bit by bit operation.

Assume if a = 60; and b = 13; Now in binary format they will be as follows −

a = 0011 1100

b = 0000 1101

Operator	Meaning	                Example

&	        Bitwise AND	            x & y       = 0 (0000 0000)
|	        Bitwise OR	             x | y      = 14 (0000 1110)
 ~	        Bitwise NOT	            ~x          = -11 (1111 0101)
^	        Bitwise XOR	            x ^ y       = 14 (0000 1110)
>>	        Bitwise right shift	    x>> 2       = 2 (0000 0010)
<<	        Bitwise left shift	    x<< 2       = 40 (0010 1000)

"""

print('5 & 6 : ', 5 & 6)  # & Binary AND  [ bin(5) '0b101' & bin(6) '0b110' ]
print('5 | 6 : ', 5 | 6)  # | Binary OR
print('5 ^ 6 : ', 5 ^ 6)  # ^ Binary XOR
print('\n')

