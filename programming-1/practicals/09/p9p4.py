'''
Write a program that prompts the user for a series of positive integers and, for each of the numbers entered, uses a while loop to calculate the factorial of that 
number. The program should stop when a negative number is entered. Save this program as p9p4.py.

Pseudocode
request user for input
while input >= 0 do
    initiate factorial and counter to 1
    while counter <= 0 do
        reset factorial value to factorial*counter
        increment counter
    print factorial of input is factorial
    ask for user input again
else do
    print you entered a negative number, program terminates

'''
user_input = int(input("Please enter a positive integer. Enter a negative integer to terminate the program: "))

while user_input>=0:
    factorial = 1
    counter = 1
    while counter <= user_input:
        factorial *= counter
        counter += 1
    print("Factorial of", user_input, "is", factorial)
    user_input = int(input("Please enter a positive integer. Enter a negative integer to terminate the program: "))
else:
    print("You entered a negative integer. Program terminates.")