class Person:
    name = "Bob"
    age = 30
    gender = "Male"

class Student(Person):
    fee = 5000

class Faculty(Person):
    lunch = False
    bonus = True

class TA(Student, Faculty):
    def showTaData(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.fee)
        print(self.lunch)
        print(self.bonus)



