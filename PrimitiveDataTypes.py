#Data Types

#String

#Subscripting
print("Hello"[0])
#Prints what letter is in position 0 (H)
#Print last letter in hello
print("Hello"[(len("Hello"))-1])

#Use underscores instead of commas for integers
#123_456_789 is 123,456,789

#Ctrl + / makes a line a comment

# type(Variable) checks what type of data type something is

#typecasting
num_char = 6
print(num_char)
new_num_char = str(num_char)
print("Your number is " + new_num_char)

#Practice 1
# Don't change the code below 
two_digit_number = input("Type a two digit number: ")
#  Don't change the code above 

####################################
#Write your code below this line 
#print(type(two_digit_number))
DigitOne = two_digit_number[0]
DigitTwo = two_digit_number[1]
#print(type(DigitTwo))
Sum = (int(DigitOne) + int(DigitTwo))
#print(DigitOne + " + " + DigitTwo + " = " + str(Sum))
print(Sum)

#2 to the power of 2 is 2 ** 2
#PEMDAS

#BMI Calculator
# Don't change the code below 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#  Don't change the code above 

#Write your code below this line 
weight = float(weight)
height = float(height)
BMI = (weight) / (height  ** 2)
print(int(BMI))

#To round to the nearest whole number, use the round() function
#Overloaded method is round(number, digits you want to round it to)
print(round((8/3), 2))
#if you just want an integer, use:
print(8 // 3)
#score = score / 2   or  score /= 2

#f-String allows us to make a string with multiple data types instead of type casting each variable to a string
print(f"your BMI is {BMI}, your height is {height}")
#put the variable you want to typecast into curly braces and put f before the quotes