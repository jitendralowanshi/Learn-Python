''''
conceptual Implimentation in python
Private attributes & methods are meant to be used only within the class and not 
accessile from outside the class 

Private 
kisi bhi attribute or  method  ko private banana ho to uske aage two underscore laga do __
like -->     self.password
privet-->    self.__password
__resetPass()


'''

class Account:

    def __init__(self, acc, password):
        self.accountNo = acc
        self.__password = password   #private attributee __


    def resetPass(self):
        print(self.__password)


acc1 = Account(12345, "abcde")
print(acc1.accountNo)


# print(acc1.__password)  # print prive attribute __ not accesable private attribute 

# private atrribute ko class ke under acces kr sakte hai lekin class ke bahar nhi
# method ke trougth private attribute ko acces kr sakte hai
print(acc1.resetPass())
print("\n")



# ===========================================
# private methods 

class Person:

    # this is private attribute 
    __name = "jitendra Lowanshi"


    # private method 
    def __hello(self):
        print("Hello Perosn")
    

    def welcome(self):
        self.__hello()
        

# class object
p1 = Person()
p1.welcome()



    