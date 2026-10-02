# Ask the user to enter a password. If the password is correct (ie it matches 
# the password stored in the program), print “You have successfully logged 
# in.” and terminate the program. If the password is wrong print “Sorry, the 
# password is wrong.” and ask the user to enter the password three times. 
# If the user enters the correct password three times, print “You have 
# successfully logged in.” and terminate the program; otherwise print 
# “You have been denied access.” and terminate the program. Do not use a 
# loop construct to solve this problem.

# pseudocode
# assign the desired password to a variable (password)
# ask the user for the password as an input
# read the input into a variable input_password
# if input_password == password:
#     print log-in successful
# else:
#     print password is wrong
#     print you will need to enter the password thrice correctly
#     ask the user again for password as an input (first of three) and assign it to the input_password varialbe (rewriting it)
#     if input_password == password:
#         ask the user again for password as an input (second of three) and assign it to the input_password variable (rewriting it again)
#         if input_password == password:
#             ask the user again for password as an input (third of three) and assign it to the input_password variable (rewriting it for the last time)
#             if input_password == password:
#                 print log-in successful
#             else:
#                 print access denied
#         else:
#             print access denied
#     else:
#         print access denied

# program terminates


password = "dUbl!n"

input_password = input("Please enter your password: ")

if input_password == password:
    print("You have successfully logged in.")
else:
    print("Sorry, the password is wrong. You will need to enter the correct password three times now.")
    input_password = input("Please enter your password (1): ")
    if input_password == password:
        input_password = input("Please enter your password (2): ")
        if input_password == password:
            input_password = input("Please enter your password (3): ")
            if input_password == password:
                print("You have successfully logged in")
            else:
                print("You have been denied access")
        else:
            print("You have been denied access") 
    else:
        print("You have been denied acccess")

print("Program completed")
