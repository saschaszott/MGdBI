"""
Berechnung der Summe der Quadrate der ersten n = 6 natürlichen Zahlen.
"""

n = 6
sum = 0
for i in range(1, n + 1):
    sum += (i * i)
print(f"Sum of squares of first {n} natural numbers is: {sum}")