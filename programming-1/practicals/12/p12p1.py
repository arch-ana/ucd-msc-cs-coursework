# (a) Write a non-recursive function that takes as its single argument a non-negative integer
# and returns the factorial of the number.
# (b) Write a program that prompts the user for an integer and checks that the number entered
# is non-negative. If it is, it calls the function defined in part (a) and prints out the result; if not, it prints out an appropriate error message.
# Save this program as p12p1.py.

# Pseudocode

# def factorial(x):
#     initiatlize factorial to 1
#     for num from 2 to x+1:
#         change value of factorial to factorial*num
#     return factorial

# ask user for a non-negative integer input and read it into a variable
# if user_input >= 0:
#     use function to calculate the factorial
#     print Factorial of user_input
# else:
#     print "Error, you entered a negative number"

def factorial(x):
    '''Finds the factorial of a number

    Assumes that x is a non-negative integer and returns the factorial of x'''
    factorial = 1
    for num in range(2, x+1):
        factorial *= num
    return factorial

user_input = int(input("Please enter a non-negative integer: "))
print("You entered", user_input)

if user_input >= 0:
    print("Factorial of", user_input, "is", factorial(user_input))
    print("Program terminates. ")
else:
    print(user_input, "is negative, program terminates.")