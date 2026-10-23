# Pseudocode
# import os 
# define function balance brackets that takes a single argument which is the name of the file:
#     open file in read more and assign this to a variable fileHandle
#     initiate variables to keep count of each bracket type and set them to zero
#     for line in fileHandle:
#         for character in line, check the character and increment the relevant variable, return false if any right bracket exceeds the left
#     close file 

#     return true if each bracket type is balanced and false otherwise. 

# prompt user for a file name
# if file name is valid:
#     open file in read mode and assign it to variable fileHandle
#     initiate variables to keep count of each bracket type and set them to zero
#     for line in fileHandle:
#         use the .count method to increment the bracket count variables for each line in the file
#     close file 

#     print each bracket type's count
#     close file

#     call the balanceBrackets functions
#     if true, print appropriate message, if false, print that the brackets are not balanced
# else:
#     print invalid file name 

import os

def balanceBrackets(fileName):

    '''
    Function takes a file name as its argument and returns true if each bracket type in the file is balanced, i.e., every left bracket type has an equivalent right bracket type. 
    The function only checks for equality in number terms, and does not concern with interweaving of different bracket types. 
    Returns true if balanced, returns false otherwise. 
    '''

    fileHandle = open(fileName, 'r')
    leftOpen, rightOpen, leftSquare, rightSquare, leftCurly, rightCurly, leftAngle, rightAngle = 0, 0, 0, 0, 0, 0, 0, 0

    for line in fileHandle:
        for char in line:
            if char == "(":
                leftOpen += 1
            elif char == ")":
                rightOpen += 1
                if rightOpen > leftOpen:
                    fileHandle.close()
                    return False
            elif char == "[":
                leftSquare += 1
            elif char == "]":
                rightSquare += 1
                if rightSquare > leftSquare:
                    fileHandle.close()
                    return False
            elif char == "{":
                leftCurly += 1
            elif char == "}":
                rightCurly += 1
                if rightCurly > leftCurly:
                    fileHandle.close()
                    return False
            elif char == "<":
                leftAngle += 1
            elif char == ">":
                rightAngle += 1
                if rightAngle > leftAngle:
                    fileHandle.close()
                    return False

    fileHandle.close()
    return(leftOpen == rightOpen and leftSquare == rightSquare and leftCurly == rightCurly and leftAngle == rightAngle)

input_file_name = input("Enter the filename of the page you have saved: ")

if os.path.isfile(input_file_name):
    fileHandle = open(input_file_name, 'r')
    LeftOpenBracket, RightOpenBracket, LeftSquareBracket, RightSquareBracket, LeftCurlyBracket, RightCurlyBracket, LeftAngleBracket, RightAngleBracket = 0, 0, 0, 0, 0, 0, 0, 0
    for line in fileHandle:
        LeftOpenBracket += line.count("(")
        RightOpenBracket += line.count(")")
        LeftSquareBracket += line.count("[")
        RightSquareBracket += line.count("]")
        LeftCurlyBracket += line.count("{")
        RightCurlyBracket += line.count("}")
        LeftAngleBracket += line.count("<")
        RightAngleBracket += line.count(">")

    print("Number of (:", LeftOpenBracket)
    print("Number of ):", RightOpenBracket)
    print("Number of [:", LeftSquareBracket)
    print("Number of ]:", RightSquareBracket)
    print("Number of {:", LeftCurlyBracket)
    print("Number of }:", RightCurlyBracket)
    print("Number of <:", LeftAngleBracket)
    print("Number of >:", RightAngleBracket)

    fileHandle.close()

    if balanceBrackets(input_file_name):
        print("The brackets in the file are balanced")
    else:
        print("The brackets in the file are not balanced")
else:
    print("Invalid file name. Program terminates. ")



