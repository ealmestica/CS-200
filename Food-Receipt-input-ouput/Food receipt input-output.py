# SNHU - CS200
# Elijah Almestica
# Program name: Food receipt input/output

# Finish reading item price and quantity, then output a receipt
itemName = input('Enter food item name: \n')
itemPrice = float(input('Enter item price: \n'))
itemQuantity = int(input('Enter item quantity: \n'))


totalCost = itemPrice * itemQuantity

print('\nRECEIPT\n',itemQuantity, itemName, '@ $', itemPrice, '= $', totalCost)

print(' Total Cost:','$', totalCost)


# Read in a second food item name, price, and quantity, then output a second receipt
itemName2 = input('\nEnter food item name: \n')
itemPrice2 = float(input('Enter item price: \n'))
itemQuantity2 = int(input('Enter item quantity: \n'))

totalCost2 = itemPrice2 * itemQuantity2
subTotal = totalCost + totalCost2

print('\nRECEIPT\n',itemQuantity, itemName, '@ $', itemPrice, '= $', totalCost)
print('',itemQuantity2, itemName2, '@ $', itemPrice2, '= $', totalCost2)

print(' Total cost: $',subTotal)


   
# Add a gratuity and total with tip to the second receipt
tip = subTotal * .15
totalBill = subTotal + tip

print('15% gratuity: $',tip)
print('Total with tip: $',totalBill)
