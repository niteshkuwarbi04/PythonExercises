'''
10. Write a Python class named Student with two attributes student_id, student_name. 
    Add a new attribute student_class and
    display the entire attribute and the values of the class. 
    Now remove the student_name attribute and display the entire attribute with values.'''

class Student:
    def __init__(self, std_id, std_name):
        self.student_id = std_id
        self.student_name = std_name

# Creating an instance of the Student class
student_instance = Student(1001, "Vivek Singh")

# Displaying entire attributes and values
print("Original attributes and values:")
print("Student ID:", student_instance.student_id)
print("Student Name:", student_instance.student_name)

# Adding a new attribute student_class
student_instance.std_class = "BCA"

# Display entire attributes and values after adding student_class
print("\nAttributes and values after adding student_class:")
print("Student ID:", student_instance.student_id)
print("Student Name:", student_instance.student_name)
print("Student Class:", student_instance.std_class)

# Remove the student_name attribute
del student_instance.student_name

# Display entire attributes and values after removing student_name
print("\nAttributes and values after removing student_name:")
print("Student ID:", student_instance.student_id)
# The next line will result in an AttributeError since student_name is removed
# print("Student Name:", student_instance.student_name)
print("Student Class:", student_instance.std_class)

