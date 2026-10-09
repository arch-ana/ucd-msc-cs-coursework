# Pseudocode
# def function fibonacci_term taking one argument x
#     if x is one
#         return 0
#     elif x is two
#         return 1
#     else:
#         return fibonacci_term(x-1)+fibonacci_term(x-2)
# request user for a non-negative integer input
# while this input is non-negative:
#     print appropriate error message for 0 as there is no 0th term
#     else call and print the fibonacci term 
#     ask the user again for an input (until they enter a negative integer)
# else:
#     print that negative inputs terminate the program



def fibonacci_term(x):
    '''
    Calculates the xth term in the Fibonacci sequence

    Function assumes that the argument is a non-negative integer and returns the xth term in the series    
    '''
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci_term(x-1)+fibonacci_term(x-2)

user_input = int(input("Enter a non-negative integer: "))


while user_input>=0:
    print("You entered:", user_input)
    if user_input == 0:
        print("There is no 0th term, try a different number")
    else:
        print("Fibonacci term ", user_input, " is: ", fibonacci_term(user_input), sep="")
    user_input = int(input("Enter a number: "))
else:
    print("You entered a negative number, program terminates. ")
    