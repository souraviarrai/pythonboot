print('welcome to the game of choices ')
direction = input('which way you want to go: left or right: ')
if direction.lower() == 'left':
    swim = input('do you want to swim or wait : ')
    if swim.lower() == 'swim':
        print('gave over')
    else:
        door = input('which color door you want to enter : red , blue , yellow: ')
        if door.lower() == 'red':
            print('gave over')
        elif door.lower() == 'blue':
            print('gave over')
        elif door.lower() == 'yellow':
            print('you win the game')
else: 
    print('game over')