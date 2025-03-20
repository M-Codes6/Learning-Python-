# message = "Hello World"
# print(message[3::10])

# Break , Continue and Pass

for x in range(8):
    if x == 4:
        print("Breaking at", x)
        break
    print(x)



# Continue
for x in range(8):
    if x == 4:
        print("Skipping", x)
        continue
    print(x)

# Pass

age = int(input("Enter your age: "))
if age> 18 and age < 28:
    print("You are welcome")
else:
    pass
