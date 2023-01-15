fact = int(input('enter the number: '))
factorial = 1
if fact < 0:
    print('no factorial for negative numbers')
elif(fact == 0):
    print('factorial of 0 is 1')
else:
    for i in range(1,fact+1):
        factorial = factorial * i
print(factorial)