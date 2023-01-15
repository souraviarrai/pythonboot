height = int(input('what is your height?: '))
if height > 120:
    age = int(input('what is your age?: '))
    if age > 18:
        print('access granted with $10 fee')
    else:
        print('accsss grated with $5 fee')
else: 
    print("you can't ride")