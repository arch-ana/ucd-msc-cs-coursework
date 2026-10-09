# Pseudocode
# def required function with single argument n
#     if n == 1:
#         return 2
#     else:
#         return n + req_func(n-1)
# request user for an integer input>=1 and read it into a variable
# if input less than 1, terminate program
# else:
#     for num in range(1, user_input+1):
#         in a print function call the function with num as the argument

def req_func(n):
    '''
    Function calculates the nth term of a sequence where f(n) = 2 when n = 1, and f(n) = n + f(n-1) if n>1

    Function assumes that n>=1 and returns the nth term in the sequence 
    '''
    if n == 1:
        return 2
    else:
        return n + req_func(n-1)

user_input = int(input("Enter an integer >= 1: "))

if user_input<1:
    print("You entered a number less than 1, program terminates.")
else:
    print("The series is: ", end="")
    for num in range(1, user_input+1):
        print(req_func(num), end=" ")
    print("")

    