# super() method is used to access methods of the parent class 
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car stopped. ")

    @staticmethod
    def stop():
        print("car stopped.. ")

class ToyotaCar(Car):
    '''agar kabhi hame apne parent class ke method ko acees krna ho to super() method ke trough acces kar sakte hai
    '''

    def __init__(self, name, type):
        self.name = name 
        # self.type = type
        super().__init__(type)   #super constructor acces the parent class typpe
        super().start()
        

car1 = ToyotaCar("Tata", "electric")
print(car1.type)

