name = '員序程馬黑來'
new_name = name[0:5]
index = len(new_name)
while index > 0:
    index -= 1
    na = new_name[index]
    print(na, end= '\t')

#other method
new = name[0:5]
correct = new[: : -1]
print(correct)

#other method
New = name[0:5][: : -1]
print(New)