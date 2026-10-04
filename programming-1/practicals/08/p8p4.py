'''
Write a program that uses a while loop to prompt the user for a series 
of integers and check whether each number is in one of the specified 
ranges:
• Number is equal to 0 
• Number is greater than 0 and less than or equal to 20 
• Number is greater than 20 and less than or equal to 40 
• Number is greater than 40 and less than or equal to 60 
• Number is greater than 60 and less than or equal to 80 
• Number is greater than 80 and less than or equal to 100 
• Number is greater than 100
The program should also count the number of numbers in each range. 
The program should continue until the user enters a number that is 
less than 0. Before finishing, the program should print out the analysis 
of the input, ie the number of numbers in each range.

Pseudocode
ask user for an integer input and save it to a variable user_input
initialize variables for each range and set them to zero
equal_to_zero = 0
less_than_or_equal_to_twenty = 0
less_than_or_equal_to_forty = 0
less_than_or_equal_to_sixty = 0
less_than_or_equal_to_eighty = 0
less_than_or_equal_to_hundred = 0
greater_than_hundred = 0

while user_input >= 0:
    if user_input == 0:
        increment equal_to_zero
    elif user_input <= 20:
        increment less_than_or_equal_to_twenty
    elif ..
    .
    .
    .
    .
    else:
        greater_than_hundred += 1
    
    ask user for an integer input and save it to a varialble user_input

else:
    print sorry, you entered a negative input

print numbers equal to 0: equal_to_zero
print numbers less than or equal to 20: less_than_or_equal_to_twenty
.
.
.
print numbers equal to hundred

print program finished

'''

user_input = int(input("Enter an integer. (Enter a negative integer to terminate)): "))
equal_to_zero = 0
less_than_or_equal_to_twenty = 0
less_than_or_equal_to_forty = 0
less_than_or_equal_to_sixty = 0
less_than_or_equal_to_eighty = 0
less_than_or_equal_to_hundred = 0
greater_than_hundred = 0

while user_input >= 0:
    print("Number entered is: ", user_input)
    if user_input == 0:
        print(user_input, "is equal to 0")
        equal_to_zero += 1
    elif user_input <= 20:
        print(user_input, "is greater than 0 and less than or equal to 20")
        less_than_or_equal_to_twenty += 1
    elif user_input <= 40:
        print(user_input, "is greater than 20 and less than or equal to 40")
        less_than_or_equal_to_forty += 1
    elif user_input <= 60:
        print(user_input, "is greater than 40 and less than or equal to 60")
        less_than_or_equal_to_sixty += 1
    elif user_input <= 80:
        print(user_input, "is greater than 60 and less than or equal to 80")
        less_than_or_equal_to_eighty += 1
    elif user_input <= 100:
        print(user_input, "is greater than 80 and less than or equal to 100")
        less_than_or_equal_to_hundred += 1
    else:
        print(user_input, "is greater than 100")
        greater_than_hundred += 1
    user_input = int(input("Enter an integer. (Enter a negative integer to terminate)): "))

else:
    print("You entered a negative number. Following is a range analysis of your numbers:")

print("Numbers equal to zero: ", equal_to_zero)
print("Numbers greater than zero and less than or equal to 20: ", less_than_or_equal_to_twenty)
print("Numbers greater than 20 and less than or equal to 40: ", less_than_or_equal_to_forty)
print("Numbers greater than 40 and less than or equal to 60: ", less_than_or_equal_to_sixty)
print("Numbers greater than 60 and less than or equal to 80: ", less_than_or_equal_to_eighty)
print("Numbers greater than 80 and less than or equal to 100: ", less_than_or_equal_to_hundred)
print("Numbers greater than 100: ", greater_than_hundred)

print("Program finished")
    
