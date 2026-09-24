
amount_in_rupees = float(input("Please enter a non-negative amount in Rupees: "))

# Pseudocode
# if amount_in_rupees is negative:
#     print that the amount must be non-negative and exit
# else:
#     print the amount in the foreign currency after conversion and any 
#     additional information

if amount_in_rupees<0:
    print("Amount must be >= 0. Please try again")
else:
    rupee_euro_conversion = 0.00916576 #as of 24th september on xe.com
    print("Amount in Rupees:",amount_in_rupees)
    print("Conversion rate from Rupees to Euros:",rupee_euro_conversion)
    print("Amount in Euros:",amount_in_rupees*rupee_euro_conversion)

print("Program completed")

# Example of experimentation with indentation
# When the indentation before the print statement within the if-block is skipped, 
# the interpreter generates the following error message:
# File "C:\Users\Asus\OneDrive - University College Dublin\trimester-1\programming-1\practicals\05\p4-5p1.py", line 12
#     print("Amount must be >= 0. Please try again")
#     ^
# IndentationError: expected an indented block after 'if' statement on line 11
