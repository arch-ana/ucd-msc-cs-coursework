# define function ispalindrome that takes one string argument:
#     if length of string is 0 or 1:
#         return True
#     else:
#         return first letter of string is the same as the last letter of the string AND ispalindrome(string[1:-1])

# define function convertletters that takes one string argument:
#     initiate a string called accept and set it equal to 'abcdefghijklmnopqrstuvwxyz'
#     initiate a string validword to an emptystring
#     for letters (lowercased) in the string argument:
#         if the letter exists in the acceptstring:
#             concatenate it with validword
#     return validword

# prompt user for a string input
# call the validword function within the ispalindrom function on user_input, if true:
#     print that userinput is a palindrome
# else:
#     print that the userinput is not a palindrome

def isPalindrome(s):
    '''Checks whether the string s is a palindrome. 
    
    Assumes that s is a str with only lowercase letters and no non-letters. 
    Returns True if s is a palindrome;
    Returns False otherwise. 
    Recursive function.
    Has print statements to trace its operation.'''
    print("isPalindrome function called with argument", s)
    if len(s) == 0 or len(s) == 1:
        print("About to return True from isPalindrome from the base case")
        return True
    else:
        result = s[0] == s[-1] and isPalindrome(s[1:-1])
        print("About to return result", result, "from isPalindrome with argument", s)
        return result

def convertLetters(s):
    '''
    Function takes a string input and outputs a subset of the string that only contains all the alphabetical characters in it in lowercase. 
    The returned string retains the order of characters as they appear in the input string. 
    '''
    accept = 'abcdefghijklmnopqrstuvwxyz'
    validWord = ""
    for letter in s.lower():
        if letter in accept:
            validWord += letter
    return validWord

user_input = input("Enter word: ")
if isPalindrome(convertLetters(user_input)):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")