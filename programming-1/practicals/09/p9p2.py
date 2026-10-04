'''
Write a program that prompts the user for a series of positive integers 
and, for each of the numbers entered, uses a for loop to calculate the 
sum of the positive integers up to and including that number. The 
program should stop when a non-positive number is entered. Save this 
program as p9p2.py.

Pseudocode
request user for an input and store it in a variable user_input
while user_input>=0:
    print entered input is user_input
    counter = 1
    sum = 0
    for num in range(user_input):
        sum += counter
        counter += 1
    request user for input again
else:
    print you have entered a negative number, program terminates
    
'''

user_input = int(input("Please enter a positive integer. Enter a negative integer to terminate the program: "))

while user_input>0:
    counter = 1
    sum = 0
    for num in range(user_input):
        sum += counter
        counter += 1
    print("Sum of integers up to and including", user_input, "is", sum)
    user_input = int(input("Please enter a positive integer. Enter a negative integer to terminate the program: "))
else:
    print("You entered a non-positive integer. Program terminates.")