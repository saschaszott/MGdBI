"""
Primfaktorzerlegung von großen Zahlen mit sympy.
"""

from sympy import factorint
print(factorint(24))
print(factorint(36))
print(factorint(1024))

p = 10**44 + 151 # 45-stellige Zahl
q = 10**44 + 271 # 45-stellige Zahl
print(p * q)
print(factorint(p * q))
