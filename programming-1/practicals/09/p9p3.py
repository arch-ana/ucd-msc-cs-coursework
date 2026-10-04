'''
Write a program that prompts the user for a positive integer and uses a for loop to calculate the factorial of that number.

Pseudocode
ask for a positive integer user input and save it in a variable (user_input)
if user_input < 0:
    print("You entered a negative number, program terminates")
else:
    initiate factorial and counter variables to 1
    factorial, counter = 1, 1 
    while counter <= user_input:
        factorial *= counter
        counter += 1
    print "factorial of user_input is", factorial
    print "program terminates"
'''

user_input = int(input("Please enter a positive integer: "))

if user_input<0:
    print("You entered a negative number. Program terminates")
else:
    factorial = 1
    for num in range(user_input):
        factorial*=(num+1)
    print("Factorial of", user_input, "is", factorial)
    print("Program terminates")

