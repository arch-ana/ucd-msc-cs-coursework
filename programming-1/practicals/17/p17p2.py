# Pseudocode
# define a function common divisors that takes two integer input arguments a and b:
#     
#     if b is a factor of a and neither a nor b are equal to 1:
#         initiate divisors tuple to contain 1 and b
#     elif a is a factor of b and neither a nor b are equal to 1:
#         initiate divisors tuple to contain 1 and a
#     else:
#         initiate divisors tuple to contain 1
#
#     for num in range(2, min(a,b)-1):
#         if num is a divisor of both a and b:
#             divisors is reset to include the contents of divisors and num
#         return divisors

# prompt user for two positive integer inputs
# if both integer inputs are > 0
#     call the common divisors function and print the common divisors
# else:
#     program terminates


def common_divisors(a, b):
    '''
    Function takes two integer argument inputs and returns their common divisors as a tuple.
    '''
    if a%b == 0 and (a!=1 and b!=1):
        divisors = (1, b,)
    elif b%a == 0 and (a!=1 and b!=1):
        divisors = (1, a,)
    else:
        divisors = (1,)
    for num in range(2, min(a, b)-1):
        if a%num == 0 and b%num == 0:
            divisors += (num,)
    
    return divisors

input_1 = int(input("Enter first number: "))
input_2 = int(input("Enter second number: "))

if input_1 >= 0 and input_2 >= 0:
    print("Common divisors of", input_1, "and", input_2, "are", sorted(common_divisors(input_1, input_2)))
else:
    print("At least one of the entered inputs are not a positive integer. Program terminates. ")