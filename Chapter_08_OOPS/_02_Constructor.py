'''
CONSTRUCTOR 
All classes have a function called __init__() , 
which is always execute when the class is being initiated
one constroctor in a one class use 
'''
# student is a class
class Student :  
    # default constructor 
    def __init__(self):
        pass


    # this is a parametrized constructor
    def __init__(self, name, marks):   
        print("\n")
        self.name = name
        self.marks = marks
        print("adding new student is database")   
       


# this is a an onject call to student class 
obj = Student("jitendra", 80)
print(obj.name, obj.marks)

obj1 = Student("Lowanshi", 90)
print(obj1.name, obj1.marks)


# _______________________________________________________________________

class Stundent:

    def __init__(self, name, surname):
        print("my full name is : " )
        self.name = name
        self.surname = surname

s1 = Stundent("jitendra", "Lowanshi")
print(s1.name)
print(s1.surname)