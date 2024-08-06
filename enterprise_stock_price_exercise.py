name = "Sophia's company"
stock_price = float(input('Enter the stock price: '))
stock_code = int(input('Your stock code: '))
days = int(input('Enter the days to grow: '))
growth = stock_price * 2 * days

print(f'After {days} day(s), your stock code {stock_code} has grown to be $%.2f' %(growth))