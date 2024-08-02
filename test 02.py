#define student number
#number can't start from 0
#Error: leading zeros in decimal integer

student_number = 1
print(f'student_number = {student_number}')

#occupy %d' %  d=06= 6 digital numbers
print(f'My student number is %06d' %student_number)
print(f'My student number is %05d' %student_number)

# test 1: price, weight, money
price = 9.00
weight = 5.00
money = price * weight
print('the price of apple is %.4f, and I buy %.4f. So I have to pay %.4f' %(price, weight, money) )
#f = float
print('the price of apple is %04d, and I buy %04d. So I have to pay %04d' %(price, weight, money) )
# d = digital