# class Student :

#     # this is constructor
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     # this is methods 
#     def welcome(self):
#         print("welcome students ,", self.name)

    
#     def get_marks(self):
#         return self.marks

# s1 = Student("jitendra ", 99)   # class object
# s1.welcome()        # method call using class object
# mark = s1.get_marks()
# print(mark)



# PRACTICE Qs 
'''
create a student class that takes name & marks of 3 subjects as arguments in constructor 
then crate a method to print the average 
'''
class Student:
    def __init__(self, name, phy, che, maths):
        self.name = name
        self.phy = phy
        self.che = che
        self.maths = maths

    def average(self):
        avg = (self.phy + self.che + self.maths)/3
        print(avg)
        return avg

s1 = Student("jitendra", 70, 80, 90)
s1.average()


# second 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum/3
        print(avg)

s1 = Student("jitendra", [70, 80, 90])
s1.average()
