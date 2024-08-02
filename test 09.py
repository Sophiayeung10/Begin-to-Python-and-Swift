#discount 12% off
t_shirt = float(input('How much was the shirt? '))
pant = float(input('How much was the pant? '))
t_shirt_count = int(input('How many shirt you bought? '))
pant_count = int(input('How many pant you bought? '))
discount = float(input('How much discount you had? '))
sum = (t_shirt * t_shirt_count + pant * pant_count) * discount
print(f'Total price that you paid = $%.2f' %(sum))