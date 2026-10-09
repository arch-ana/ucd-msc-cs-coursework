# Implement the program that uses the print max function from the lectures (Page 9 of the notes on Lecture 15, the section on “Functions 
# within functions”). Ensure that you understand what is going on and how it works.

# Pseudocode
# def max function that takes two arguments (a, b):
#     if a>b:
#         return a
#     else:
#         return b (also handles the case where both are equal)
# request user for two float inputs and store them in variable
# within a print statement, call the max function on the two variables alone with an appropriate print message

def max(a,b):
    '''Function that returns the largest of its two arguments'''
    if a>b:
        return a
    else:
        return b

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("The largest of", number1, "and", number2, "is", max(number1, number2))
print("Finished")