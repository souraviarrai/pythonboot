import random
names = input('enter the names of the people: ')
list_of_names = names.split(',')
random_name = random.randint(1,len(list_of_names))
print(f'Today\'s bill will be paid by {list_of_names[random_name-1]}.')