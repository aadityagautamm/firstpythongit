operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")
    exit()

print(f"{num1} {operator} {num2} = {result}")



#Inheritance practice

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")

class Programmer1(Programmer):
  def showLanguage1(self):
    print("The default langauge is C++")

e = Employee("Rohan Das", 400)
e.showDetails()
e1 = Employee("Harry", 4100)
e1.showDetails()
e2 = Programmer("Harry", 4200)
e2.showLanguage()
e3 = Programmer1("Harry", 41200)
e3.showLanguage1()