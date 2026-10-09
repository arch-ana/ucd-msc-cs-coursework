# Pseudocode
# define required function with argument n:
#     if n == 0:
#         return 13
#     elif n == 1:
#         return 8
#     else:
#         return req_func(n-2) + (13*req_func(n-1))
# ask for user input, store it, when input is less than zero, terminate program
# else print statement calling the function with userinput as argument and ask for input again (until input < 0)


def req_func(n):
    '''
    Function returns the nth term in the series f where f(n) = 13 when n = 0, f(n) = 8 for n = 1, and f(n) = f(n-2) + 13*f(n-1) for n>1

    Function assumes an input >= 0 and returns the nth term in the series    
    '''
    print("Calling req_func(", n, ")", sep="")
    if n == 0:
        print("Reached base case, returns 13")
        return 13
    elif n == 1:
        print("Reached base case, returns 8")
        return 8
    else:
        result = req_func(n-2) + (13*req_func(n-1))
        print("Returning req_func(", n-2, ") + (13*req_func(",n-1,")): ", result, sep="")
        return result

user_input = int(input("Enter an integer >=0: "))

while user_input>=0:
    print("Term", user_input, "in sequence is", req_func(user_input))
    user_input = int(input("Enter a number: "))
else:
    print("Number less than zero, program terminates")
