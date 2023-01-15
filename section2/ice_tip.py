print('welcome to the tip calculator')
total_bill = float(input('what was the total bill?:$ '))
tip = int(input('what is the tip percentage you want: 10,12 or 15 ?: '))
people = int(input('how many people are there: '))
net_total_bill = round((total_bill + (total_bill * (tip/100))),2)
pay_for_each = net_total_bill / people
print(f'Each person should pay ${pay_for_each}')