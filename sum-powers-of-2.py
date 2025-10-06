"""
Berechnung der Summe der ersten n + 1 = 10 Zweierpotenzen, beginnend bei 2^0.
"""

n = 9
sum = 0
for i in range(0, n + 1):
    sum += (2 ** i)
print(f"Sum of first {n + 1} powers of 2 is: {sum}")