class Car():

    def displacement(self):
        print("Me desplazo utlilizando 4 ruedas")
    
class Motorcycle():

    def displacement(self):
        print("Me desplazo utilizando 2 ruedas")

class Truck():

    def displacement(self):
        print("Me desplazo utilizando 6 ruedas")

"""
myVehicle = Motorcycle()

myVehicle.displacement() 

myVehicle2 = Car()

myVehicle2.displacement()

myVehicle3 = Truck()

myVehicle3.displacement()  #llamo al metodo desplazamiento de la clase camion 
"""


def vehicularDisplacement(vehicle):
    vehicle.displacement()

myVehicle = Truck() #creo un objeto de tipo camion 

vehicularDisplacement(myVehicle)     #utilizo el metodo desplazamientoVehicular y le paso por parametro el objeto de tipo camion 


