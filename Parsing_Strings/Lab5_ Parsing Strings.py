# SNHU - CS200
# Elijah Almestica
# Program name: Parsing Strings 
# 6.6.1: Parsing strings (Python 3)

# Prompts to input a string
string = input('Enter input string: ')
# Breaks loop if input is q
while string != 'q':  
  while "," not in string: # Prints error if comma is missing and re-prompts for string
    print("\nError: No comma in string.")
    string = input("Enter input string: ")
      
  string = string.replace(' ','')
  string = string.split(',')
  print("\nFirst word: " + string[0])
  print("Second word: " + string[1])
  string = input("\n\nEnter input string: ")
print()