'''
Write a program that prompts the user for a series of non-negative integers and, for each of the numbers entered, uses a for loop to calculate that number of terms 
of the Fibonacci Series. The program should stop when a negative number is entered. Save this program as p11p3.py.

Pseudocode
ask user to enter an integer to denote the length of the fibonacci seq
while input >= 0:
    set term 1 and 2 to be equal to 1
    print the input
    if input == 0
        print there is no sequence of length 0
    else:
        for num in range(input)
            print(t1, end=" ")
            reset t1 to t2 and t2 to t1+t2
    ask for user input again
if input <0:
    print program terminates

'''

user_input = int(input("Please enter an integer to denote the length of the Fibonacci sequence required (Enter a negative number to terminate the program): "))

while user_input >= 0:
    t1, t2 = 1, 1
    print("You entered:", user_input)
    if user_input == 0:
        print("Nothing to print. ")
    else:
        for num in range(user_input):
            print(t1, end=" ")
            t1, t2 = t2, t1+t2
    user_input = int(input("\nPlease enter an integer to denote the length of the Fibonacci sequence required (Enter a negative number to terminate the program): "))
if user_input<0:
    print("You entered a negative number. Program terminates. ")