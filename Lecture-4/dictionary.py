
# DICTIONARY IN PYTHON 

dict = {
    "name": "Muzamil",
    "age": 23,
    "class" : "BSc.CS",
}

print(dict["age"], dict["name"], dict["class"])


info = {
    "key" : " value",
    "name" : "Muzamil",
    "age" : 23,
    "class" : "BSc.CS",
}

print(info)



# NESTED DICTIONARY

student = {
    "name": "Muzamil",
    "score": {
        "math": 73,
        "physics": 80,
        "chemistry": 70
    }
}

print(student)
print(student ["score"]["math"])


# DICTINOARY METHODS

dict = {
    "name": "Muzamil",
    "age": 23,
    "class" : "BSc.CS",
    "state": "Kashmir"
}

print(dict.keys()) # returns the keys of the dictionary
print(dict.values()) # returns the values of the dictionary
print(dict.items()) # returns the key-value pairs of the dictionary
print(dict.get("name")) # returns the value of the key
print(dict.get("state")) # returns the value of the key
dict.update({"city": "Sopore"}) # updates the value of the key
print(dict)
