'''
Someone bought a box of eggs. When counted two by two, one egg is left over.
When counted three by three, one egg is left over.
When counted four by four, one egg is left over.
How many eggs are there in the box?
'''
count = 2 #it can be any number
         # but the result should be larger than 2
while True: #death loop(don't know when to end)
    if count % 2 == 1 and count % 3 == 1 and count % 4 == 1:
        print(f'count = {count}')
        break #if encounter a correct answer, will stop
    count +=1 #it can't be included in the command of print and break
    #can't run the command after 'break'
