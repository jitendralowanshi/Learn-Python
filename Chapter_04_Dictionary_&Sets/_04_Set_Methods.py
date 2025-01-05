collect = set()

# FIRST METHOD collect.add(el)
# set stored elements in a ascending orders
collect.add(2)
collect.add("hello")
collect.add(1)
# collect.add([1,2,3])       list cant pass in set 
print(collect,"\n")


# SECOND METHOD collect.remove(el)
collect.remove(2)
print(collect, "\n")


# THIRD METHOD collect.clear()
# this method use clear and empty the set 
collect.clear()
print("this is empty set --> ",collect, "\n")


# FOURTH METHOD IS 
# set automatic arrange string 
collection = {"hello", "jitendra", "world", "coding", "python"}
# collection.pop()
print(collection, "\n")
print(collection.pop())
print(collection.pop())
print(collection.pop())
print("\n")


# TWO IMPORTANT METHODS IN A SET 
# union method combine two sets and return new set 
# FIRTH ONE IS  set.union(set2)
setOne = {1, 3, 5, 7, 9, 6}
setTwo = {1, 2, 4, 7, 8}

combineSet = setOne.union(setTwo)
print("combine set is ")
print(combineSet)


# dono set ki combine value ko print krwata hai, both set ki common value ko print krwata hai 
print(setOne.intersection(setTwo))


