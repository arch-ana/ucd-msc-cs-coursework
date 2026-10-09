# Pseudocode
# request user for an integer input and read it into a variable
# for number in range(2, user_input+1):
#     for num in range(2, number):
#         if number is a multiple of num:
#             number is not a prime number because num is not 1 or number itself
#             for factors in range(2, number):
#                 if number%fact == 0:
#                     fact and number//fact are factors of number
#             break (since we found that its not prime)
#         else:
#             number is prime

user_input = int(input("Please enter a number: "))
print("You entered", user_input)

for number in range(2, user_input): ## up to 20
    for num in range(2, number):
        if number%num == 0:
            print(number, "is not prime. Its factors other than 1 and", number, "are: ")
            for facts in range(2,number):
                if number%facts == 0:
                    print(facts, "and", number//facts)
            break
    else:
        print(number, "is a prime number.")

print("Finished")
