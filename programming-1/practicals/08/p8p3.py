'''
Write a program that uses a while loop to generate a simple 
multiplication table from 0 to 20. For example, were the user to enter 
“6”, the following table would be generated:

Times 6 Table
0 0 
1 6
2 12
3 18

Pseudocode
request user for an input and read it into a variable (user_input)
initiate counter for multiplication to zero
initiate limit with value 20 as we want to print multiples of 6 from
0 times to 20 times
limit = 20
if user_input >= 0:
    print(times input table)
    while counter <= limit:
        we print the counter and the product
        increment counter
else:
    print("Sorry, you did not enter a non-negative integer")

print program finished
'''

user_input = int(input("Please enter a non-negative integer: "))
counter, limit = 0, 20

if user_input >= 0:
    print("Times", user_input, "Table")
    while counter <= limit:
        print(counter,"\t",counter*user_input)
        counter += 1
else:
    print("Sorry, you entered a negative integer. Program terminates. ")


