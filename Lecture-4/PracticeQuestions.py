

# Q1: Store following word meanings in a dictionary?
# table: "a piece of furniture","list of facts and figures"
# cat : "a cmall animal"

word_meanings = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}

print(word_meanings)
print(word_meanings["table"])

# Q2: You are given a list of subjects for students. Assume 1 class room is required for 1 sbuject.How many class rrooms are needed by all the students?
# "python", "java", "c++", "c", "python", "javascript", "java", "c++"

subjects = ["python", "java", "c++", "c", "python", "javascript", "java", "c++"]
class_rooms = set(subjects)
print(class_rooms)
print(len(class_rooms))