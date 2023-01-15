height = int(input('what is your height: '))
bill = 0
if(height >= 120 ):
    print('you can ride')
    age = int(input('what is your age: '))
    if age < 12:
        bill = 5
        print(f'for {age} your bill is $5')
    elif age > 12 and age < 18:
        bill = 8
        print(f'for {age} your bill is $8')
    elif age >= 45 and age <= 55:
        price = 0
        print(f'you can ride for ${price}')
    else:
        bill =10
        print(f'for {age} your bill is $10')
    
    photo_want = input('do you want a photo? (yes or no): ')
    if photo_want.lower() == 'yes':
        if age >= 45 and age <= 55:
            bill = 0
        else:
            bill += 3
        
    print(f'your final bill is ${bill}')


else:
    print('you can\'t ride sorry')