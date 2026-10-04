'''
Taking the program to calculate the factorial of a number presented in class, investigate how it would be possible to have just two cases, one where the number 
is less than 0 and one where it isn't. Rewrite the program to do this.

Pseudocode
ask user for the number for which theyd like to find the factorial

if input<0
    terminate program
else
    factorial = 1
    set counter variable to 2
    while counter <= input:
        reset factorial variable to factorial*counter
        increment counter
    print factorial of input is factorial

'''

user_input = int(input("Enter the number for which you wish to calculate the factorial (an int >= 0): "))

if user_input < 0:
    print("Error: Number entered was less than zero. ")
else:
    factorial = 1
    counter = 2
    while counter<=user_input:
        factorial *= counter
        counter += 1
    print("Factorial of", user_input, "is", factorial)