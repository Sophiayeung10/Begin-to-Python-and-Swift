member = input('Are you member y? Yes or No: ')
money = float(input('PLease enter total amount of price: '))
money20 = money * 0.8
money10 = money * 0.9
money5 = money * 0.95
if member == 'yes':
    if money >= 200:
        print(f'You got 20% off = ${money20:.3f}')
    elif money >= 100:
        print(f'You got 10% off = ${money10:.3f}')
    else:
        print(f'You do not have any discount = ${money:.3f}')
else:
    if money >= 200:
        print(f'You got 5% off = ${money5:.3f}')
    else:
        print(f'You don not have any discount = ${money:.3f}')