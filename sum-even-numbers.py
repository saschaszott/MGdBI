"""
Berechnung der Summe der ersten n = 100 geraden Zahlen.
"""

n = 100
sum = 0
for i in range(1, n + 1):
    sum += (2 * i)
print(f"Sum of first {n} even numbers is: {sum}")