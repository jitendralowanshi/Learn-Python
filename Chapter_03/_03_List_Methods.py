# list methods 

#FIRST --> append()
list = [2, 1, 3]
list.append(4)
print(list)


# ASCENDING ORDER 
#SECOND -->  sort()  this function sort the list by assending order 
print(list.sort())
list.sort()
print("Assending order list is ",list)

# DISENDING ORDER 
# this method reverse the list by using sort method 
list.sort(reverse=True)
print("dissending order list is ",list)

# THIRD METHOD  reverse() method 
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list1.reverse()
print(list1)


# FOURTH METHOD insert(idx, val)
list.insert(2, 12)
print(list)
print("\n")


# FIFTH METHOD remove(val)  -->remove first occurence of element
val = [2, 1, 3, 1, 1]
val.remove(1)
print(val)

# pop method same as remove method 
# pop(idx)
val.pop(3)
print(val)