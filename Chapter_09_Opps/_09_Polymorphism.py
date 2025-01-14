'''
Polymorphism : Operator Overloading
when the same operator is allowed to have different according to the context.

operators & Dunder functions

a + b    #addition               a.__add__(b)
a - b    #substraction           a.__sub__(b)
a * b    #multiplication         a.__mul__(b)
a / b    #divition               a.__truediv____(b)
a % b    #modulo                 a.__mod____(b)


print([1, 2, 3] + [4, 5, 6])


# types
print(type([2, 3]))    #list
print(type( (1, 2) ))  #tupple
print(type( {1, 2, 3})) #set 

'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, )
    
com = Complex(4, 6)
com.showNumber()


