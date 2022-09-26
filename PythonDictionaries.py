#Python Dictionaries

#Dictionaries are like a list
programming_dictionary = {
    "Bug": "Something wrong with your code preventing it from running"
}
#add an item to the dictionary
programming_dictionary["Loop"] = "Something done over and over again"
print(programming_dictionary)
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Student grades calculator using dictionaries
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades= {}

for student in student_scores:
    score = student_scores[student]
    if(score <= 70):
        student_grades[student] = "Fail"
    elif(score <= 80):
        student_grades[student] = "Acceptable"
    elif(score <= 90):
        student_grades[student] = "Exceeds Expectations"
    elif(score > 90):
        student_grades[student] = "Outstanding"    

# 🚨 Don't change the code below 👇
print(student_grades)

#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
    }

#Nesting list in dictionary

travel_log = {
    "France": ["Paris", "Dijon", "Lille"]
}

#It is possible to nest a list in a list
# [A, B, [C, D]]

#Nesting dictionary in dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Dijon", "Lille"], "total_visits": 13},
    "Germany": ["Berlin", "Hamburg"]
}

#Nesting dictionary in list

travel_log = [
    {
    "country" : "France",
    "cities_visited": ["Paris", "Dijon", "Lille"],
    "total_visits": 13
    },
    {
    "country" : "Germany",
    "cities_visited": ["Berlin", "Hamburg"],
    "total_visits": 12
    }
]


#Second exercise
#Create function to add travel stuff to the existing list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_dictionary = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_dictionary)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)