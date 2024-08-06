choice = 1223
for i in range(3):
    choice = int(input('Please enter your password: '))
    if choice == 1223:
        print('Log in successful!')
        break
    else:
        if choice != 1223:
            print('Incorrect password was provided.')
else:
    print('Addmission is rejected.')
