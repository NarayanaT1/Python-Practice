# Example 1: Creating a simple class

class Student:
    pass


student1 = Student()
student2 = Student()

print("Student1 is Student2:", student1 is student2)

student3 = student1

print("Student1 is Student3:", student1 is student3)
print("Student1 == Student2:", student1 == student2)
print("Student1 == Student3:", student1 == student3)


# Example 2: Class with constructor

class Student:
    def __init__(self, id):
        self.id = id


student1 = Student(1)
student2 = Student(2)
student3 = Student(1)
student4 = student1

print("Student1 is Student4:", student1 is student4)
print("Student1 is Student2:", student1 is student2)
print("Student1 is Student3:", student1 is student3)
print("Student1 == Student3:", student1 == student3)


# Example 3: Override equality using __eq__()

class Student:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


student1 = Student(1)
student2 = Student(2)
student3 = Student(1)
student4 = student1

print("Student4 == Student1:", student4 == student1)
print("Student2 == Student1:", student2 == student1)
print("Student3 == Student1:", student3 == student1)