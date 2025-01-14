# we use property decorator on any method in the class to use the method as a property 

class Student:

    def __init__(self, phy, chem ,maths):
        self.phy = phy
        self.chem = chem 
        self.maths = maths 
        # self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3)+ "%"

 

stud1 = Student(98, 97, 99)
print(stud1.percentage)

stud1.phy = 80
# print(stud1.phy)
# stud1.calcPercentage()
print(stud1.percentage)