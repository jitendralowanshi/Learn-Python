# Recursion 
# when a function calls  itself repeatedly


def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

# call show method
show(10)


# factorial 
def fact(n):
    # base case 
    if(n == 0 or n == 1):
        return 1
    return n * fact(n-1)
print(fact(10))

# recursive fn to calculate the sum of first n natural numbers 
def sumOfN(n):
    if(n == 0):
        return 0
    return sumOfN(n-1) + n
    
# call sumOfN Numver

print(sumOfN(9))