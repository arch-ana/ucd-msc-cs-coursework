# Pseudocode
# define required function with argument n:
#     if n == 0:
#         return 13
#     elif n == 1:
#         return 8
#     else:
#         return req_func(n-2) + (13*req_func(n-1))

# ask user for an input and store it in a variable
# if input>=0:
#     for num in range(user_input):
#         print the number in the sequence by calling the function with num as the argument
# else:
#     print program terminates

def req_func(n):
    '''
    Function returns the nth term in the series f where f(n) = 13 when n = 0, f(n) = 8 for n = 1, and f(n) = f(n-2) + 13*f(n-1) for n>1

    Function assumes an input >= 0 and returns the nth term in the series    
    '''
    if n == 0:
        return 13
    elif n == 1:
        return 8
    else:
        return req_func(n-2) + (13*req_func(n-1))

user_input = int(input("Enter a number: "))

if user_input>=0:
    print(user_input, "terms in the sequence are: ", end="")
    for num in range(user_input):
        print(req_func(num), end=" ")
    print("")
else:
    print("Number less than 0 entered. Program terminates. ")