# set is the collection of unorder items
# Each element in the set must be unique & immutable
# duplicate values are not allowed in set

#  How to create empty set
# empty set  syntex 
collection = set()
print(type(collection))
collection.add(1)
collection.add(2)
collection.add(2) #egnotre this value because its repeat
collection.add("Jitendra")
print(collection)
print("\n")



set = {1, 1, 2, 2, 3, 4, 5, "hello", "world", 5, 4}
print(set)
print(type(set))
print(len(set))  #total number of items 
print("\n")



# Repeated element stored only once , so it resolved to {1, 2}
# set egnored repeated elements in set 
set2 = {1, 2, 2, 2, 1}
print(set2)  



