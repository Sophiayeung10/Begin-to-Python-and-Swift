English_score = int(input('The English exam score you got: '))
Chinese_score = int(input('The Chinese exam score you got: '))
Math_score = int(input('The Math exam score you got: '))

if English_score >= 60 and Chinese_score >= 60 and Math_score >= 60:
    print('You did so well!')
else:
    print('You are out of your mind.')