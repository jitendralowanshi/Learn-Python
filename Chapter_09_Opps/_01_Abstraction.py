
# hiding the implimentation details of a clas and only showing the essential features to the user 
# this is a class 
class Car:

    # this is a constructor 
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    # This is a start method to start a car 
    def start(self):
        self.acc = True
        self.brk = True
        self.clutch = True
        print("Car started...")

# this is a Object 
car1 = Car()
car1.start()

