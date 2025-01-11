'''
A class method is bound to the class & receinves the class as an implicit first arguments
Note-> static method can't access or modify class state & generally for utility

agar hame python me constructor ke trough kisi class attribute ko value assign karani hai to use constractor 
ke under className.classCAttrubute name karenge to value class attribute ko assign ho jayegi 

Three different method is 

# basically jab hame koi kam karana hai jab class ya instance ke kisi mehtod ko touch nhi kar rahe tab 
static method use kar lenge 
1> static method ()

jab hame sirf class attribute ko use kare tab class method ko use karenge 
2> class method (cls)

jab hame sirf instance attribute ko use krna hai tab instance method use karenge 
3> instance method(self)

'''
class Person:
    name = "Anonymous"

    #FIRST TARIKA
    # def changeName(self, name):
    #     # self.name = name this creat a new attribut but we are change the class atrribut so use Person.name = name 
    #     Person.name = name


# using class method cls is a keyword
    @classmethod
    def changeName(cls, name):
        cls.name = name



p1 = Person()
p1.changeName("Jitendra Lowanshi")
print(p1.name) 
print(Person.name)

# METHODS 
# 1> static method ()
# 2> class method (cls)
# 3> instance method(self)