# number = int(input('enter the number: '))
# if number > 1:
#     for i in range(2,int((number/2)+1)):
#         if(number%i == 0):
#             print(f'{number} is a not a prime number')
#             break
#         else:
#             print(f'{number} is a prime number')
# else:
#     print(f'{number} is not a prime number')


num = int(input('enter the number'))
flag = False

if num > 1:
    for i in range(2,num):
        if (num%i == 0):
            flag = True
            break
if flag:
    print(f'{num} is not a prime number')

else:
    print(f'{num} is a prime number')