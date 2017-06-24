""" The Challenge
Author: Olyn Valencia
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""


bill = input('How much is your total bill?')
payment = input('How much is your payment?')
change = float(payment) - float(bill)
print ('Hi! Your change is {}'. format(change))