# pseudocode
# ask for input from user for the name of a city
# read the input from the user and store it in a variable town_or_city
# if the town_or_city is belfast, derry or lisburn
#   print that it is in Ulster
# elif the town_or_city is cork, limerick or waterford
#   print city is in munster
# elif the town_or_city is dublin or kilkenny
#   print city is in leinster
# elif the town_or_city is galway or sligo
#   print city is in connacht
# else 
#   print sorry, i dont recognise the name
# program completed

# ulster = ["Belfast", "Derry", "Lisburn"]
# munster = ["Cork", "Limerick", "Waterford"]
# leinster = ["Dublin", "Kilkenny"]
# connacht = ["Galway", "Sligo"]

ulster = "is in Ulster"
munster = "is in Munster"
leinster = "is in Leinster"
connacht = "is in Connacht"

town_or_city = input("Enter the name of a city/town: ")

if town_or_city == "Belfast" or town_or_city == "Derry" or town_or_city == "Lisburn":
    print("You entered", town_or_city+".", town_or_city, ulster)
elif town_or_city == "Cork" or town_or_city == "Limerick" or town_or_city == "Waterford":
    print("You entered", town_or_city+".", town_or_city, munster)
elif town_or_city == "Dublin" or town_or_city == "Kilkenny":
    print("You entered", town_or_city+".", town_or_city, leinster)
elif town_or_city == "Galway" or town_or_city == "Sligo":
    print("You entered", town_or_city+".", town_or_city, connacht)
else:
    print("Sorry, I don't recognise that name")

print("Program completed")




