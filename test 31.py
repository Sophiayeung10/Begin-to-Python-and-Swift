#sum of 1 to 100 (incorrect)
i = 1
while i <= 100:
    i += 1
    sum = 0
    sum += i

#sum of 1 to 100 (correct)
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f'sum = {sum}')

