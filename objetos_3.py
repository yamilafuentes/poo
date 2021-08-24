"""
Realizar un programa que tenga una clase Persona con las siguientes características.
La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios 
para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
"""

#Creamos nuestra clase persona
class Person():

    #inicializamos nuestros atributos
    def initialize(self, name, age):
        self.name = name
        self.age = age

    #imprimir los datos 
    def display(self):
        print("Nombre: ", self.name)
        print("Edad: ", self.age)

    #comprobamos si es mayor o no 
    def higher_age(self):
        if self.age >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

person1 = Person()
person1.initialize("Ivan", 23)

person2 = Person()
person2.initialize("Carlos", 17)

#imprimimos datos y comprobamos si es mayor de edad 
person1.display()
person1.higher_age()
person2.display()
person2.higher_age()
