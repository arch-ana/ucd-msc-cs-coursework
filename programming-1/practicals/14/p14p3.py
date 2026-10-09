# Pseudocode
# request user for an integer input and read it into a variable
# for number in range(2, user_input+1):
#     for num in range(2, number):
#         if number is a multiple of num:
#             number is not a prime number because num is not 1 or number itself
#             break (since we found that its not prime)
#         else:
#             number is prime

user_input = int(input("Please enter an integer > 0: "))
print("You entered", user_input)

for number in range(2, user_input+1):
    for num in range(2, number):
        if number%num == 0:
            print(number, "is not prime because ", number, "=", num, "*", number//num)
            break
    else:
        print(number, "is a prime number.")

print("Finished")
