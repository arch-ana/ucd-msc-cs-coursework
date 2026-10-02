# Write a program that uses a while loop to sum the integers in the range 
# 1–10000 that are divisble by 3 or by 5 and prints out the total.

# Pseudocode
# Initialize a counter and give it a value of 1
# counter = 1
# initialize a variable sum with the value 0
# sum = 0
# while counter <= 10000:
#     if the counter is divisible by 3:
#         add counter to the sum
#     if the counter is divisible by 5:
#         add counter to the sum
# print the final sum
# program terminates

counter = 1
sum = 0

while counter <= 10000:
    if counter%3 == 0 or counter%5 == 0:
        sum += counter
    counter += 1
print("Sum of all numbers that are divisible by 3 or 5 below 10,000 is", sum)
print("Program completed")
