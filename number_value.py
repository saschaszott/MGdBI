base = 2
number = '11101'
value = 0
position = 0
for digit in reversed(number):
    if digit != '0':
        value += (base ** (position)) * int(digit)
    position += 1
print(f"(Decimal) Value of {number} is: {value}")