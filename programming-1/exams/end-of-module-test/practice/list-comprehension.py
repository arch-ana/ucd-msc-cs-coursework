list1 = [x**2 for x in range(5)]
list2 = [x for x in range(10) if x%2 == 0]
list3 = [x for x in range(10) if x%2 == 0 or x%3 == 0] 
list4 = [0] * 4
list5 = list1
x = 9
y = x
x += 1
print("x is:", x)
print("y is:", y)
list6 = [x for x in range(10) if x%2 == 0] # same as list 2
print(list1)
print(list2)
print(list3)
print(list4)
print("id of list1:", id(list1))
print("id of list5:", id(list5))
print("id of list2:", id(list2))
print("id of list6:", id(list6))
list1.append(7)
print(list1)
print(list5)
list1 += [100]
print(list1)
print(list5)
a = 5690
b = 5690
print("id of a is", id(a))
print("id of b is", id(b))