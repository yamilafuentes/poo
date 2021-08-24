class Vehicle():                         # cuando creemos un objeto de tipo vehiculo u otro que herede de 
    def __init__(self, brand, model):    #vehiculo, ese objeto va a tener una marca y un modelo que le pasaremos al constructor
        self.brand = brand               # por defecto no estara en marcha acelerando o frenando 
        self.model = model
        self.moving_state = False
        self.speed_up_state = False
        self.brake_state = False

    def moving(self):        #comportamiento o metodo
        self.moving_state = True

    def speed_up(self):
        self.speed_up_state = True

    def brake(self):
        self.brake_state = True

    def state(self):
        print("Marca: ", self.brand, " \nModelo: ", self.model, "\nEn Marcha: ", self.moving_state, "\nAcelerando: ", self.speed_up_state, "\nFrenando: ", self.brake_state)


class Van(Vehicle):         #no tengo ningun constructor pero hedera de vehiculo 
    def load_truck(self, load):
        self.loaded_truck = load 

        if (self.loaded_truck):
            return "La furgoneta esta cargada" 
        else:
            return "La furgoneta no esta cargada"


class Motorcycle(Vehicle):        # instancia u objeto de tipo moto, perteneciente a la clase vehiculo 
    speed_up_suddenly_state = False            # esta clase hereda de vehiculo
    
    def speed_up_suddenly(self):
        self.speed_up_suddenly_state = True

    
    def state(self):
        print("Marca: ", self.brand, " \nModelo: ", self.model, "\nEn Marcha: ", self.moving_state, "\nAcelerando: ", self.speed_up_state, "\nFrenando: ", self.brake_state, "\n", "\nAcelero de repente: ", self.speed_up_suddenly_state)


class Electric_vehicle(Vehicle):
    def __init__ (self, brand, model):
        super().__init__(brand, model)
        self.autonomy = 100
    
    def load_energy(self):
        self.loading = True


my_motorcycle = Motorcycle("Honda", "CBR")   

my_motorcycle.speed_up_suddenly() 

my_motorcycle.state()               #utitlizo la instancia para llamar a cualquiera de los metodos que hemos heredado


my_van = Van("Renault", "Kangoo")  

my_van.moving()

my_van.state()

print(my_van.load_truck(True))

class Electric_bicycle(Electric_vehicle,Vehicle):
    pass

my_bicycle = Electric_bicycle("Orbea", "Hjd")

# super() va a llamar al metodo de la clase padre, ejecuta el metodo _init__ de la clase padre

