import random
computer = random.randint(1, 3)
Sophia = int(input('Please enter your move (1:揼, 2:剪, 3:包): '))
if Sophia == 1 and computer == 2 or Sophia == 2 and computer == 3 or Sophia == 3 and computer == 1:
    print('Sophia wins!')
elif Sophia == 1 and computer == 3 or Sophia == 2 and computer == 1 or Sophia == 3 and computer == 2:
    print('Computer wins')
else:
    print('No winner!')
print(f'computer = {computer}')