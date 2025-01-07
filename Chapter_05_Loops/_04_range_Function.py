# range functo=ion return a sequence of numbers, starting from 0 by default , 
# and increments by 1(by default) , and stop before a specified number
# Ex -->  range(start>, stop, step?)

# range return sequence of numbers
for el in range(10) :
    print(el)
print("\n")


 #sequence start from 0 t0 9, ending index not encluded
for el in range(2, 10) :
    print(el)
print("\n")

# even number print -- if print odd num start from 1
for el in range(2, 11, 2) :
    print(el)
print("\n")



# practice using for loops 
# Q1 print number 1 to 100
for val in range(1,51) :
    print(val)
print("\n")


# Q2 print number 100 t0 1 
for val in range(100, 0, -1 ) :
    print(val)
print("\n")


# Q3 print the multiplication of a number n
n = int(input("enter number : "))
for val in range(1, 11) :
    mul = val * n
    print(mul)