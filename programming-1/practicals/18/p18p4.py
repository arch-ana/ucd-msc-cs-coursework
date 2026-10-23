# Pseudocode
# define a function isEndString that takes two string arguments string1 and string2:
#     first identify the short and the long string by comparing the lengths of the two strings
#     return True if longString[-len(shortString):] == shortString
#     else return False
# prompt the user for two string inputs
# call the isEndString function and print out whether either of the strings appear at the end of the other

def isEndString(string1, string2):
    '''
    Function takes two strings as arguments and returns True if either of the strings
    appear at the end of the other. Otherwise it returns False. 
    '''
    if len(string1) < len(string2):
        shortString, longString = string1.lower(), string2.lower()
    else:
        shortString, longString = string2.lower(), string1.lower()

    return longString[-len(shortString):] == shortString

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")


if len(word1)>0 and len(word2)>0:
    if isEndString(word1, word2):
        if len(word1) < len(word2):
            print(word1, "appears at the end of", word2)
        else:
            print(word2, "appears at the end of", word1)
    else:
        if len(word1) < len(word2):
            print(word1, "does not appear at the end of", word2)
        else:
            print(word2, "does not appear at the end of", word1)
else:
    print("You entered at least one empty string. Program terminates. ")