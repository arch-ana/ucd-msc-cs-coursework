# Pseudocode
# define a print_max function that prints the largest of two numbers with no arguments
#     within it, define a max function that takes two arguments a, b and returns the maximum of the two
#         if a>b, return a
#         else return b
    
#     ask user for two float inputs whose max they would like to calculate
#     print the largest of the two by calling the max function inside of the print statement
#     return (returns None when nothing is specified)
# call the print_max() function


def print_max():
    '''
    Function that prints out the largest of two numbers

    Uses the function max to find the largest
    '''
    def max(a,b):
        '''Function that returns the largest of its two arguments'''
        if a>b:
            return a
        else:
            return b

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print('The largest of', number1, "and", number2, "is", max(number1, number2))
    return 

print_max()