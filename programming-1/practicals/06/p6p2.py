# Write a program that prompts the user for three numbers (ints), 
# examines the numbers and prints out the largest odd number among 
# them. If none of them is a negative odd number, the program should 
# print out a message to that effect. The program should then terminate.

# Pseudocode
# Prompt the user for the first number
# Read the first number to a variable (num1)
# Prompt the user for a second number
# Read the second number to a variable (num2)
# Prompt the user for a third number
# Read the third number to a varialbe (num3)
# if num1 is even and num2 is even and num3 is even:
#     print None of the numbers are odd
# else:
#     if num1 is odd: 
#         set a max_odd variable to equal num1
#    
#     if num2 is odd:
#         if num1 was even  
#             create a max_odd variable and set its value to be num2
#         else if num1 was odd to begin with:
#             if if num2 > max_odd:
#                 change the value of max_odd to be that of num2
#    
#     if num3 is odd:
#         if both num1 and num2 were even:
#             max_odd is assinged value of num3
#         else:
#             if num3 > max_odd:
#                 change the value of max_odd to that of num3
#
#     print("The highest odd number is", max_odd)
#
# if (num1>=0 or num1%2==0) and (num2>=0 or num2%2==0) and (num3>=0 or num3%2==0):
#     print("There are no negative odd numbers")
# Program terminates

num1 = int(float(input("Please enter the first integer: ")))
num2 = int(float(input("Please enter the second integer: ")))
num3 = int(float(input("Please enter the third integer: ")))

if num1%2 == 0 and num2%2 == 0 and num3%2 == 0:
    print("None of the numbers are odd")
else:
    if num1%2 != 0: 
        max_odd = num1
    
    if num2%2 != 0:
        if num1%2 == 0:
            max_odd = num2
        else:
            if num2 > max_odd:
                max_odd = num2
    
    if num3%2 != 0:
        if num1%2 == 0 and num2%2 == 0:
            max_odd = num3
        else:
            if num3 > max_odd:
                max_odd = num3

    print("The highest odd number is", max_odd)

if (num1>=0 or num1%2==0) and (num2>=0 or num2%2==0) and (num3>=0 or num3%2==0):
    print("There are no negative odd numbers")

print("Program completed")
