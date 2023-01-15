print('welcome to our pizza order online shop')
size = input('what size of pizza do you want (s for small , m for medium and l for large): ')
price = 0
if size.upper() == 'S':
    price = 15
    print('for small size pizza, the price is $15')
    pep = input('do you want pep? yes or no')
    if pep.upper() == 'YES':
        price+=2
        cheese = input('do you want cheese? yes or no')
        if cheese.upper() == 'YES':
            price+=1
            print(f'your small pizza with pep and cheese costed you ${price}')
        else:
            print(f'your small pizza with pep costed you ${price} ')
    else:
        print(f'your small pizza costed you ${price} ')

elif size.upper() == 'M':
    price = 20
    print('for medium size pizza, the price is $20')
    pep = input('do you want pep? yes or no')
    if pep.upper() == 'YES':
        price+=3
        cheese = input('do you want cheese? yes or no')
        if cheese.upper() == 'YES':
            price+=1
            print(f'your medium pizza with pep and cheese costed you ${price}')
        else:
            print(f'your medium pizza with pep costed you ${price} ')
    else:
        print(f'your medium pizza costed you ${price} ')
elif size.upper() == 'L':
    price = 25
    print('for large size pizza, the price is $25')
    pep = input('do you want pep? yes or no')
    if pep.upper() == 'YES':
        price+=3
        cheese = input('do you want cheese? yes or no')
        if cheese.upper() == 'YES':
            price+=1
            print(f'your large pizza with pep and cheese costed you ${price}')
        else:
            print(f'your large pizza with pep costed you ${price} ')
    else:
        print(f'your large pizza costed you ${price} ')


