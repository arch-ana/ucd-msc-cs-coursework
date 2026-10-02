# Write a program that uses a while loop to sum the first 5000 integers 
# and prints out the total.

# Pseudocode
# Initiate a variable sum and set it to zero
# sum = 0
# Initiate a variable counter and set it to 1
# counter = 1
# while counter <= 5000:
#     add the next number to the sum by adding counter to the sum
#     sum += counter
#     increment counter by one
#     counter += 1
# print the sum

sum = 0
counter = 1

while counter <= 5000:
    sum += counter
    counter += 1

print("Total is", sum)
print("Program completed")