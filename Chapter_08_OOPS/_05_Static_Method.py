'''
static method 
'''
class Student:

    @staticmethod   #this is decorator
    def staticMethod():
        print("lowansi G")

    def printSt(Student):
        s1 = Student()
        s1.staticMethod()

s1 = Student()
s1.staticMethod()