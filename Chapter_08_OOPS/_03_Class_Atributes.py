'''
two types of atrributes 
Class Attributes 
object Attributes

'''
# class attribute class ke under likhe jate hai or unhe class ke name se acces kiya jata hai 
# print(Student.name)-->  className.AttributeName

# CLASS ATTRIBUTES 
# jo chije common hoti hai har object ke liye unhe ham class attribute bna dete hai 

class Student:

    collegeName = "Iet davv indore "    # class atributes har object ke liye sama rahenge 
    name = "jitendra Lowanshi"        #this is class attributes 

    def __init__(self, name):
        self.name = name     

s1 = Student("mahendra ")
print(Student.name)




# Object attribute ko class ke object ke through acces kiya jata hai jo constructor ke under likhe jate hai
# Object Attribute
class Student:

    def __init__(self, name):
        self.name = name     #this is a object attribute

s1 = Student("mahendra ")
print(s1.name)


# ========================================================================

class Student:
    collegeName = "IET Davv"    # class Attribute

    def __init__(self, name):
        self.name = name        # obj attribute


s1 = Student("mahendra ") 
print(s1.name)      #print obj attr

print(Student.collegeName) #print class attr





    