list = ('Sophia', 11, ['football', 'music'])
Q1 = list.index(11)
print(Q1)
Q2 = list[0]
print(f'The name of the student is {Q2}.')
Q3 = list[2]
del Q3[0]
print(list)
Q4 = Q3.append('coding')
print(list)