

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