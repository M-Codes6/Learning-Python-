
# Q1: Create a new file "practice.txt" using python. Add the following data in it 
# Hi every one ,
# we are learning file i/o,
#  using python , 
# i like learning python.

with open("practice.txt", "w") as f:
    f.write("Hi every one\nwe are learning file i/o\nusing python\nI like learning python.")






# Q2: WAF that replcae all occurences of "Python" with "JavaScript" in above file 

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("python","Javascript")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)




# Q3: Search if the word "learning" exists in the file or not 

word = "learning"

with open("practice.txt","r") as f:
    data = f.read()

    if(data.find(word) != -1):
       print("Found")
    else:
        print("Not Found")