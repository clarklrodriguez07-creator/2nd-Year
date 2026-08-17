class Student:

    def __init__(self, student_id, lastname, firstname, mi, course, section):
        self.student_id = student_id
        self.lastname = lastname
        self.firstname = firstname
        self.mi = mi
        self.course = course
        self.section = section

    def display_info(self):
        print("Student ID: " + self.student_id)
        print("Last Name: " + self.lastname)
        print("First Name: " + self.firstname)
        print("Middle Initial: " + self.mi)
        print("Course: " + self.course)
        print("Section: " + self.section)

student_id = input("Enter Student ID: ")
lastname = input("Enter Last Name: ")
firstname = input("Enter First Name: ")
mi = input("Enter Middle Initial: ")
course = input("Enter Course: ")
section = input("Enter Section: ")

student = Student(student_id, lastname, firstname, mi, course, section)
print("\nStudent Information:")
student.display_info()