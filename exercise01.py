bill = input('How much is your total bill?')
payment = input('How much is your payment?')
change = float(payment) - float(bill)
print ('Hi! Your change is {}'. format(change))