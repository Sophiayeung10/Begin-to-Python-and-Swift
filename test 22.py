score = int(input('Please enter your score: '))
# the range of score should be 0 to 100
if 0 <= score <= 100:
    if score >= 80:
        print('You are excellent!')
    elif score >= 70:
        print('You are great!')
    elif score >= 60:
        print('Good.')
    else:
        print('Bad Ass.')
else:
    print('The score is illegal.')