# Pseudocode
# prompt user for a string
# if the count of dog and cat in input string is equal:
#     print they are equal
# else:
#     print that they are unequal

user_input = input("Enter a string: ")
if user_input.lower().count("cat") == user_input.lower().count("dog"):
    print("The number of instances of cat and dog in the input string are equal to each other. ")
else:
    print("The number of instances of cat and dog in the input string are not equal to each other. ")
