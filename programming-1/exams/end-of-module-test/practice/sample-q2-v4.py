# Program to prompt for a series of strings and check whether each string or a prefix of the string (to a minimum length) is to be found in a file containing lines of text.
# User is also prompted for file to search through; default is lines.txt.

import os


def searchFile(inputFile, searchString):
    """Checks whether the string searchString is in the file inputFile.

    Assumes inputFile and searchString are of type str.
    Assumes that inputFile exists.
    Prints out all lines in inputFile that contain searchString.
    Returns True if searchString is found in inputFile;
    Returns False otherwise."""

# Open the file for reading.
    inputFileHandle = open(inputFile, "r")

# Assume the string is not there until we find it.
    foundString = False
    
# Search for the searchstring one line at a time...
    for line in inputFileHandle:
        if line.find(searchString) != -1:
# We need print(line[:-1]) to get rid of the trailing newline.
            print(line[:-1])
            foundString = True

# Close the file
    inputFileHandle.close()

    return foundString


minPrefixLength = 5

# Prompt the user for an input file...
inputFile = input("Enter a file to operate on (default is lines.txt): ")

# If no file supplied, use lines.txt
if inputFile == "":
    inputFile = "lines.txt"

# Check that the file is there...
if not os.path.isfile(inputFile):
    print("The file", inputFile, "does not exist in the current directory.")
else:
    searchstring = input("Enter a string to search for (empty string to exit): ")

    while searchstring != "":
        print("Searching for", searchstring, "in", inputFile)
        stringFound = searchFile(inputFile, searchstring)
        
        if not stringFound:
# This line of output was given in the question, so reproducing it here...
            print("Didn't find " + searchstring + ". Now searching for prefixes...")

# Take off the last character.
# Using a new variable to preserve the original searchstring.
            newString = searchstring[:-1]

            while not stringFound and len(newString) >= minPrefixLength:
# This line of output was given in the question, so reproducing it here...
                print("Searching for:", newString, "   length of s:", len(newString), "   minlen:", minPrefixLength)
                stringFound = searchFile(inputFile, newString)

                newString = newString[:-1]

        if stringFound:        
            print("The string", searchstring, "or a prefix of it was found.")
        else:
            print("Neither the search string", searchstring, "nor any of its prefixes of it was found.")

        print()

        searchstring = input("Enter a string to search for (empty string to exit): ")

print("Finished!")
