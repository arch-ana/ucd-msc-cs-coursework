# Pseudocode
# define function divisors that takes an integer argument n:
#     initiate a tuple divisors with elements 1, n
#     for num in range(2, (n//2) + 1):
#         if n is divisible by num and num is not in divisors already:
#             if num is not the same as n//num
#                 modify divisors to be contents of divisors, num and n//num
#             else:
#                 modify divisors to be contents of divisors, and num
# prompt user for a positive integer input
# if user_input <= 0:
#     program terminates
# else:
#     call the divisors function and print out the divisors of user_input


def divisors(n):
    '''
    Function takes an integer input n and returns all positive factors of n. 
    '''
    divisors = (1,)
    if n != 1:
        divisors = (1, n,)
    for num in range(2, (n//2)+1):
        if n%num == 0 and num not in divisors:
            if num != n//num:
                divisors += (num, n//num,)
            else:
                divisors += (num,)
    return sorted(divisors)

user_input = int(input("Enter a number: "))

if user_input <= 0:
    print("Not a positive number, program terminates")
else:
    print("Divisors of", user_input, "are: ", end="")
    for div in divisors(user_input):
        print(div, end=" ")