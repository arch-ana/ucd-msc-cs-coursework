# Pseudocode
# define a function isPalindrome that takes a single string argument str:
#     first strip the string of all non-alphabetical characters
#     initiate a string validWord to the empty string ""
#     for character in str:
#         if character is a letter from the alphabet:
#             concatenate validWord with character
    
#     check if validword is a palindrome by comparing characters on opposite ends
#     initiate indexes for the left end and right end of the word
#     left, right = 0, len(validWord)-1
#     while left < right:
#         at any point if the two characters are not the same, return false
#         if validWord.lower()[left] != validWord.lower()[right]:
#             return False
#         else:
#             move to the next characters +1 on the left and -1 on the right
#             left += 1
#             right -= 1
#     once we go through the word without returning False, return True

# prompt user for a string input
# call the isPalindrome function using input as the argument and return True if isPalindrome returns True, else return False

def isPalindrome(s):
    '''
    isPalindrome function takes a string as its input argument and returns True if the string is a palindrome, and returns False otherwise. 

    isPalindrome is not case sensitive, i.e., RaceCaR is a palindrome. 
    '''
    validWord = ""
    for character in s:
        if character.isalpha():
            validWord += character

    if validWord == "":
        return False

    left, right = 0, len(validWord)-1
    while left<right:
        if validWord[left].lower() != validWord[right].lower():
            return False
        else:
            left += 1
            right -= 1    
    return True

user_input = input("Enter a word to check if it is a palindrome: ")

if user_input != "":
    if isPalindrome(user_input):
        print(user_input, "is a palindrome")
    else:
        print(user_input, "is not a palindrome")
else:
    print("Empty string input, program terminates. ")