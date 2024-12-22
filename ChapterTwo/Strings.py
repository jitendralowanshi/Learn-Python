# new lines use in python
str1 = "this is a string.\nwe are creating it in python."
str2 = "this is a string.\twe are creating it in python."
print(str1)
print(str2)

print("\n")

# concatinating two strings 
s1 = "Hello"
s2 = "World"

final_str = s1 + s2          #concatination two strings 
print("Concatinating strings are : ", final_str)  
length = len(final_str)      #string length store in variable and print length
print("length is : ", length,"\n")


#this len count with spaces 
finalString = s1 + " " + s2
stringlen = len(finalString)
print("Concatinating string with OneSpace : ",finalString)
print("Length is : ", stringlen)

str = "jitendr lowanshi"
ch = str[1]
print(ch)
#