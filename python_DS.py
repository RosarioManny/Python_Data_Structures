# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
   students = ["Rose", "Chris", "Alice", "Megan", "Bruce"]
   first_student = students[1]
   last_student = students.pop() 
   print(f"The first student is {first_student} and {last_student} is the last")
# print('Exercise 1:', manage_students())

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.
foods = ("Peach", "Spaghetti", "Cookies", "Sandwiches", "Salmon")
meal = ""

def combine_foods():
   for food in foods:
    meal = food

    print("1", meal)

# print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings 
# in the foods to a variable named last_two_foods.

def slice_foods():
   last_two_foods = foods[-2:]
   print(last_two_foods)

# Call the function and print the result
print('Exercise 3:', slice_foods())

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a 
# string with this format: “I was born in <city>, <state> - population of <population>”
home_town = {
    "city": "NYC",
    "state": "NY",
    "population": 8000000,
}
city, state, population = home_town
def hometown_info():
    
    home_town_message = f"I was born in {home_town[city]}, {home_town[state]} - population of {home_town[population]}"
    print(home_town_message)

print('Exercise 4:', hometown_info())

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary 
# and append a string with the following format to home_town_items: "<key> = <value>"
home_town_items = []
def list_home_town_items():
    for key, val in home_town.items() :
        home_town_items.append(f"{key} = {val}")
    print(home_town_items)
    
print('Exercise 5:', list_home_town_items())
