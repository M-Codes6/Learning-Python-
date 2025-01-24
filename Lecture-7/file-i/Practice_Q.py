
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


def check_for_word() :
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()

        if(word in data):
            print("Found")
        else:
            print("Not Found")

check_for_word()


    


# Q4: WAF to find in which line of the file does the word "learning" occur  first. Print -1 if word not found

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data :
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(check_for_line())  






# Q5: From a file containing numbers seperated by comma, print the count of even numbers 

count = 0
with open("practice-2.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0) :
            count += 1

print(count)