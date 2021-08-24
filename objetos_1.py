class Car():

    def __init__ (self):    #constructor de mi clase, le da estado inicial a los objetos que pertenezcan a esta clase

        self.__chassis_length = 250           #estado inicial o punto de partida 
        self.__chassis_width = 120
        self.__wheels = 4
        self.__moving = False

    def start(self, stared):

        self.__moving = stared            #le asigna a la variable __moving, arrancamos

        if (self. __moving):                  #si la funcion __chequeo_interno da True es xq esta todo Ok y el auto puede 
            check = self.__internal_check()         

        if (self.__moving):
            return "El choche esta en marcha"

        elif (self.__moving and check == False):
            print("Algo ha ido mal en el chequeo, no podemos arrancar")

        else:
            return "El coche esta parado" 

    def state(self):
        print("El coche tiene: ", self.__wheels, "ruedas, un ancho de: ", str(self.__chassis_width) + " cm", "y un largo de: ", str(self.__chassis_length) + " cm")

    def __internal_check(self):
        print("Realizando chequeo interno")

        self.gasoline = "Ok"
        self.oil = "Ok"
        self.doors = "Cerradas"

        if (self.gasoline == "Ok" and self.oil == "Ok" and self.doors == "Cerradas"):
            return True
        else:
            return False



my_car = Car()         #creo la instancia


print(my_car.start(True))     #para que el coche arranque

my_car.state()    #aca le pregunto el estado 


print("------------ A continuacion creamos el segundo objeto -------------")


my_car2 = Car()         #creo una segunda instancia

print(my_car2.start(False))     #para que no arranque el coche

my_car2.state()       #aca le pregunto el estado 



