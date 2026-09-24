income = float(input("Please enter a non-negative value for an income: "))

# Pseudocode
# if the income negative:
#     print that the amount must be non-negative and exit
# else:
#     print the initial income, tax amounts, total tax and nett income

if income < 0:
    print("Amount of income must be >= 0. Please try again.")
else:
    sixty_of_income = income*(60/(60+40))
    forty_of_income = income*(40/(60+40))
    tax_rate_for_larger_income = 20/100
    tax_rate_for_smaller_income = 40/100

    post_tax_larger_income = sixty_of_income*(1-tax_rate_for_larger_income)
    post_tax_smaller_income = forty_of_income*(1-tax_rate_for_smaller_income)
    post_tax_total_income = post_tax_larger_income+post_tax_smaller_income

    print("Income:", income)
    print("Larger income after dividing income in 60:40:",sixty_of_income)
    print("Tax on larger income: ", sixty_of_income*tax_rate_for_larger_income)
    print("Larger income after taxes:", post_tax_larger_income)
    print("Smaller income after dividing income in 60:40:", forty_of_income)
    print("Tax on smaller income: ", forty_of_income*tax_rate_for_smaller_income)
    print("Smaller income after taxes:", post_tax_smaller_income)
    print("Total tax collected: ", (sixty_of_income*tax_rate_for_larger_income)+(forty_of_income*tax_rate_for_smaller_income))
    print("Total income after taxes:", post_tax_total_income)

print("Program completed")