# dictionary are unordered ,
# dict are mutable

info = {
    # "key" : "value",
    "name" : "jitendra",
    "Learning" : "college",
    "subject" : ["java", "Python", "C", "C++"],  #list
    "topics" : ("disctionary", "set"),
    "age" : 24,
    "is_adult" : True,
    "marks" : 96
}


print(info)
print("\n")

print(info["name"])
print(info["subject"])
print(info["topics"])
print("\n")

info["name"] = "Mahendra " #change values 
info["surname"] = "Lowanshi"   #add new values in dict
print(info["name"])
print(info)
print("\n")


# NESTED DICTIONARY 
student = {
    "name" : "sidharth goutam",
    "subjects" : {
        "phy" : 97,
        "chem" : 95,
        "maths" : 98
    }
}
print(student)
print(student["subjects"])
print(student["subjects"] ["maths"])   # print dictionary ke under dictionary ki value print nested dict
