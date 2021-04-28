# Program to find Area of an Equilateral Triangle
# Computer Programming Tutor,APRIL 28,2021

import math
s = float(input("Input the Length of Side of a Equilateral Triangle: "))

#Calculate the Area
Area =(math.sqrt(3)/4)*(s*s)

# Calculate thePerimeter
Peri =3*s

# Calculate the Semi-Perimeter
Semip =Peri/2

#calculate the Altitude
Altitude = (math.sqrt(3)/2)*s

print("Altitude of Equilateral Triangle = %.2f" %Altitude)
print("\n Area of Equilateral Triangle = %.2f" %Area)
print("Perimeter of Equilateral Triangle = %.2f" %Peri)
print("Semi Perimeter of Equilateral Triangle = %.2f" %Semip)
