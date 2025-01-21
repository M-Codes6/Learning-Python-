
# LOOPS IN PYTHON 

# loops are used to repeate instructions

# WHILE LOOP 

count = 1

while count <= 5 :
    print("Hello")
    count += 1

print(count)


i = 1 

while i <= 5 :
    print("buddy")

    i += 1

# We can also print itterators for example 

i = 1

while i <= 10 :

    print("Heloo World", i)

    i += 1



# Break And Continue 

# Break 

i = 0

while i <= 5 :
    print(i)
    
    if ( i == 3) :
        break
    i += 1

print (" End of Loop")


# Continue


i = 0

while i <= 5 :
    
    if ( i == 3) :
        i += 1
        continue
   
    print(i)
    i += 1



# For Loops 
 
list = [1, 2,  3, 4, 5]

for val in list :
    print(val)
