

# File i/o in python ...... i/o ( input / output)


# Existing building functions to open, read and write a file 


# OPen, Read and Close file

'''f = open("file_name", "mode")   # file_name = sample.txt, demo.docx ... mode = r : read mode , w : write mode
data = f.read()
f.close() '''

f = open("Lecture-7/file-i/demo.txt","r")

data = f.read()
print(data)



# Reading a File 
'''
data = f.read()      # reads entire file
data = f.readline()   # reads onne line at a time '''

data = f.read()
print(data)

data = f.readline()
print(data)

data = f.readlines()
print(data)




# Writing to a file 

'''
f = open("demo.txt","w")
f.write("this is a new line)  #overwrites the entiree file 

f = open("demo.txt","a")
f.write("the this is next line) #adds to the file
'''

f = open("Lecture-7/file-i/demo.txt", "w")
f.write("I am from kashmir :")
f.close()


f = open("Lecture-7/file-i/demo.txt", "a")
f.write(" Sopore, Baramulla")
f.close()



# With Syntax

'''
with open("demo.txt", "mode") as f:
        data = f.read()
'''

with open("Lecture-7/file-i/demo.txt","r") as f:
    data = f.read()

    print(data)


# Deleting A File 

'''
using the os module
# os module is a code library
import os   
os.remove(file name)
'''

import os 
os.remove("Lecture-7/file-i/demo.txt")