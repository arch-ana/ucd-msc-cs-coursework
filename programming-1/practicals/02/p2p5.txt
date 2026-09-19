animals = "herd of elephants"
seg0 = animals[2:3]
print("seg0, which is animals[2:3], returns letters from position 2 to 3, 3 not included:", seg0)
seg1 = animals[2:2]
print("seg1, animals[2:2] returns letters from position 2 to 2, 2 not included, hence an empty string:", seg1)
seg2 = animals[3:2]
print("seg2, animals [3:2] returns an empty string because there are no letters starting position 3 and moving to position 2 from left to right:", seg2)
seg3 = animals[:3]
print("seg3, animals[:3] prints all letters up until position 3, 3 not included:", seg3)
seg4 = animals[3:]
print("seg4, animals[3: ] prints all letters from position 3 until the end of the string:", seg4)
seg5 = animals[:]
print("seg5, animals[:] prints the entire word:", seg5)


##Answers
##1
## When x and y are the same, Python outputs an empty string. This is because slicing takes
## letters from position x to position y, y not included. Since x and y are the same, when y
## gets excluded, that excludes x as well. 

##2
## When x is greater than y, Python does not have anything to read from x to y going from left
## to right. So it prints an empty string.

##3
## When x is omitted, we technically remove a lower limit, Python starts from the beginning of
## the string and prints until y, y not included

##4
## When y is omitted, we remove the upper limit, the sliced output starts from x and prints
## up till the end of the string

##5
## When both x and y are omitted, there is no upper or lower limit and the entire string is printed
