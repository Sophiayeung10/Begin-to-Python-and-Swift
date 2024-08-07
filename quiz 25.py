list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_no = []
index = 0
while index < len(list):
    element = list[index]
    if element % 2 == 0:
        even_no.append(element)
    index += 1
print(even_no)

