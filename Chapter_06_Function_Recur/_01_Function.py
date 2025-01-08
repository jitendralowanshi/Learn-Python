# block of statement that perform a specific task
# EXAMPLE
# def <funName> (arg1 , arg2..) :  <-- function defining 
#     #somework
#     return val


def sumOfTwoNum(a , b) :
    sum = a + b
    print(sum)
    return sum


a = int(input("enter first number : "))
b = int(input("enter your second number : "))
sumOfTwoNum(a,b)


def calc_sum(a, b) :
    return a + b

sum = calc_sum(335, 356)
print(sum)


# koi value return nhi krta hai 
def print_hello() :
    print("huy")

output = print_hello()
print(output)