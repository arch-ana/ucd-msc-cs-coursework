def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

a = factorial(10)
b = factorial(1)
c = factorial(0)
d = factorial(5)
print(a)
print(b)
print(c)
print(d)