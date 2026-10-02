# Write a program that prompts the user for a year and checks 
# whether the year is a leap year. Use the algorithm on the 
# Wikipedia page (also given in Lecture 8). Ensure you understand 
# how this program works and, in particular, how the conditions work.

# Pseudocode
# Ask user to enter a year as an input
# read input into a variable (year)
# if year >= 0:
#     if year%4 == 0:
#         check if it is divisible by 100
#         if year%100 != 0:
#             check if it is divisible by 400
#             if year%400 == 0:
#                 print leap year
#             else:
#                 print not leap year
#         else:
#             print not leap year
#     else:
#         print not leap year
# else:
#     print year should be > 0

# program terminates

year = int(float(input("Enter year: ")))
print("Year entered is:", year)

if year >= 0:
    if year%4 != 0:
        print("It is a common year")
    else:
        if year%100 != 0:
            print("It is a leap year")
        else:
            if year%400 != 0:
                print("It is a common year")
            else:
                print("It is a leap year")
else:
    print("Year entered must be greater than 0")

print("Program completed")
