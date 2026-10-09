# Add some extra variables and operations on those variables in the program from the previous question to ensure
# that you understand what is going on and how it works.
# Save this program as p13p5.py.

def f(x):
    '''Function that adds 1 to its argument and prints it out'''
    print('In function f:')
    x += 1
    y = 1
    a = 7
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('a is', a)
    a += y
    b = 3
    return x

x, y, z = 5, 10, 15
a, b = 20, 25

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)
print('b is', b)

z = f(x)
b = f(x) + x

print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)
print('b is', b)