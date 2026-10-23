# Pseudocode
# define function hasXyz with a single string argument:
#     initiate counter to 0
#     while counter+2 < len(s): # we need three characters from the current index for us to find an xyz
#         if counter-1 == -1: # if we are evaluating the first character, there is no preceding character
#             if s[counter: counter+3].lower() == "xyz": # we only need to check if we have an xyz (case insensitive)
#                 return True
#             else:
#                 increment counter
#         else: # we have a preceding character and we need to check it
#             if s[counter-1] != "." and s[counter:counter+3].lower() == "xyz":
#                 return True
#             else:
#                 increment counter
#     return False # we have gone through all characters and did not find an xyz not preceded by a period

# prompt user for a string input
# call the hasXyz function and return True if the input contains an occurence of xyz that is not preceded by a period

def hasXyz(s):
    '''
    Function takes a single string argument and returns True if the given string contains an appearance of xyz
    where xyz is not directly preceded by a period ("."). Function is case insensitive. 
    '''
    counter = 0
    while counter+2 < len(s):
        if (counter == 0 or s[counter-1] != ".") and (s[counter:counter+3].lower() == "xyz"):
            return True
        else:
            counter += 1
    return False

user_input = input("Enter a string to check if it contains an instance of xyz that is not preceded by a period (.): ")

if hasXyz(user_input):
    print(user_input, "contains an instance of xyz that is not preceded by a period (\".\")")
else:
    print(user_input, "does not contain an instance of xyz that is not preceded by a period (\".\")")
