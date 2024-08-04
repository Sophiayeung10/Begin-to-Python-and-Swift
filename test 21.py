num1 = int(input('Please enter the first number: '))
num2 = int(input('PLease enter the second number: '))
num3 = int(input('Please enter the third number: '))

max = num1 if num1 > num2 else num2
Themax = max if max > num3 else num3
print(f'max = {Themax}')