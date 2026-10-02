# Write a program that prompts the user for a year and checks whether 
# the year is a leap year. Use my algorithm from Lecture 8. Ensure you 
# understand how this program works and, in particular, how the conditions 
# work.

# Pseudocode
# Ask the user for a year as an input
# Read the input year into a variable (year)
# if year >= 0:
#     if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#         print it is a leap year
#     else:
#         print it is not a leap year
# else:
#     print year should be > 0
# program terminates

year = int(float(input("Please enter a year: ")))
print("Year entered:", year)

if year >= 0:
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    print("Year must be greater than zero")

print("Program completed")
    