# dictionary ke under duplicate keys are not allowed 
student = {
    "name" : "sidharth goutam",
    "subjects" : {
        "phy" : 97,
        "chem" : 95,
        "maths" : 98
    }
}

#1 FIRST METHOD  -->  dictName.keys()
# this method print key values like name , subjects are keys val
print(student.keys())
print(list(student.keys()))
# use typcasting
print(len(list(student.keys())),"\n")      # student key ko list me store karaya or uski length find ki



#2 SECOND FUNCTION --> dictName.value(key, val)
# this function print keys values , key ki values ko print krwayega 
print(student.values())
print(list(student.values()))
print("\n")


#3 THIRD METHOD -->  dictName.items()
# thi function print dictionary items only not keys 
print(student.items())
print("list is ",list(student.items())) #convert into list
print("tupple is ",tuple(student.items()))
print("\n")


#4 FOURTH METHOD  dictName.get("key")
# this get fun get key values and not give any error if any case keys are wrong
print(student.get("name"))
print(list(student.get("subjects")))

# print(student["name2"])       # if key id wrong , this fn give erro
print(student.get("name2"))     # this fn not gives any error and return none
print("\n")


# FIFTH METHOD --> dictName.update(newDict)
# this method update and add any keys in dictionary
student.update({"city" : "Indore"}) 
print(student)

new_dict = {"name" : "jitendra lowanshi", "age": 24 }
student.update(new_dict)
print(student)
print("\n")