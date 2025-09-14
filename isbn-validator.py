isbn10 = '3960091877' # Git – kurz & gut 
sum = 0
position = 1

for i in isbn10:
    if i == 'X':
        digit = 10
    else:
        digit = int(i)
    sum += digit * position
    position += 1

if sum % 11 == 0:
    print(f"{isbn10} is a valid ISBN-10")
else:
    print(f"{isbn10} is NOT a valid ISBN-10")