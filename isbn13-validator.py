isbn13 = '9783864903847'
sum = 0
for i, digit in enumerate(isbn13):
    # Stellennummern i beginnen bei 0
    n = int(digit)
    if i % 2 == 0:
        sum += n
    else:
        # dreifache Gewichtung von ungeraden Stellen
        sum += n * 3

if sum % 10 == 0:
    print(f'{isbn13} is valid')
else:
    print(f'{isbn13} is NOT valid')