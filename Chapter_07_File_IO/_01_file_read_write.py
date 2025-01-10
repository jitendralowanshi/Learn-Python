'''
We have to open a file before reading or writing 

f = open("fileName" , "mode")
data = f.read()    --> reading file and fransfer and open data to data file 

Ex-
fileName --> sample.txt,   demo.docx
mode --->  r: read mode,   w: write mode

f.close()    close the file 
'''



fileRead = open("Chapter_07_File_IO/demo.txt", "r")      #r --> read w-->write
data = fileRead.read()
print(data)
print(type(data))
fileRead.close()


# read line by line --read one line at a one time--> redaline() fn
f = open("Chapter_07_File_IO/demo.txt", "r")
line1 = f.readline()
print(line1)



# create a new file thi code create file in write mode 
# this file also create in append mode a
creatFile = open("Chapter_07_File_IO/sample.txt",  "w")
creatFile.close()


# create a file and write something
# FileRD = open("Chapter_07_File_IO/sample.txt", "r+")
# fileRead.write("some thing changes ")
# # file = fileRead.read()
# fileRead.close()


# create a file and write something
with open("Chapter_07_File_IO/sample.txt","w") as f :
    f.write("my name is jitendra 73543")
 