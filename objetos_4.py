""" Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para 
inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es 
(equilátero, isósceles o escaleno). """

class Triangle(): #creamos la clase
    def inicializar(self):
        self.side1 = int(input("Ingrese el valor del primer lado: "))
        self.side2 = int(input("Ingrese el valor del primer lado2: "))
        self.side3 = int(input("Ingrese el valor del primer lado3: "))

    def display(self):
        print("Los lados del triangulo tiene los siguientes valores: ")
        print("Lado1: ", self.side1)
        print("Lado2: ", self.side2)
        print("Lado3: ", self.side3)

    def bigger_side(self):
        print("El lado mayor es el: ")

        if self.side1 > self.side2 and self.side1 > self.side3:
            print("lado 1: ", self.side1)
        elif self.side2 > self.side3:
            print("lado 2: " , self.side2)
        else:
            print("lado 3: ", self.side3)

    def kind(self):
        if self.side1 == self.side2 and self.side1 == self.side3:
            print("Es un triángulo equilátero")
        elif self.side1 != self.side2 and self.side1 != self.side2 and self.side1 != self.side3:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


geometric_figure = Triangle()
geometric_figure.inicializar()
geometric_figure.display()
geometric_figure.bigger_side()
geometric_figure.kind()

