# SNHU - CS200
# Elijah Almestica
# Program name: Automobile Service Invoice

# Dictionary of car services and prices 
carServices = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12
}
# Prints  services and prices info
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

# Prompts user to input service type
firstService = input('Select first service: \n')

secondService = input('\nSelect second service: \n')

# Prints invoice 
print("\n\nDavy's auto shop invoice\n")

if firstService == "-":
    AmountfirstService = 0
    print("Service 1: No service")
else:
    AmountfirstService = carServices[firstService]
    print("Service 1: "+str(firstService)+", $"+str(carServices[firstService]))

if secondService == "-":
    AmountsecondService = 0
    print("Service 2: No service")
else:
    AmountsecondService = carServices[secondService]
    print("Service 2: "+str(secondService)+", $"+str(carServices[secondService]))
# Prints total computation 
print("\nTotal: $"+str(AmountfirstService+AmountsecondService))
    
    