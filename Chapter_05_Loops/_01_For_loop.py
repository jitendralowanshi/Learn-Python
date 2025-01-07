# for loops are used for sequential traversal . For traversing list, string, tupples etc 
list = [1, 2, 3, 4, 5]

# for each loop
for val in list :
    print(val)
print("\n")



# print string 
str = "jitendralowanshi"
for ch in str :
    if (ch == 'o'):
        print("found O ")
        break  #else wala kam break bali condition me execute nhi hoga 
    print(ch)
else :
    print("END ")

# QS.
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
x = 49
i = 0; 
for el in nums :
    if(el == x) :
        print("number found at index ",i)

    i += 1

