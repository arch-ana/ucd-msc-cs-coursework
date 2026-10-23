# define function code_count that takes a single string argument:
#     return the count of the string 'code' in the argument
# prompt the user for a string input
# call the code_count function and print the result 

def code_count(s):
    '''
    The function takes a string as its argument and returns the number of occurences of the string 'code' in it. 
    '''
    return s.count("code")

user_input = input("Enter word: ")

print(user_input, "has \"code\" in it", code_count(user_input), "times")