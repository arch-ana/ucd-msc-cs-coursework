# Write a password checking program to keep track of how many times a 
# user has entered their password incorrectly. Store a password in your 
# program. If the user enters the password incorrectly more than three 
# times, print “You have been denied access.” and terminate the program. 
# If the password is correct, print “You have successfully logged in.” 
# and terminate the program. Do not use a loop construct to solve this 
# problem.

# Pseudocode
# Create a variable password with a randomly selected "password"
# Ask user for their password as an input
# read the input into a variable (input_password)
# if password == input_password:
#     print You have successfully logged in
# else:
#     ask for input from user again 
#     read this into input_password variable (rewrite its value)
#     if input_password == password:
#         print You have successfully logged in
#     else:
#         ask for input from user again
#         read it into input_password
#         if input_password == password:
#             print successful log-in
#         else:
#             ask for input from user for a final time
#             if input_password == password:
#                 print succesfful log-in
#             else:
#                 print access denied
# Program completed    


password = "dUbl!n"

input_password = input("Attempt one: Please enter password: ")

if input_password == password:
    print("You have successfully logged in")
else:
    input_password = input("Attempt two: Please enter your password: ")
    if input_password == password:
        print("You have successfully logged in")
    else:
        input_password = input("Attempt three: Please enter your password: ")
        if input_password == password:
            print("You have successfully logged in")
        else:
            input_password = input("Final attempt: Please enter your password: ")
            if input_password == password:
                print("You have successfully logged in")
            else:
                print("You have been denied access")
            
print("Program completed")
