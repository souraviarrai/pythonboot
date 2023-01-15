height = int(input('what is your height: '))
if height > 120:
    age = int(input('what is your age: '))
    picture = input('do you want a picture (yes/no): ')
    if picture.lower() == 'yes':
        if age < 12:
            print('$8')
        elif age > 12 and age < 18:
            print('$10')
        else:
            print('$13')
    else:
        if age < 12:
            print('$8')
        elif age > 12 and age < 18:
            print('$10')
        else:
            print('$13')
else:
    print('you can\'t ride sorry')