# pseudocode

# def required function to take an argument n
#     define the base case
#     if n == 1:
#         return 2
#     else:
#         return 2*req_func(n-1)

# ask user for an integer input >= 1

# if input >= 1:
#     for num in range(user_input):
#         call the function and print the result with num+1 as argument
#     ask user for input again

# program terminates

def req_func(n):
    '''
    Function returns the nth term in the sequence

    Function assumes that the input >=1 and return the nth term in a sequence where f(n) = 2 if n = 1 and f(n) = 2*f(n-1) for n>1
    '''
    if n == 1:
        return 2
    else:
        result = 2*(req_func(n-1))
        return result

user_input = int(input("Please enter an integer >=1 [Enter zero or a negative number to terminate the program]: "))

if user_input >= 1:
    print("Sequence is:", end=" ")
    for num in range(user_input):
        print(req_func(num+1), end=" ")
    print("\nProgram terminates")
else:
    print("Zero or negative number entered. Program terminates")
