#student_number is 26129750
#amount before decimal: 261297
#amount after decimal: 50

amount_in_rupees = float(input("Please enter a non-negative amount in Rupees: "))
rupee_euro_conversion = 0.00907941 #as of 18th september on xe.com

print("Conversion rate from Rupees to Euros:",rupee_euro_conversion)
print("Amount in Rupees:",amount_in_rupees)
print("Amount in Euros:",amount_in_rupees*rupee_euro_conversion)
print("Program completed")
