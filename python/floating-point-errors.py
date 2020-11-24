from decimal import *
import math
#   LINK: https://docs.python.org/3/tutorial/floatingpoint.html
#   LINK: https://docs.python.org/3/library/decimal.html
#   LINK: https://blog.tecladocode.com/decimal-vs-float-in-python/

#   Example of 'problem' with floating point numbers:
a = 1.1
b = 2.2
print("%s + %s using floats:" % (str(a), str(b)))
print(a+b)
print()
#>>     1.1 + 2.2 using floats:
#>>     3.3000000000000003


a = Decimal('1.1')
b = Decimal('2.2')
print("%s + %s using decimals:" % (str(a), str(b)))
print(a+b)
print()
#>>     1.1 + 2.2 using decimals:
#>>     3.3


#   using float literals results in decimal values with the same value as the float approximation of 1.1 and 2.2
a = Decimal(1.1)
b = Decimal(2.2)
print("%s + %s using decimals from floats" % (str(a), str(b)))
print(a+b)
print()
#>>     1.100000000000000088817841970012523233890533447265625 + 2.20000000000000017763568394002504646778106689453125 using decimals from floats
#>>     3.300000000000000266453525910


#   Simple solution for exact values - convert floats to string, then to decimals
a = Decimal(str(1.1))
b = Decimal(str(2.2))
print("%s + %s using decimals from floats" % (str(a), str(b)))
print(a+b)
print()
#>>     1.1 + 2.2 using decimals from floats
#>>     3.3


#   Convert float to decimals using context
context = Context(prec=20, rounding=ROUND_DOWN)
a = context.create_decimal_from_float(1.1)
b = context.create_decimal_from_float(2.2)
print("%s + %s using decimals from decimal context" % (str(a), str(b)))
print(a+b)
print()
#>>     1.1000000000000000888 + 2.2000000000000001776 using decimals from decimal context
#>>     3.3000000000000002664


