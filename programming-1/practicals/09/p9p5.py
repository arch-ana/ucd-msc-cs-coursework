'''
On any given day, a pizza company offers the choice of a certain number of toppings for its pizzas. Depending on the day, it provides a fixed number of 
toppings with its standard pizzas. Write a program that prompts the user (the manager) for the number of possible toppings and the number of toppings offered 
on the standard pizza and calculates the total number of different combinations of toppings. Recall that the number of combinations of k items from n possibilities 
is given by the formula n C k = n!/(k!(n-k)!).

ask manager for #toppings as input
ask manager for #toppings-on-a-standard-pizza as input
(to simplify variables, use a, b and c to denote the numberator and denominator terms of a combinations formula)
a, b, c = toppings, toppings on standard pizza, toppings - toppings on standard pizza
initiatiate factorial variables for each to 1

initiate counter to 1
while counter <= a:
    a_fact *= counter
    increment counter
repeat this for terms b and c

if toppings>0 and toppings on standard pizza >=0 do
    print (a_fact//(b_fact*c_fact))
else:
    print neither of these can be negative

'''

toppings = int(input("Enter number of toppings: "))
toppings_on_standard_pizza = int(input("Enter number of toppings offered on a standard pizza: "))

a, b, c = toppings, toppings_on_standard_pizza, toppings - toppings_on_standard_pizza
a_fact, b_fact, c_fact = 1, 1, 1

counter = 1
while counter <= a:
    a_fact *= counter
    counter+= 1

counter = 1
while counter <= b:
    b_fact *= counter
    counter += 1

counter = 1
while counter<=c:
    c_fact *= counter
    counter += 1


if 0 <= toppings_on_standard_pizza <= toppings:
    print("Number of combinations possible is:", a_fact//(b_fact*c_fact))
else:
    print("Invalid numbers. Program terminates. ")