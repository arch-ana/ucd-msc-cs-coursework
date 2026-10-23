# Pseudocode
# define function saveOccurences that takes one file name as a string input:
#     open the file to read and save the opened readable file in a variable
#     for line in fileHandle:
#         save the count of each string in respective variables
#     close the file that was open to be read
    
#     open a new text file in write mode and save it to a variable fileHandle
#     write the result of each string count into this text file
#     close the file

# prompt the user to enter the name of a file path

# if file exists:
# run the saveOccurences function with the input as its argument
# else print error message

import os

print(os.getcwd())

def saveOccurences(fileName):
    '''
    Function takes the name of a file as its input, counts the number of certain strings, and writes it into a file called 'results'. 
    '''
    fileHandle = open(fileName, 'r')

    leftAngle, rightAngle, newLine, lowerCaseE, string1, string2 = 0, 0, 0, 0, 0, 0

    for line in fileHandle:
        leftAngle += line.count("<")
        rightAngle += line.count(">")
        newLine += line.count("\n")
        lowerCaseE += line.count("e")
        string1 += line.count("<!--")
        string2 += line.count("-->")

    fileHandle.close()

    fileHandle = open("results.txt", "w")
    
    fileHandle.write("Number of left angles: "+str(leftAngle)+"\n")
    fileHandle.write("Number of right angles: "+str(rightAngle)+"\n")
    fileHandle.write("Number of new lines: "+str(newLine)+"\n")
    fileHandle.write("Number of lower case e: "+str(lowerCaseE)+"\n")
    fileHandle.write("Number of <!-- strings: "+str(string1)+"\n")
    fileHandle.write("Number of --> strings: "+str(string2)+"\n")

    fileHandle.close()

user_input = input("Enter the filename of the page you have saved: ")

if not os.path.isfile(user_input):
    print("File", user_input, "does not exist")
else:
    saveOccurences(user_input)



