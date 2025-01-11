'''
used to delet object properties or object itself 
del s1.name          #delete attributes 
del s1               #delet comple object
'''
class Student:
    def __init__(self, name):
        self.name = name 

s1 = Student("jitendra")
print(s1)
print(s1.name)

# this is delete the class object 
del s1   #delet object
print(s1.name)


# this is delet the attributes like name 
del s1.name
print(s1.name)