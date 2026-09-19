#student_number is 26129750
#amount before decimal: 261297
#amount after decimal: 50

import math
l = float(input("Please enter a non-negative value for length: "))

area_of_square_with_length_l = l**2 
volume_of_a_cube_with_a_side_l = l**3
area_of_circle_with_radius_l = math.pi*(l**2)
volume_of_sphere_with_radius_l = (4/3)*math.pi*(l**3)
volume_of_cylinder_with_radius_and_side_l = math.pi*(l**2)*l

print("Area of square with a side of length",l,"is:", area_of_square_with_length_l)
print("Volume of a cube with side of length",l,"is:", volume_of_a_cube_with_a_side_l)
print("Area of a circle with a radius of length",l,"is:", area_of_circle_with_radius_l)
print("Volume of a sphere with radius of length",l,"is:", volume_of_sphere_with_radius_l)
print("Volume of a cylinder with a radius and height of length",l,"each is:", volume_of_cylinder_with_radius_and_side_l)
print("Program completed")
