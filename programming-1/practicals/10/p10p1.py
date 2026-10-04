'''
Write a program that prompts the user for an integer and performs exhaustive enumeration to find the integer square root of the number. By “exhaustive enumeration”, 
we mean that we start at 0 and succcessively go through the integers, checking whether the square of the integer is equal to the number entered.
If the number is not a perfect square, the program should print out a message to that effect. The program should exit when a negative number is entered.

Pseudocode
request user for input
if input >= 0 do:
    set counter variable equal to zero
    while counter <= input do:
        if counter**2 is equal to user input:
            print counter is the square root of input
            break 
        else
            increment counter
    else:
        print number does not have an integer square root
else:
    print you entered a negative number

'''
user_input = int(input("Enter an integer. Enter a negative integer to terminate the program: "))

if user_input >= 0:
    counter = 0
    while counter <= user_input:
        if counter**2 == user_input:
            print(counter, "is the square root of", user_input)
            break
        else:
            counter+= 1
    else:
        print("Entered number is not a perfect square and does not have an integer square root")
else:
    print("You entered a negative number. Program terminates. ")