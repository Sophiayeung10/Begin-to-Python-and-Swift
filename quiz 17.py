list = [1, 2, 3, 4]
list.append(5)
print(f'list = {list}, type(list) = {type(list)}')

list2 = [6, 7, 8, 9]
list.extend(list2)
print(list)