#Randomization and Lists

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
randomName = random.randint(0, (len(names)-1) )
print(f"{names[randomName]} is going to buy the meal today!")



#Nested Lists
fruits = ["Strawberries", "Apples", "Oranges"]
vegetables = ["Carrots", "Asparagus", "Celery"]
healthy_foods = [fruits, vegetables]
print(healthy_foods[1][1]) #will print item at index 1 from vegetables
print(fruits[-1])
#You can have negatives in lists, they just count backwards