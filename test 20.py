num1 = int(input('PLease enter a number: '))
num2 = int(input('Please enter a second number: '))

#short if-else
max = 'num1' if num1 > num2 else 'num2'
print(f'max = {max}')

#longer if-else
if num1 > num2:
    print('num1')
else:
    print('num2')