#Control Flow and Logical Operators


#If else, leap year or not

#  Don't change the code below 
year = int(input("Which year do you want to check? "))
# Don't change the code above 

#Write your code below this line 

if((year % 4) != 0):
    print("Not leap year.")
elif((year % 100) != 0):
    print("Leap year.")
elif((year % 400) != 0):
    print("Not leap year.")
else:
    print("Leap year.")

#Pizza cost calculator

#  Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#  Don't change the code above 

#Write your code below this line 
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

totalCost = 0
#print(type(totalCost))
if(size == "S"):
    totalCost += 15
    if(add_pepperoni == "Y"):
        totalCost += 2
if(size == "M"):
    totalCost += 20
    if(add_pepperoni == "Y"):
        totalCost += 3
if(size == "L"):
    totalCost += 25
    if(add_pepperoni == "Y"):
        totalCost += 3
if(extra_cheese == "Y"):
    totalCost += 1

print(f"Your final bill is: ${totalCost}.")



#Love score calculator

# Don't change the code below 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#  Don't change the code above 

#Write your code below this line 

name1 = name1.casefold()
name2 = name2.casefold()
# print(name1)
# print(name2)
totalTrue = ( (name1.count('t')) + (name1.count('r')) + (name1.count('u')) + (name1.count('e')) )
totalTrue += ( (name2.count('t')) + (name2.count('r')) + (name2.count('u')) + (name2.count('e')) )
#print(type(totalTrue))
totalLove = ( (name1.count('l')) + (name1.count('o')) + (name1.count('v')) + (name1.count('e')) )
totalLove += ( (name2.count('l')) + (name2.count('o')) + (name2.count('v')) + (name2.count('e')) )

loveScore = str(totalTrue) + str(totalLove)
#print(type(loveScore))
#print(loveScore)
loveScore = int(loveScore)
#print(type(loveScore))

if( (loveScore < 10) or (loveScore > 90)):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif( (loveScore >= 40) and (loveScore <= 50) ):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")