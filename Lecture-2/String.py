
# STRING

str1 = 'Hello World'   #single quote
str2 = "Hello World"    #double quote
str3 = """Hello World"""    #triple quote


# ESCAPE SEQUENCE CHARACTER 

str1 = "This is a first line . \n This is a second line ."   # \n is used for new line
print(str1)

str1 = "This is a first line . \t This is a second line ."   # \t is used for tab space 
print(str1)


# BASIC STRING OPERATION

   # 1. Cocatenation

str1 = "Hello" + "World"
print(str1)    #HelloWorld

    # 2. Length of string

str1 = "Hello World"
print(len(str1))   #11


# SLICING

str = "Hello World"

print(str[0])   #H
print(str[1:5])   #ello



# STRING FUNCTIONS

str = " i am a coder"

print(str.endswith("r"))  #True
print(str.startswith("i"))  #True
print(str.capitalize())   #I am a coder  (first letter of string is capital)
print(str.replace("coder","developer"))   #i am a developer (replace coder with developer)
print(str.upper())   #I AM A CODER
print(str.lower())   #i am a coder
print(str.find("a"))   #3 (index of first occurence of a)
print(str.count("a"))   #2 (count of a in string)

