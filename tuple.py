t1 = (3, 'Sophia', True)
t2 = (3)
t3 = ()
print(f'the type of t1 is {type(t1)}. The content of it is {t1}.')
print(f'the type of t1 is {type(t2)}. The content of it is {t2}.')
print(f'the type of t1 is {type(t3)}. The content of it is {t3}.')

#embedded
t5 = ((1, 2, 3), (4, 5, 6))
print(f'the type of t1 is {type(t5)}. The content of it is {t5}.')
v = t5[1][2]
print(v)

#different types of for in 
t8 = (1, 2, 3, 4, 5, 6)
for element in t8:
    print(element)

for element in range(len(t8)):
    print(t8[element])
