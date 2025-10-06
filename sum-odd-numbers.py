"""
Berechnung der Summe der ersten n = 100 ungeraden Zahlen.
"""

n = 100
sum = 0
for i in range(1, n + 1):
    sum += (2 * i - 1)
print(f"Sum of first {n} odd numbers is: {sum}")