'''
Write a program that prompts the user for a series of strings and counts and prints out the number of vowels 
(letters 'a', 'e', 'i', 'o' or 'u') in each string. The program should exit when an empty string is entered.

Pseudocode
ask user for a string input
while input is not empty:
    print the input
    set vowel_count variable to zero
    for letters in the input:
        if letter is a, e, i, u, A, E, I, O or U:
            increment vowel count
    print vowel count
    ask for next input
else:
    print you entered an empty string
'''
user_input = input("Enter a string. Press enter to terminate the program : ")

while user_input != "":
    print("You entered", user_input)
    vowel_count = 0
    for letter in user_input:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "O" or letter == "I" or letter == "U":
            vowel_count += 1
    print(user_input, "has", vowel_count, "vowels.")
    user_input = input("Enter a string. Press enter to terminate the program : ")
else:
    print("You pressed enter. Program terminates. ")
