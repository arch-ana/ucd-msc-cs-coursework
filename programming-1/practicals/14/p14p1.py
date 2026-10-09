# Source - https://stackoverflow.com/a/1557584
# Posted by rogeriopvl, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-09, License - CC BY-SA 3.0

import time
start_time = time.time()

# def factorial_recursive(x):
#     if x == 0:
#         return 1
#     else:
#         return x*factorial_recursive(x-1)

def factorial_simple(x):
    factorial = 1
    for num in range(1,x+1):
        factorial *= num
    return factorial

user_input = int(input("Enter a number: "))

# print("Factorial by factorial_recursive", factorial_recursive(user_input))
print("Factorial by factorial_simple", factorial_simple(user_input))

print("--- %s seconds ---" % (time.time() - start_time))