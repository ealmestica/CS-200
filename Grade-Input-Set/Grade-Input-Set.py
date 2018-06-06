import math

# SNHU - CS200
# Elijah Almestica
# Program name: Grade Input Set

#variable intializations  
gradeList = []
total = 0
grade = 0
min = 0
max = 0
answer ='-'

#Get a grade from a user
grade = int(input('Enter a grade: '))

#Add the grade to the total
total = grade + total
#Add the grade to the list
gradeList.append(grade)
#Set grade to max and min
max = grade
min = grade

#Get another grade from a user or quits program by pressing q
answer = input('Press the enter key to enter another grade or q to quit:')
#Continue to get grades until the user quits
while(answer != 'q'):
  #Gets another grade from the user
  grade = int(input('Enter a grade: '))
  #Adds the current grade to the total
  total = grade + total
  #Adds new grade to the list
  gradeList.append(grade)
  #Checks if new grade is greater than max
  if(grade > max):
    max = grade
  #Checks if new grade is lesser than min
  if(grade < min):
    min = grade
  #Get another grade from a user or quits program by pressing q
  answer = input('Press the enter key to enter another grade or q to quit:')


#Prints lowest, highest, and average grade.
print('Your average grade is -->', math.floor(total / len(gradeList)))
print('Your highest grade is -->',  max)
print('Your lowest grade is -->',  min)
    


