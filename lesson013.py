class Person:
    name = "Bob"
    age = 40
    gender = "Male"

class Student(Person):
    fees = 15000

class TA(Student):
    salary = 5000

    def showTaData(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Fees: ", self.fees)
        print("Salary: ", self.salary)

ta = TA()
ta.showTaData()