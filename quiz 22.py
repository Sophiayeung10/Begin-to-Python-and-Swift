age = [21, 25, 21, 23, 22, 20]
age.append(31)
print(age)
#[29, 33, 30]
age.extend([29, 33, 30])
print(age)
n = age.pop(0)
print(n)
m = age.pop(8) #it would be cancel
print(m)
vb = age.index(31)
print(vb)

name = [1, 2, 3]
index = name.index(3)
print(index)