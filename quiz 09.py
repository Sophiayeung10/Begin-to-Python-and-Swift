choice = 1223
for i in range(3):
    choice = int(input('Please enter your password: '))
    if choice == 1223:
        print('Log in successful!')
        break
    else:
        if choice != 1223:
            print('Incorrect password was provided.')
        if i == 2: #no need to write because range(3) will end when i == 2
            print('Addmission is rejected.')

