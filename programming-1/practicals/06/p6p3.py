# Write a program that asks the user their name. If they enter your name, 
# print “That is a cool name!” If they enter “Mickey Mouse” or “Spongebob 
# Squarepants”, tell them that you are not sure that that is their name. 
# Otherwise, tell them “You have a nice name.”. The program should then 
# terminate.

# Pseudocode
# Ask the user to input a name
# Read the name into a variable (name)
# if name == Archana:
#     print That is a cool name
# elif name == Mickey Mouse or name == Spongebob Squarepants:
#     print I am not sure if that is your name
# else:
#     print You have a nice name
# Program completes

name = input("Enter your name: ")
if name == "Archana":
    print("That is a cool name")
elif name == "Mickey Mouse" or name == "Spongebob Squarepants":
    print("I am not sure if that is your actual name")
else:
    print("You have a nice name.")

print("Program completed")