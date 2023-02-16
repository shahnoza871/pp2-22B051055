#ex1
"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price)) #The price is 49 dollars
"""


#ex2

"""price = 49.12
txt = "The price is {:.1f} dollars"
print(txt.format(price)) #The price is 49.1 dollars"""

#ex3

"""price = 49
quantity = 5
thing = "kiwi"
txt = "The price is {} dollars for {} kg of {}"
print(txt.format(price, quantity, thing))#The price is 49 dollars for 5 kg of kiwi
"""

#ex4

"""price = 49
quantity = 5
thing = "kiwi"
txt = "The price is {0} dollars for {1:.2f} kg of {2}"
print(txt.format(price, quantity, thing)) #The price is 49 dollars for 5.00 kg of kiwi
"""

#ex5
txt = 'Can I buy {quantity} kg of {thing} for {price} dollars?'
print(txt.format(quantity = 12, thing = 'kiwi', price = 49)) #Can I buy 12 kg of kiwi for 49 dollars?