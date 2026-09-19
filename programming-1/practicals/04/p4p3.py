#student_number: 26129750
#amount before decimal: 261297
#amount after decimal: 50

amount = float(input("Please enter a non-negative value for an amount: "))
sixty_of_amount = amount*(60/(60+40))
forty_of_amount = amount*(40/(60+40))
tax_rate_for_larger_amount = 13.5/100
tax_rate_for_smaller_amount = 23/100

post_tax_larger_amount = sixty_of_amount*(1+tax_rate_for_larger_amount)
post_tax_smaller_amount = forty_of_amount*(1+tax_rate_for_smaller_amount)
post_tax_total_amount = post_tax_larger_amount+post_tax_smaller_amount

print("Amount:", amount)
print("Larger amount after dividing amount in 60:40:",sixty_of_amount)
print("Smaller amount after dividing amount in 60:40:", forty_of_amount)
print("Larger amount after taxes:", post_tax_larger_amount)
print("Smaller amount after taxes:", post_tax_smaller_amount)
print("Total amount after taxes:", post_tax_total_amount)
print("Program completed")