weight = int(input('what is your weight?: '))
height = int(input('what is your height?: '))
bmi = weight/height**2
if bmi < 18.5:
    print('under weight')
elif 18.5 < bmi < 25:
    print('normal')
elif 25 < bmi < 30:
    print('overweight')
elif 30 < bmi < 35:
    print('obese')
else:
    print('critical')
