'''Write a program that uses a while loop to prompt the user for a 
series of numbers, check whether each number is divisble by 2, 3, 5 
or 7 and print out which of 2, 3, 5 or 7 it is divisible by. Execution 
of the program continues until a negative number is entered.

Pseudocode
request user for input, read it into a variable
while input >= zero do
    print input
    if input%2 == 0:
        print divisible by 2
    (repeat for 3, 5, 7)
    prompt user for input again
else do:
    print program finishes
'''

user_input = int(input("Please enter a positive number. Enter a negative number to end the program: "))

while user_input >= 0:
    print("You have entered", user_input)
    if user_input%2 == 0:
        print(user_input, "is divisible by 2")
    if user_input%3 == 0:
        print(user_input, "is divisible by 3")
    if user_input%5 == 0:
        print(user_input, "is divisible by 5")
    if user_input%7 == 0:
        print(user_input, "is divisible by 7")
    if user_input%2 != 0 and user_input%3 != 0 and user_input%5 != 0 and user_input%7 != 0:
        print(user_input, "is not divisible by 2, 3, 5 or 7")
    user_input = int(input("Please enter a a positive number. Enter a negative number to end the program: "))
else:
    print("You entered a negative number. Program terminates. ")