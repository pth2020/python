#A python program that calculates the total stock value in a cafe.

#List - available stock items
menu = ['tuna sandwich','carrot cake','soft drink can','water bottle 1.5L','J2O']

#Dictionary - key(item in list):value(quantity of item in stock)
stock = {menu[0]:50,menu[1]:15,menu[2]:150,menu[3]:200,menu[4]:30}

#Dictionary - key(item in list):value(price of item)
price = {menu[0]:5.95,menu[1]:3.80,menu[2]:1.50,menu[3]:1.20,menu[4]:1.60}

#total stock value initialised to zero
total_stock_value = 0.0

#loop through stock dict and price dict
for item in menu:
    total_stock_value += stock[item] * price[item] #add on (quantity of item * item price) for each item
    
print("\nTotal stock value: £{:.2f}\n".format(total_stock_value)) #write total value (money) to 2 decimal places
