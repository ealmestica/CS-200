# SNHU - CS200
# Elijah Almestica
# Program name: Text Analyzer Modifier

# Counts Characters
def get_num_of_characters(inputStr): 
  characters = 0
  for i in range(0,len(inputStr)):
    characters = characters + 1
  return characters
# Removes whitespace

def output_without_whitespace(no_whitespace):   
    return no_whitespace.replace(" ","")
# Run Script
if __name__ == '__main__':    
    string  = input('Enter a sentence or phrase: ')
    print('\nYou entered:',string)
    print('\nNumber of characters:', get_num_of_characters(string))
    print('String with no whitespace:', output_without_whitespace(string)) 