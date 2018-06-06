# SNHU - CS200
# Elijah Almestica
# Program name: Half Arrow 

# output arrow_base_height = 5, arrow_base_width = 2, and arrow_head_width = 4:
print ('Enter arrow base height: ')
arrow_base_height = int(input())
   
print ('Enter arrow base width: ')
arrow_base_width = int(input())

arrow_head_width = 0
while arrow_head_width <= arrow_base_width:
    print ('Enter arrow head width: ')
    arrow_head_width = int(input())

# Draw arrow base (height = 3, width = 2)
for arrow_base_height in range(arrow_base_height):
    for arrow_base_width in range(arrow_base_width):
      arrow_base_width = arrow_base_width + 1
      print('*', end=' ')
    print('')

# Draw arrow head (width = 4)
for arrow_head_width in range((arrow_head_width), 0, -1):
  for arrow_head_width in range ((arrow_head_width), 0, -1):
    arrow_head_width = arrow_head_width - 1 
    print('*', end =' ')
  print('')