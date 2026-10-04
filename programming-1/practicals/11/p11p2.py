'''
Write a program that prompts the user for a non-negative integer and 
uses a while loop to calculate that number of terms of the Fibonacci 
Series. Try to make the program as small and efficient as possible.
Save this program as p11p2.py.

Pseudocode
ask user for an integer input to denote the length of the fibonnaci seq
set t1 and t2 to 1
if input <= 0
    print program terminates
set a counter variable to 1 (denoting third term)
while counter <= input
    print(t1, end = " ")
    modify t1 to t2 and t2 to t1+t2
    increment counter
'''

user_input = int(input("Please enter an integer to denote the length of the Fibonacci sequence required: "))
t1, t2 = 1, 1
if user_input <= 0:
    print("You entered a number less than or equal to zero. Program terminates. ")

counter = 1
while counter <= user_input:
    print(t1, end=" ")
    t1, t2 = t2, t1 + t2
    counter += 1
