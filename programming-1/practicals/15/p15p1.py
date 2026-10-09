# Pseudocode
# def required function with single argument n
#     if n == 1:
#         return 2
#     else:
#         return n + req_func(n-1)
# request user for an integer input>=1 and read it into a variable

# while input>=1:
#     print the term by calling the req_func with input as argument
#     ask for user input again (until 0 or a negative number is entered)
# else:
#     print input <1 terminates the program


def req_func(n):
    '''
    Function calculates the nth term of a sequence where f(n) = 2 when n = 1, and f(n) = n + f(n-1) if n>1

    Function assumes that n>=1 and returns the nth term in the sequence 
    '''
    print("req_func of ", n, " called")
    if n == 1:
        print("Reached base case, returning 2")
        return 2
    result = n + req_func(n-1)
    print("Calling ", n, " + ", " req_func(", n-1, ") = ", result, sep="")
    return result

user_input = int(input("Enter an integer >= 1: "))

while user_input>=1:
    print("The result is", req_func(user_input))
    user_input = int(input("Enter an integer >= 1: "))
else:
    print("You entered a number equal to or less than zero. Program terminates. ")
 