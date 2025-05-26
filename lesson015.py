class Person:
    name = "Bob"
    gender = "Male"

class Student(Person):
    fee = 5000
    age = 30

class Faculty(Person):
    lunch = False
    bonus = True
    age = 40

class TA(Faculty, Student):
    def showTaData(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.fee)
        print(self.lunch)
        print(self.bonus)

ta = TA()
ta.showTaData()


