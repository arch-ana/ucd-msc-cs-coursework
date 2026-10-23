
print("Program to calculate the date, month and year in an Indian academic year 2026-2027 of a given day.")
print("Enter zero or a negative number to exit.")
print("")
user_input = int(input("Enter the day for which you want to find the date (a positive integer): "))

month = ""
year = 0
day = 0

# to keep going until non-positive input, use while loop on
# user input variable
while user_input > 0:
    print("You entered:", user_input)
    # check the number a
    if user_input <= 365:
        if user_input <= 31:
            month = "August"
            year = 2026
            day = user_input
        elif user_input <= 61:
            month = "September"
            year = 2026
            day = user_input - 31
        elif user_input <= 92:
            month = "October"
            year = 2026
            day = user_input - 61
        elif user_input <= 122:
            month = "November"
            year = 2026
            day = user_input - 92
        elif user_input <= 153:
            month = "December"
            year = 2026
            day = user_input - 122
        elif user_input <= 184:
            month = "January"
            year = 2027
            day = user_input - 153
        elif user_input <= 212:
            month = "February"
            year = 2027
            day = user_input - 184
        elif user_input <= 243:
            month = "March"
            year = 2027
            day = user_input - 212
        elif user_input <= 273:
            month = "April"
            year = 2027
            day = user_input - 243
        elif user_input <= 304:
            month = "May"
            year = 2027
            day = user_input - 273
        elif user_input <= 334:
            month = "June"
            year = 2027
            day = user_input - 304
        else:
            month = "July"
            year = 2027
            day = user_input - 334

        print("Day number", user_input, "is", day, month, year)
    else:
        print("Day number", user_input, "is not in the Indian academic year 2026-2027!")

    user_input = int(input("Enter the day for which you want to find the date (a positive integer): "))
    

print("Finished!")