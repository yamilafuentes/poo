#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota 
#del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el 
#resultado de la nota y si ha aprobado o no.

#inicializamos al clase
class Student():
    
    #inicializamos los atributos
    def initialize(self, name, test_scores):
        self.name = name
        self.test_scores = test_scores
    
    def display(self):
        print("Nombre: ", self.name)
        print("Nota: ", self.test_scores)

    def result(self):
        if self.test_scores < 5:
            print("El alumno ha desaprobado")
        else:
            print("El alumno ha aprobado")


#creamos los nuevos objeros
student1 = Student()
student2 = Student()

#inicializamos los atributos
student1.initialize("Ivan", 8)
student2.initialize("Juan", 4)

#imprimimos los datos y resultados de cada alumno 
student1.display()
student1.result()

student2.display()
student2.result()

