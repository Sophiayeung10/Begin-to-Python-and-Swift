#withdrawal in bank
money = 7034.7
withdraw_the_money = float(input('Please enter the amount of money you want to withdraw: '))
if money >= withdraw_the_money:
    print(f'Here is your amount $%4d' %(withdraw_the_money))
else:
    print('You don not have enough money!')
withdrawal = input('Do you need to get back your card? Yes or no: ')
if withdrawal == 'yes' or withdrawal == 'Yes':
    print('Here is your card')
else:
    print('other opinions')