# Assignment
# Create a dictionary called students where:

# The key is the student’s name (string)

# The value is another dictionary with subjects and grades

# Example:

# students = {
#     "Alice": {"Math": 88, "Science": 92, "English": 85},
#     "Bob": {"Math": 75, "Science": 78, "English": 80}
# }


# Add a new student and their subjects/grades using dict.update().

# Update a student’s grade for a particular subject.

# Remove a student from the dictionary using .pop().

# Display all students and their grades in a formatted way.

# Find and display:

# The average grade for each student.

# The student with the highest average grade.

# Allow users to search for a student by name using .get().

# Allow users to add new subjects to existing students.

# Print all subjects offered (no duplicates) using dictionary methods.\

# which method collects all the keys in a dictionary and put them in a list 


# Solution
students = {
    "Alice": {"Math": 88, "Science": 92, "English": 85},
    "Bob": {"Math": 75, "Science": 78, "English": 80}
}
students.update({"Segun" : {"Math":99,"Science":89,"English":93}})
# students["segun"].update()
students["Segun"]["Math"] = 90
students.pop("Alice")
print(students)
print(students["Segun"] )
print(f'The Average score for Bob is {(int(students["Bob"]["Math"])+int(students["Bob"]["Science"])+int(students["Bob"]["Science"]))/3}')
print(f'The Average score for Segun is {(int(students["Segun"]["Math"])+int(students["Segun"]["Science"])+int(students["Segun"]["Science"]))/3}')
student = input("Enter the name to search: ")
name = students.get(student, "Name not found")
print(name)
Stu_name = input("Enter the nsme of the student")
subject = input("Enter the subject : " )
score = input("Enter the student score")
students.update({Stu_name:{subject:score}})
add_sub = students[student][subject] = score
print(students)

samuel = students.keys()
print(samuel)
