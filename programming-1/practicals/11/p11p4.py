'''
Write a program that prompts the user for an integer and calculates that number of Catalan Numbers using one or more of the above techniques.

ask user for an integer input greater than 0
if input >= 1:
    print input
    for num in range(input):
        (use variables to denote the terms for the numerator and denominator of the catalan sequence definiiton)
        a = 2*num
        b = num
        c = num+1
        similarly initiate each of their factorial values to 1
        a_fact, b_fact... = 1, 1, 1

        initiate counter variable to 1
        while counter <= a:
            a_fact *= counter
            increment counter
        (repeat this code block for b and c)

        print(a_fact//(b_fact*c_fact), end = " ")
'''

user_input = int(input("Enter an integer greater than zero. The program will print as many Catalan numbers: "))
if user_input >= 1:
    print("You entered", user_input)
    for num in range(user_input):
        #variables required
        a, b, c = 2*num, num, num+1
        a_fact, b_fact, c_fact = 1, 1, 1
        counter = 1
        while counter <= a:
            a_fact *= counter
            counter += 1
        counter = 1
        while counter <= b:
            b_fact *= counter
            counter+= 1
        counter = 1
        while counter <= c:
            c_fact *= counter
            counter += 1

        print(a_fact//(b_fact*c_fact), end=" ")
else:
    print("You entered zero or a negative number. Program terminates. ")
