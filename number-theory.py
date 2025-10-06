"""
Berechnung des größten gemeinsamen Teilers (ggT) und des kleinsten gemeinsamen Vielfachen (kgV) zweier Zahlen.
"""

import math

a = 4
b = 10
# greatest common divisor
gcd = math.gcd(a, b)
# least common multiple
lcm = math.lcm(a, b)
print(f"ggT({a}, {b}) = {gcd}")
print(f"kgV({a}, {b}) = {lcm}")