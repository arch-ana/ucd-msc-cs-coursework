# Pseudocode
# def required function with single argument n (>= 1)
#     if n == 1
#         return 1
#     else
#         return 2**(n-1) + req_func(n-1)
# ask user to enter an integer input >= 1
# if_input<1:
#     terminate
# else:
#     for num in range(1, input+1):
#       print the term at num by calling the function with num as the argument

def req_func(x):
    '''
    Function returns nth term in sequence where f(n) = 1 for n=1, and f(n) = f(n-1)+2**(n-1) for n>1

    Function assumes that the input is an integer >= 1 and returns the nth term in the sequence
    '''
    if x == 1:
        return 1
    else:
        return 2**(x-1) + req_func(x-1)

user_input = int(input("Enter an integer >= 1: "))
print("You entered", user_input)

if user_input<1:
    print("Number less than 1, program terminates. ")
else:
    print("The series is: ", end="")
    for num in range(1, user_input+1):
        print(req_func(num), end=" ")
    print("")