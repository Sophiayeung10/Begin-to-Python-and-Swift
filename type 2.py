set = {'Sdd', 'ser', 'Qwe', 'Ads'}
new_set = set.pop()
print(f'The random element has selected is {new_set}. ')

set.clear()
print(f'new_set is {set}')

list1 = {1, 2, 3}
list2 = {1, 5, 6}
list3 = list1.difference(list2)
print(f'The difference between list1 and list2 is {list3}')
list4 = list2.difference(list1)
print(list4)

