# Pseudocode
# define a function code_count that takes a single string as its argument:
#     initiate a counter, and code_count to 0s
#     while counter+3 < len(s): #we make sure that from the starting index, there are atleast four letters left for us to check
#         if first two letters are 'co' and next is an alphabet character and the next is e:
#             increase code_count by 1
#             increase counter by 4 #we don't need to check the next three characters if they are already part of 'co#e'
#         else:
#             increment counter by 1
#     return code_count

# prompt user for a string input
# call the code_count function and print the result

def code_count(s):
    '''
    Function takes a string as its argument and returns the number of times
    the string 'co#e' (where # can be any letter from the alphabet) appears in the argument. 
    '''
    counter, code_count = 0, 0
    while counter+3 < len(s):
        if s[counter:counter+2] == "co" and s[counter+2].isalpha() and s[counter+3] == 'e':
            code_count += 1
            counter += 4
        else:
            counter += 1
    return code_count

user_input = input("Enter word: ")

print(user_input, "has \"co*e\" ( where * can be any letter in the alphabet) in it", code_count(user_input), "times")