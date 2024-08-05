#the sum of number between 1 to 100
i = 1
sum = 0
for i in range(1, 101, 1):
    print(i, end= '\t')
    sum += i
print(f'sum = {sum}')

#use while
i = 1
sum = 0
while i <= 100:
    print(i, end= '\t')
    sum += i
    i += 1
print(f'sum = {sum}')