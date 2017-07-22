""" Mang Toto's ForEx Challenge
Author:
Description: Aling Nena's Sari-sari store just had a new neighbor! It's Mang Toto's ForEx!
Help Mang Toto to convert `USD, JPY, SGD` to `PHP` by:
* Asking the customer for their currency.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
* If they are not exchanging the currrency, notify the customer.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
>> aud
>> Sorry! We do not exchange aud!
* If they are in their currency list, ask for the amount and inform the original and equivalent PHP amount.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
>> usd
>> Your 100.50 usd is equivalent to 5069.22 PHP
"""

PHP_EXCHANGE_RATE = {
  'usd': 50.44,
  'jpy': 0.45,
  'sgd': 36.25
}

def converter(currency, amount):
    return amount * PHP_EXCHANGE_RATE[currency]

customer_currency = input("Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd): ").lower()
if not (customer_currency in PHP_EXCHANGE_RATE):
    print("Sorry! We do not exchange {}!".format(customer_currency.upper()))
else:
    customer_amt = float(input("How much {}?".format(customer_currency.upper())))
    print("Your {:.02f} {} is equivalent to {:.02f} PHP".format(customer_amt, 
        customer_currency.upper(), 
        float(converter(customer_currency, customer_amt))))

