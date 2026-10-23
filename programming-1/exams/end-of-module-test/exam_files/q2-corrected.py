import os

def file_stats(file_name):
    
    vowels = "aeiouyAEIOUY"

    #running line
    line_num = 0

    #counts
    line_count = 0
    character_count = 0
    vowel_count = 0
    consonant_count = 0
    octal_count = 0
    word_count = 0
    blank_line_count = 0

    ##line-wise max
    max_char_line = 0 
    max_char = 0
    max_vowel_line = 0
    max_vowel = 0
    max_consonant_line = 0
    max_consonant = 0
    max_octal_line = 0
    max_octal = 0
    max_word_line = 0
    max_word = 0

    file_handle = open(file_name, 'r')

    # going by line
    for line in file_handle:
        
        line_num += 1
        line_count += 1

        # blank lines
        if line == "\n":
            blank_line_count += 1

        #words
        words_in_line = 0
        words = line.split()
        word_count += len(words)
        words_in_line += len(words)
        if words_in_line > max_word:
            max_word = words_in_line
            max_word_line = line_num

        ## per line tally
        chars_in_line, vowels_in_line, consonants_in_line, octals_in_line = 0, 0, 0, 0

        # going by character
        for char in line:

            character_count += 1
            chars_in_line += 1

            #if char in the alphabet
            if char.isalpha():
                #vowels
                if char in vowels:
                    vowel_count += 1
                    vowels_in_line += 1
                else:
                    consonant_count += 1
                    consonants_in_line += 1
            
            if char.isnumeric():
                if 0 <= int(char) < 8:
                    octal_count += 1
                    octals_in_line += 1

        if chars_in_line > max_char:
            max_char = chars_in_line
            max_char_line = line_num
        if vowels_in_line > max_vowel:
            max_vowel = vowels_in_line
            max_vowel_line = line_num
        if consonants_in_line > max_consonant:
            max_consonant = consonants_in_line
            max_consonant_line = line_num
        if octals_in_line > max_octal:
            max_octal = octals_in_line
            max_octal_line = line_num
        if words_in_line > max_word:
            max_word = words_in_line
            max_word_line = line_num

    print("Processing file ", file_name, ".", sep="")
    print("Statistics for file ", file_name, ":", sep="")
    print("Total number of characters:", character_count)
    print("Total number of vowels:", vowel_count)
    print("Total number of consonants:", consonant_count)
    print("Total number of octal digits:", octal_count)
    print("Total number of words:", word_count)
    print("Total number of blank lines:", blank_line_count)
    print("Total number of lines:", line_count)
    print("")

    print("Maximum number of characters on a line:", max_char)
    if max_char > 0:
        print("This was (or the first occurence of it was) on Line", max_char_line)
    print("")

    print("Maximum number of vowels on a line:", max_vowel)
    if max_vowel > 0:
        print("This was (or the first occurence of it was) on Line", max_vowel_line)
    print("")
    
    print("Maximum number of consonants on a line:", max_consonant)
    if max_consonant > 0:
        print("This was (or the first occurence of it was) on Line", max_consonant_line)
    print("")

    print("Maximum number of octal digits on a line:", max_octal)
    if max_octal>0:    
        print("This was (or the first occurence of it was) on Line", max_octal_line)
    print("")

    print("Maximum number of words on a line:", max_word)
    if max_word>0:
        print("This was (or the first occurence of it was) on Line", max_word_line)
    print("")    

    file_handle.close()

def string_in_file(s, file_name):
    
    file_handle = open(file_name, 'r')

    line_nums = []
    curr_line = 0

    for line in file_handle:
        curr_line += 1
        if line.find(s) != -1:
            line_nums.append(curr_line)

    file_handle.close()

    return line_nums

input_file = input("Enter a file name: ")


while input_file != "":

    # ask for string to search
    input_string = input("Enter a string to search for: ")

    #checking if file exists
    if os.path.isfile(input_file):

        #if yes, call stats function
        file_stats(input_file)

        # if string entered
        if input_string != "":
            res = string_in_file(input_string, input_file)
            
            if len(res) != 0:
                print("The string '", input_string, "' was found on the following line(s):", sep="")
                for i in res:
                    print(i, end=" ")
                print("")
            else:
                print("The string '", input_string, "' was not found", sep="")
        
        #if no string entered
        else:
            print("No search string was supplied")

    #if file does not exist    
    else:
        print("File does not exist!")
    
    print("\n*****")

    # while loop condition reset
    input_file = input("Enter a file name: ")

print("Finished!")

    

    

