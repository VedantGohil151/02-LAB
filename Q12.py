import math
x_center = int(input("Enter x of circle center: "))
y_center = int(input("Enter y of circle center: "))
radius = int(input("Enter radius: "))
x = int(input("Enter x of point: "))
y = int(input("Enter y of point: "))

distance = math.sqrt((x - x_center)**2 + (y - y_center)**2)
if distance < radius:
    print("Point is inside the circle")
elif distance == radius:
    print("Point is on the circle")
else:
    print("Point is outside the circle")
