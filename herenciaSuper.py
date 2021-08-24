class Person():

    def __init__ (self, name, age, residence):

        self.name = name
        self.age = age
        self.residence = residence

    def description(self):

        print("Nombre:", self.name, "\nEdad:", str(self.age) + " años", "\nLugar de residencia:", self.residence)

class Employee(Person):

    def __init__ (self, wage, seniority, employee_name, employee_age, employee_residence):

        super().__init__(employee_name, employee_age, employee_residence)

        self.wage = wage 

        self.seniority = seniority

    def description(self):
        super().description()
        print("Salario: ", str(self.wage) + " pesos", "\nAntiguedad: ", str(self.seniority) + " años")
        


Manuel = Employee(1500, 15, "Manuel", 55, "Colombia")

Manuel.description()


