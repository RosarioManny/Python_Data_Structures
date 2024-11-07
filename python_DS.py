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
print('Exercise 1:', manage_students())
