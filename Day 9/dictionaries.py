programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"]="The action of doing something over and over again."
print(programming_dictionary)

# Create empty dictionary
# empty_dictionary = {}

#Wipe an existing dictionary:
# programming_dictionary={}

#Edit an item in a dictionary
# programming_dictionary["Bug"] = "Test assign"
# print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])