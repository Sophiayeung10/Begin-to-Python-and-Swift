num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a number: '))
num3 = int(input('Please enter a number: '))

if num1 > num2 and num1 > num3:
    print('num1 = {num1} is the largest number')
elif num2 > num1 and num2 > num3:
    print('num2 = {num2} is the largest number')
elif num3 > num1 and num3 > num2:
    print('num3 = {num3} is the largest number')
else:
    print('The set has equal values')