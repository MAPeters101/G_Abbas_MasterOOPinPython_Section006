class Person:
    def setData(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher(Person):
    def __init__(self, salary):
        self.salary = salary

    def showTeacherData(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Salary: ", self.salary)
