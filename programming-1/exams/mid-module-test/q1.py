#print what the program does with a linebreak after
print("Program to calculate the number of integers evenly divisible by 5, 7, 13, 17 and 19\n")
print("")

#get user input and read it into a variable, print it onto the screen
user_input = int(input("Enter a positive integer: "))
print("You entered:", user_input)

#initiate a counter to start from 1 (eventually it will go up to the number specified by the user)
counter = 1

#initiate variables denoting numbers divisible by 5, 7, 13, 17 and 19 to zero
div_5 = 0
div_7 = 0
div_13 = 0
div_17 = 0
div_19 = 0

# use if statement to ensure that the integer is positive, if it is, we move to the while loop
if user_input > 0:
    # within the while loop, check the divisibility of each number and accordingly increment the corresponding variable
    while counter <= user_input:
        if (counter%5 == 0):
            div_5 += 1
        if (counter%7 == 0):
            div_7 += 1
        if (counter%13 == 0):
            div_13 += 1
        if (counter%17 == 0):
            div_17 += 1
        if (counter%19 == 0):
            div_19 += 1 
        # increment counter
        counter += 1
    
    print("Number of numbers from 0 up to and including", user_input, "evenly divisible by 5:", div_5)
    print("Number of numbers from 0 up to and including", user_input, "evenly divisible by 7:", div_7)
    print("Number of numbers from 0 up to and including", user_input, "evenly divisible by 13:", div_13)
    print("Number of numbers from 0 up to and including", user_input, "evenly divisible by 17:", div_17)
    print("Number of numbers from 0 up to and including", user_input, "evenly divisible by 19:", div_19)
    

else:
    print("Number entered should be > 0.")

print("Finished!")