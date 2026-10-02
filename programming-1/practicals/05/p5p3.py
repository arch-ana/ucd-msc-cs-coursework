# pseudocode
# prompt the user for a floating-point number 
# read the input to a variable num
# if num<0:
#     print number is negative
# elif num>0:
#     print number is positive
# else:
#     print number is zero
# program finishes

num = float(input("Please enter a number: "))

if num<0:
    print("Number is negative")
elif num>0:
    print("Number is positive")
else:
    print("Number is zero")

print("Program completed")