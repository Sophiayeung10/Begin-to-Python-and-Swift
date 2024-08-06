name = "Sophia company"
stock_price = 19.99
stock_code = '00213'
days = 7
growth = 1.2
price = days * growth * stock_price

print(f'After {days} day(s), your stock code {stock_code} of {name} has grown to be $%.2f' %(price))