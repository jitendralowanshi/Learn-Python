# Tupples are immutable in python
tup = "Hello"
print(tup)
print(type(tup))
print("\n")


tup1 = (1, 2, 3, 4, 2, 2, 2)
print(tup1)
print(type(tup1))
# tupple slicing
print(tup1[1:3])
print("\n")


# TWO TUPPLES METHOD 
# index(ele) --> return index of first occurence
ans = tup1.index(4)
print(ans)


# count(ele) --> count total occurences 
count = tup1.count(2)
print(count)
