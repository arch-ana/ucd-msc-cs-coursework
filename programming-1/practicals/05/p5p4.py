# pseudocode
# prompt the user for an integer input 
# read the input into a variable num
# if num<0:
#     print number is negative
# elif num=0:
#     print number is zero
# elif num<=20:
#     print number is greater than 0 and less than or equal to 20
# elif num<=40:
#     print number is greater than 20 and less than or equal to 40
# elif num<=60:
#     print number is greater than 40 and less than or equal to 60
# elif num <= 80:
#     print number is greater than 60 and less than or equal to 80
# elif num <= 100:
#     print number is greater than 80 and less than or equal to 100
# else:
#     print number is greater than 100

# program finishes

num = int(float(input("Enter a number: ")))

if num<0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
elif num <= 20:
    print("Number is greater than 0 and less than or equal to 20")
elif num <= 40:
    print("Number is greater than 20 and less than or equal to 40")
elif num <= 60:
    print("Number is greater than 40 and less than or equal to 60")
elif num <= 80:
    print("Number is greater than 60 and less than or equal to 80")
elif num <= 100:
    print("Number is greater than 80 and less than or equal to 100")
else:
    print("Number is greater than 100")

print("Program completed")

