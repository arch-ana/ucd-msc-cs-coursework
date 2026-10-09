# (a) Write a non-recursive function that takes as its argument a non-negative integer and
# prints out that number of terms of the Fibonacci Series. This function should not return an explicit value.
# (b) Write a program that prompts the user for an integer and checks that the number entered
# is non-negative. If it is, it calls the function defined in part (a); if not, it prints out an appropriate error message.

# Pseudocode

# function fibonacci terms(x):
#     current term, next term = 0, 1   
#     for numbers in range(x):
#         print current term
#         current term, next term = next term, current term + next term
#     print empty line

# request and read user input to a variable
# if input < 0:
#     print error message
# else:
#     call fibonacci function for user input
# program terminates 


def fibonacci_terms(x):
    '''
    Finds the first x Fibonacci terms

    Assumes that x is a non-negative integer and prints the first x numbers in the Fibonacci series 
    '''
    f_1, f_2 = 0, 1
    print("The first", x,"terms of the Fibonacci sequence are: ", end=" ")
    for _ in range(x):
        print(f_1, end= " ")
        f_1, f_2 = f_2, f_1 + f_2
    print("")

user_input = int(input("Enter a non-negative integer denoting the number of terms of the Fibonacci series that you want to print: ")) 
print("Entered number is", user_input)

if user_input < 0:
    print(user_input, "is negative, Program terminates")
else:
    fibonacci_terms(user_input)
    print("Program terminates")
