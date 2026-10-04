'''
Write a program that prompts the user for a series of integers and, for each of the numbers entered, performs exhaustive enumeration to find the integer cube 
root of the number. If the number is not a perfect cube, the program should print out a message to that effect. Note that the program should work for negative 
numbers as well as positive numbers. The program should exit when a 0 is entered.

Pseudocode
ask user for a non-zero integer input
while input != 0:
    initiate counter to 1
    while counter <= absolute value of input:
        if counter***3 == input:
            if user input is positive:
                print counter is the cube root of input
            else:
                print -counter is the cube root of input
        else:
            increment counter
    else:
        print number is not a perfect cube
    ask user for the next input
else:
    print you entered zero

'''
user_input = int(input("Enter an integer. Enter zero to terminate the program: "))

while user_input != 0:
    counter = 1
    while counter <= abs(user_input):
        if counter**3 == abs(user_input):
            if user_input < 0:
                print(-counter, "is the cube root of", user_input)
            else:
                print(counter, "is the cube root of", user_input)
            break
        else:
            counter+= 1
    else:
        print("Entered number is not a perfect cube and does not have an integer cube root")
    user_input = int(input("Enter an integer. Enter zero to terminate the program: "))
else:
    print("You entered zero. Program terminates. ")