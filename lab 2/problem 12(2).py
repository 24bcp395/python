import math
x_center=0
y_center=0
x1_point=int(input("enter x1 here:"))
x2_point=int(input("enter x2 here:"))
radius=int(input("enter a radius here:"))

distance=math.sqrt(pow(x1_point-x_center,2)+pow(x2_point-x_center,2))
print(distance)

if distance<radius:
    print("inside the circle")
elif distance>radius:
    print("outside the circle")
else:
    print("on the circle")

