'''
Write a program that prompts the user for a positive integer and 
uses a while loop to calculate the sum of the positive integers up to 
and including that number.

Pseudocode:
ask the user for a positive integer input and read it into a variable (user_input)
initiate a counter variable to go from 1 to the user_input
counter = 1
initiate a sum variable and set it to zero
sum = 0
if user_input < 0:
    print sorry, you did not enter a positive integer
else:
    while counter <= user_input:
        sum += counter
        counter += 1

print the sum is, sum
'''

user_input = int(input("Please enter a positive integer: "))

counter, int_sum = 1, 0

if user_input = 0:
    while counter <= user_input:
        int_sum += counter
        counter += 1
    print("Sum of integers up to and including", user_input, "is", int_sum)
else:
    print("Sorry, you did not enter a positive integer")

print("Program finished")
