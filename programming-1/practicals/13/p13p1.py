# Implement the programs that illustrate the definition and use of functions in Python from the lectures (Pages 4 and 5 
# of the notes on Lecture 15, the section on “Function Definition and Function Use”).
# Save these programs as p13p1.py and p13p2.py, respectively.

# Pseudocode
# def max function with two arguments (a,b):
#     if a > b:
#         return a
#     else:
#         return b (also handles the case where both are equal)
# ask user for two float inputs and store it in two variables
# run the max function to and store the returned value in a variable
# print the contents of this variable with appropriate message

def max(a, b):
    '''Function that returns the largest of its two arguments'''
    if a>b:
        return a
    else:
        return b

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

biggest = max(number1, number2)

print("The largest of", number1, "and", number2, "is", biggest)
print("Finished")