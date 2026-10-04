'''
On any given day, a pizza company offers the choice of a certain number of toppings for its pizzas. Depending on the day, it provides a fixed number of 
toppings with its standard pizzas. Write a program that prompts the user (the manager) for the number of possible toppings and the number of toppings offered 
on the standard pizza and calculates the total number of different combinations of toppings. Recall that the number of combinations of k items from n possibilities 
is given by the formula n C k = n!/(k!(n-k)!).

define a function to calcualte factorial
def factorial(x)
    initiate factorial to 1
    for num in range(x)
        factorials value is reset to factorial*(num+1)
    return factorial

ask manager for #toppings as input
ask manager for #toppings-on-a-standard-pizza as input
if both >= 0 do
    total_combinations = factorial(topping)/((factorial(topping-toppings on pizza))*(factorial(toppings on pizza)))
    print total combinations
else:
    print neither of these can be negative

'''
def factorial(x):
    factorial = 1
    for num in range(x):
        factorial *= (num+1)
    return factorial

toppings = int(input("Enter number of toppings: "))
toppings_on_standard_pizza = int(input("Enter number of toppings offered on a standard pizza: "))
if toppings>=0 and toppings_on_standard_pizza>=0:
    combinations = factorial(toppings)//(factorial(toppings-toppings_on_standard_pizza)*factorial(toppings_on_standard_pizza))
    print("Number of combinations possible is:", combinations)
else:
    print("Neither of these can be a negative number. Program terminates. ")