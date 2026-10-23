def search_string_in_file(s, file):
    fileHandle = open(file, 'r')

    found = False
    for line in fileHandle:
        if s in line:
            found = True
            print(line, end="")

    fileHandle.close()
    return found


import os

fileName = input("Please enter the name of a valid file: ")
searchString = input("Please enter the string you would like to search in the file: ")

if not os.path.isfile(fileName):
    fileName = "lines.txt"

while searchString!= "":

    search_string_in_file(searchString, fileName)

    if not search_string_in_file(searchString, fileName):
        prefix = searchString[:-1]
        print("Didn't find", searchString, "now looking for prefixes")
        while len(prefix) >= 5:
            print("Searching for:", prefix, "length of prefix is:", len(prefix), "minlen: 5")
            search_string_in_file(prefix, fileName)
            if search_string_in_file(prefix, fileName):
                break
            prefix = prefix[:-1]
    else:
        print("")
    
    searchString = input("Please enter the string you would like to search in the file: ")

print("Finished")
# if os.path.isfile(fileName):
#     fileHandle = open(fileName, 'r')
# else:
#     fileName = "lines.txt"
#     fileHandle = open(fileName, 'r')

# found = False
# for line in fileHandle:
#     if searchString in line:
#         found = True
#         print(line[:-1])
# else:
#     fileHandle.close()
#     print("Didn't find", searchString, "now searching for prefixes...")
#     prefix = searchString[:-1]
#     while len(prefix) >= 5:
#         print("Searching for", prefix,"\tlength of s", len(prefix), "\tminlen: 5")
#         fileHandle = open(fileName, "r")
#         for line in fileHandle: 
#             if prefix in line:
#                 found = True
#                 print(line[:-1])
#         if found:
#             break
#         prefix = prefix[:-1]
#         fileHandle.close()        

# if found == True:
#     print("The search string", searchString, "or a prefix of it was found")
# else:
#     print("Neither the search string", searchString, "nor any of its prefixes were found")