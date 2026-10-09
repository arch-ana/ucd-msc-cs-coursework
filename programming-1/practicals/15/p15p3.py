# Pseudocode
# def required function with single argument n (>= 1)
#     if n == 1
#         return 1
#     else
#         return 2**(n-1) + req_func(n-1)
# while user_input>=1:
#     print the term by calling the function with argument user_input
#     ask user for input again
# else:
#     print that anything less than 1 terminates program and terminate

def req_func(n):
    '''
    Function returns nth term in sequence where f(n) = 1 for n=1, and f(n) = f(n-1)+2**(n-1) for n>1

    Function assumes that the input is an integer >= 1 and returns the nth term in the sequence
    '''
    print("Returning req_func(", n, ")", sep="")
    if n == 1:
        print("Reached base case, returns 1")
        return 1
    else:
        result = 2**(n-1) + req_func(n-1)
        print("Calling 2**", n-1, "+ req_func(", n-1,"): ", result, sep="")
        return result

user_input = int(input("Enter an integer >= 1: "))

while user_input>=1:
    print("Term", user_input, "is", req_func(user_input))
    user_input = int(input("Enter an integer >= 1: "))
else:
    print("Number less than 1 entered. Program terminates. ")
