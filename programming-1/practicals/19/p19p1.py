# Pseudocode
# define a function convertToBase that takes two arguments - a decimal number and a base to which we wish to convert it:
#     initiate an emtpy string called result
#     while the integer division of num by base is >=0:
#         result = str(num%base) + result # concatenate result string with the remainder (but in reverse!)
#         if num//base == 0: # we have reached the stage where integer division is zero
#             break
#         num = num//base # reset num to be num integer divided by base

#     return result as in int

# prompt user to enter a decimal number and a base
# if both are positive, call the convertToBase function and print the result,
# else terminate program

def convertToBase(num, base):
    '''
    Function takes two arguments, a number in base 10 and a base to which we want the number converted to. 
    The function returns the decimal number converted to the required base.  
    '''
    result = ""
    while num > 0:
        result = str(num%base) + result
        num = num//base        
    return result

num = int(input("Enter number in base 10: "))
base = int(input("Enter the base you wish to convert it to: "))

if num>0 and 2 <= base <= 10:
    print(num, "in base", base, "is", convertToBase(num, base))
else:
    print("Either number or base are non-positive. Program terminates. ")