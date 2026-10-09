# (a) Write a recursive function that takes as its single argument a non-negative integer and returns the factorial
# of the number.
# (b) Write a program that prompts the user for an integer and checks that the number entered is non-negative. If it is, it 
# calls the function defined in part (a) and prints out the result; if not, it prints out an appropriate error message.
# (c) In your function, include some print statements that allow you to see the operation of the recursion and
# its progress towards the base case.

# Pseudocode
# define factorial function taking one argument x
#     if x == 0 (base case)
#         return 1 (factorial of 0 is 1)
#     else:
#         recursively call the function for x - 1
#         return x * factorial(x-1)

# request user for a  non-negative integer input and read it into a variable
# if it is non-negative, call the factorial function and print the factorial
# else program terminates

def factorial(x):
    '''
    Finds the factorial of a given number
    
    Function assumes that the number is a non-negative integer
    '''
    print("Factorial (", x, ") called ", sep="")
    if x == 0:
        print("Base case reached, returning 1")
        return 1
    result = x*factorial(x-1)
    print("factorial(", x, ") returns ", x, " * factorial(", x - 1, ") = ", result, sep="") 
    return result

user_input = int(input("Enter an integer: "))
print("You entered: ", user_input)

if user_input<0:
    print(user_input, "is negative. Program terminates.")
else:
    print("Factorial of", user_input, "is", factorial(user_input))
    print("Program terminates")