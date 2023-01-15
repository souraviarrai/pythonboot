print('welcome to my pizza shop')
size = input('what size small s , meium m or large l')
pep = input('do you want pep yes or no')
cheese = input('do you want cheese yes or no')
bill = 0

if size.upper() == 'S':
    bill += 15

elif size.upper() == 'M':
    bill += 20

elif size.upper() == 'L':
    bill += 25

if pep.upper() == 'YES':
    if size.upper() == 'S':
        bill += 2
    else:
        bill += 3
if cheese.upper() == 'YES':
    bill += 1
print(f'The total bill is ${bill}')

