#student_number is 26129750
#amount before decimal: 261297
#amount after decimal: 50

pi = 3.1415927
l = 261297.50

area_of_square_with_length_l = l**2 
volume_of_a_cube_with_a_side_l = l**3
area_of_circle_with_diameter_l = pi*((l/2)**2)
volume_of_sphere_with_diameter_l = (4/3)*pi*((l/2)**3)
volume_of_cylinder_with_diameter_and_side_l = pi*((l/2)**2)*l

print("Area of square with a side of length",l,"is:", area_of_square_with_length_l)
print("Volume of a cube with side of length",l,"is:", volume_of_a_cube_with_a_side_l)
print("Area of a circle with a diameter of length",l,"is:", area_of_circle_with_diameter_l)
print("Volume of a sphere with diameter of length",l,"is:", volume_of_sphere_with_diameter_l)
print("Volume of a cylinder with a diameter and height of length",l,"each is:", volume_of_cylinder_with_diameter_and_side_l)
print("Program completed")
