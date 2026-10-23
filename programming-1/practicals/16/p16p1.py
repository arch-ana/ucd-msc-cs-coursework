# pseudocode

# def required function to take an argument n
#     define the base case
#     if n == 1:
#         return 2
#     else:
#         return 2*req_func(n-1)

# ask user for an integer input >= 1

# while input >= 1:
#     call the function and print the result
#     ask user for input again

# program terminates

def req_func(n):
    '''
    Function returns the nth term in the sequence

    Function assumes that the input >=1 and return the nth term in a sequence where f(n) = 2 if n = 1 and f(n) = 2*f(n-1) for n>1
    '''
    print("Calling req_func(", n, ")", sep="")
    if n == 1:
        print("Base case; returns 2")
        return 2
    else:
        result = 2*(req_func(n-1))
        print("Returning 2*(req_func(", n-1,")); result is ", result, sep="")
        return result

user_input = int(input("Please enter an integer >=1 [Enter zero or a negative number to terminate the program]: "))

while user_input >= 1:
    print("Term", user_input, "in the sequence is", req_func(user_input))
    user_input = int(input("Please enter an integer >=1 [Enter zero or a negative number to terminate the program]: "))
else:
    print("Zero or negative number entered. Program terminates")
