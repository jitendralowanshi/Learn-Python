'''
three types inheritance in python
1>  Single Inheritance
2>  Multi-level Inheritance
3>  multiple Inheritance
'''

# SINGLE INHERITANCE
class Car:

    color = "black"

    @staticmethod
    def start():
        print("car is started ")

    @staticmethod
    def stop():
        print("car is stopped ")


class TataCar(Car):
    # inherit class Car

    def __init__(self, name):
        self.name = name


# tata car class object 
car1 = TataCar("Toyota")
car2 = TataCar("fortuner")

print(car1.start())
print(car1.color)
print(car2.color)
print("\n")



# ====================================================================================================
''' MULTI LEVEL INHERITANCE '''

# class One
class Car:

    color = "black"

    @staticmethod
    def start():
        print("car is started ")

    @staticmethod
    def stop():
        print("car is stopped ")


# class second
class TataCar(Car):
    # inherit class Car

    def __init__(self, name):
        self.name = name


# cclass third 
class MultiLevel(TataCar):

    def __init__(self, type):
        print("this car, is a petrol car ")

   

# object 
obj = MultiLevel("petrol")
obj.start()
obj.stop()
print("\n")


# =============================================================================================
''' MULTIPLE INHERITANCE'''

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"


# Inherit two class in a class 
class C(A, B):
    varC = "welcome to class C"

# Object 
obj = C()

print(obj.varA)
print(obj.varB)
print(obj.varC)