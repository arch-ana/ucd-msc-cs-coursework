# Pseudocode
# define function convertToDecimal that takes two inputs - a string of digits representing a number and a base:
#     initiate counter to -1 # we will work from right to left
#     initate decimal to 0 # we will add to this
#     initiate power to 0 

#     while counter >= -(len(stringNumber)):
#         decimal += int(stringNumber[counter])*(base**power))
#         decrement counter to move left
#         increment power to increase bit weight
#     return decimal
# prompt user for a number and a base
# if the number as int is positive and base is between 2 and 9:
#     call the convertToDecimal function and print the function
# else:
#     program terminates

def convertToDecimal(stringNumber, base):
    '''
    Function converts a number in a given base to its decimal equivalent

    Function takes a number as a string and a base as an integer and returns the decimal equivalent of the number using the base indicated. 
    '''
    counter = -1
    decimal = 0
    power = 0
    while counter >= -(len(stringNumber)):
        decimal += int(stringNumber[counter])*(base**power)
        counter -= 1
        power += 1
    
    return decimal

numberInput = input("Enter a number: ")
baseInput = int(input("What base is the entered number in?: "))

if int(numberInput) >= 0 and (2 <= baseInput <= 10):
    print("Decimal equivalent of", numberInput, "in base", baseInput, "is", convertToDecimal(numberInput, baseInput))
else:
    print("Invalid numbers, program terminates")


