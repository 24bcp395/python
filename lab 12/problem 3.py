import math

class Solid:
    def accept_data(self):
        self.shape = input("Enter shape (cube, sphere, cylinder): ").lower()

        if self.shape == "cube":
            self.side = float(input("Enter side of the cube: "))
        elif self.shape == "sphere":
            self.radius = float(input("Enter radius of the sphere: "))
        elif self.shape == "cylinder":
            self.radius = float(input("Enter radius of the cylinder: "))
            self.height = float(input("Enter height of the cylinder: "))
        else:
            print("Shape not supported.")
            self.shape = None

    def surface_area(self):
        if self.shape == "cube":
            return 6 * self.side ** 2
        elif self.shape == "sphere":
            return 4 * math.pi * self.radius ** 2
        elif self.shape == "cylinder":
            return 2 * math.pi * self.radius * (self.radius + self.height)
        else:
            return 0

    def volume(self):
        if self.shape == "cube":
            return self.side ** 3
        elif self.shape == "sphere":
            return (4/3) * math.pi * self.radius ** 3
        elif self.shape == "cylinder":
            return math.pi * self.radius ** 2 * self.height
        else:
            return 0

#use the class
solid = Solid()
solid.accept_data()

if solid.shape:
    print(f"Surface Area: {solid.surface_area():.2f}")   #.2 mean after point 2 number we seen
    print(f"Volume: {solid.volume():.2f}")
