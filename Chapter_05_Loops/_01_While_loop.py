
i = 1
while  i <= 5 :
    print("hello World", i)
    i += 1


# PRINT NUM FROM 1 TO 100
num = 1
while num <= 100 :
    print(num)
    num += 1 
print("\n")


# PRINT THE MULTIPLICCATION TABLE OF A NUMBER N 
n = int(input("enter n : "))

mul = 1
while mul <= 10 :
    print(n* mul)
    mul += 1

print("\n")

# Qs. print list with the help of while loop
# list 
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(nums) :
    print(nums[index])
    index += 1
print("\n")

# QS SEARCH FOR A NUMBER X IN THIS TUPPLE USING LOOP 
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
j = 0
while j < len(tup) :
    if (nums[j] == x) :
        print("x is found at index ",j )
    else :
        print("finding x ")

    j += 1
