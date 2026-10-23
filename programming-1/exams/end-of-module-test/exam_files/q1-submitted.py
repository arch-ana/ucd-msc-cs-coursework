
#strip the word of characters we are not concerned with
def clean_word(s):
    valid_word = ""
    for char in s:
        if char.isalpha() or char.isnumeric() or char == "+" or char == "-" or char == "*" or char == "/" or char == "?":
            valid_word += char
    return valid_word

#check if the word is palindrome after using the clean_word function to only evaluate the string that contains desired characters
def palindrome(s):

    word_to_check = clean_word(s)
    left, right = 0, len(word_to_check) -1
    while left<right:
        if word_to_check[left] != word_to_check[right] and (word_to_check[left] != "?" and word_to_check[right] != "?"):
            return False
        else:
            left += 1
            right -= 1

    return True

#prompt user for a string input
user_input = input("Enter a string (empty string to exit): ")

#while user input is not an empty string, check if string is a palindrome
while user_input != "":
    if palindrome(user_input):
        print(user_input, "is a palindrome")
    else:
        print(user_input, "is not a palindrome")

    #while loop conditional reset
    user_input = input("Enter a string (empty string to exit): ")

print("Finished!")