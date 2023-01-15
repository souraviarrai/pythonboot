# using zip function and iterating over a list from 

name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

zipped = zip(name,animal,age)

for i,j,k in zipped:
    print(f'{i} the {j} is {k}')