# Built-in function this fn is python fn not user difine fn
# print()
# len()
# type()
# range()

# User define functions 

def calc_prod(a, b):
    print(a * b)
    return a * b
calc_prod(5, 4)



# DEFAULT PARAMETERS
# assigning a default value to parameter ,which is used when no arguments is passed 
def calc_prod(a=1, b=1):  #<----- defaulr parameters 
    print(a * b)
    return a * b
calc_prod()     #not give any arguments 


# LET'S PRACTICE
# PRINT THE LEGTH OF A LIST (LIST IS THE PARAMETER)
num = [1, 2, 3, 4, 5, 6, 7, 8]

def print_len(list):
    print(len(list))

print_len(num)

# find the factorial of n (n is the parameter )

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)


# homework problem
def rr(n):
    if(n%2 ==0):
        print("Even")
    else:
        print("Odd")

rr(10)