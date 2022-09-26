#Functions

#Write your code below this line 

# def paint_calc(height, width, cover):
#     number_of_cans = round(((height * width) / cover))
#     print(f"You'll need {number_of_cans} cans of paint.")


# #Write your code above this line 
# # Define a function called paint_calc() so that the code below works.   

# #  Don't change the code below 
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
# # ^^ Keyword arguments, add an equal sign and it won't matter what order you put it in
# #positional arguments are where you have to add arguments in order

#Prime Number Checker

#Write your code below this line 

def prime_checker(number, number1):
    number2 = (number1 - 1)
    if(number2 == 1):
        print("It's a prime number.")
    elif( (number % number2) == 0):
        print("It's not a prime number.")
    else:
        prime_checker(number=number, number1=number2)


#Write your code above this line 

#Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n, number1 = n)