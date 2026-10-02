# Question:
# Write a program that prompts the user for two numbers. If the sum of the 
# numbers is greater than 100, print “That is a big total!” and terminate 
# the program.
# Save this program as p6p1.py.

# Pseudocode
# Ask the user to input the first number
# Read the input into a variable (num1)
# Ask the user to input a second number
# Read the input into a variable (num2)
# if num1+num2>100:
#     print "That is a big total"
# Program completes


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1+num2>100:
    print("That is a big total!")

print("Program completed")