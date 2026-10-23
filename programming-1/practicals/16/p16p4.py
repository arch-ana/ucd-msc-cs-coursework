# Pseudocode
# define a function taking one argument n:
#     initiate counter to 1 and total to 0
#     while counter is less than argument n:
#         if n is divisible by counter:
#             increment total by counter
#         increment counter by one
#     if total is equal to the argument n:
#         return True
#     return False 

# prompt user for a positive integer input
# if input >= 0:
#     for num in (1, user_input+1):
#         call the function to check if num is a perfect number and print it out
# else:
#     program terminates


def is_perfect_number(n):
    '''
    Function takes an integer argument and returns True if it is a perfect number. 

    The function assumes that the entered argument is an integer and returns True or False on whether the number if a perfect number. 
    A perfect number is one whose factors sum up to the number itself. 
    '''
    counter = 1
    total = 0
    while counter < n:
        if n%counter == 0:
            total += counter
        counter += 1
    if total == n:
        return True
    
    return False

user_input = int(input("Enter a positive integer: "))
if user_input >= 0:
    print("Perfect numbers up to and including", user_input, "are: ", end="")
    for num in range(1, user_input+1):
        if is_perfect_number(num) == True:
            print(num, end=" ")
else:
    print("Non-positive number entered. Program terminates. ")

