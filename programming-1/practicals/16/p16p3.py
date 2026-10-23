# Pseudocode

# define a function that takes two arguments:
#     initiate counter to value 1
#     initiative empty tuple to contain common divisors
#     while counter <= min(the two arguments):
#         if counter divides both arguments:
#             add counter to the tuple of divisors
#         increment counter 

#     return tuple divisors 

# Prompt user for two positive integers
# if either of the numbers are not positive:
#     print error message
# else:
#     call the divisors function and print all the divisors

#     initiate a sum variable to zero
#     for div in divisor:
#         add div to sum
#     print the final sum

# program terminates

def common_divisors(a, b):
    '''
    Function takes two integer arguments a and b and returns its common divisors

    Function assumes that input arguments are integers and finds divisors common to both of them 
    '''
    divisors = ()
    counter = 1
    while counter <= min(a,b):
        if a%counter == 0 and b%counter == 0:
            divisors += (counter,)
        counter += 1

    return divisors

input_1 = int(input("Enter first positive integer: "))
input_2 = int(input("Enter second positive integer: "))

if input_1 <=0 or input_2 <= 0:
    print("You did not enter positive integers. Program terminates.")
else:
    result = common_divisors(input_1, input_2)
    print("Common factors of", input_1, "and", input_2, "are: ", end="")
    print(result)

    total = 0
    for res in result:
        total += res
    print("The sum of all common divisors is: ", total)
    
print("Program terminates")