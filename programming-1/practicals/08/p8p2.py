'''
Write a program that prompts the user for a number and uses a while 
loop to generate the “multiplication table” for that number from 1 
up to the number. For example, if the user were to enter “5”, the 
following table would be generated

1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25

Pseudocode:
request user for input and read it into a variable (user_input)
if input>0 do
    i = 1 (counter for rows)
    while i <= user_input do
        j = 1 (counter for cols)
        while j <= user_input do
            print i*j 
            increment j
        inrement i
        print newline
else:
    print you entered 0/negative number, program terminates
program finishes
'''

user_input = int(input("Please enter a positive number: "))

if user_input > 0:
    i = 1
    while i <= user_input:
        j = 1
        while j <= user_input:
            print (i*j, " ", end='')
            j += 1
        i += 1
        print("")
else:
    print("Sorry, you entered a non-positive number. Program terminates. ")
