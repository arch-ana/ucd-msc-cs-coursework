# (a) Write a function that takes as its two arguments a number and a tolerance and, using
# the technique exposed in lectures, returns an approximation of the square root of the number that is within the tolerance.
# (b) Write a program that prompts the user for a floating-point number and checks that the
# number entered is non-negative. If it is, it calls the function defined in part (a) with the number and a tolerance defined in the program and prints out 
# the square root of the number; if not, it prints out an appropriate error message.

# Pseudocode
# def function with arguments number and tolerance:
#     set a step indicating increments that we check
#     initiate value of root to zero
#     initiate number of guesses to zero
#     while num-root**2 is still greater than or equal to tolerance AND root is still less than or equal to num
#         increment root by the step
#         increment numGuesses by one
#         print the numGuesses if its reached a multiple of 100000
#     check how the while loop ended using 
#     if num-root**2 less than tolerance:
#         we have found a root within tolerance, return root
#     else:
#         we do not have a root within desired tolerance, return None


# request user for number whose root they would like to calculate
# set desired tolerance limit
# if input < 0:
#     print error message and terminate
# else:
#     run the square root function
#     if the return value is equal to None:
#         print there is no root within desired tolerance
#     else:
#         print the root

def sq_root(num, tolerance):
    '''
    Function to find the square root of a floating point number within a desired tolerance of error
    
    Assumes that num and tolerance are non-negative and returns the approximate square root of num
    '''
    step = tolerance ** 2
    root = 0.0
    numGuesses = 0
    while abs(num-root**2) >= tolerance and root <= num:
        root += step
        numGuesses += 1
        if numGuesses % 100000 == 0:
            print("Still running. Number of guesses:", numGuesses)
    if abs(num-root**2) < tolerance:
        return root
    else:
        return None

user_input = float(input("Please enter a floating number whose square root you would like to calculate: "))
tolerance = 0.01
print("You entered number", user_input, "and tolerance of", tolerance)

if user_input < 0:
    print(user_input,"is negative. ")
else:
    square_root = sq_root(user_input, tolerance)
    if square_root != None:
        print("Square root of", user_input, "is", square_root)
    else:
        print("The number does not have a square root within the desired tolerance")
print("Program terminates. ")

