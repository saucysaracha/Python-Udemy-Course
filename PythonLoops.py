#Python Loops

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


#Highest Score Calculator
#  Don't change the code below 
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
#  Don't change the code above 

#Write your code below this row 

highestScore = student_scores[0]
for n in range(0, len(student_scores)):
  if(student_scores[n] > highestScore):
    highestScore = student_scores[n]

print(f"The highest score in the class is: {highestScore}")


#Average Height Calculator
#  Don't change the code below 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above 


#Write your code below this row 
totalHeights = 0
for heights in student_heights:
    totalHeights += heights

#print(totalHeights)
averageOfHeights = round((totalHeights / len(student_heights)))
print(averageOfHeights)