import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter")
    
    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.diameter

    def compute_area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius: {self.radius} and diameter: {self.diameter}"
    
    def __add__(self, other_circle):
        new_radius = self.radius + other_circle.radius
        return Circle(radius=new_radius)
    
    def __gt__(self, other_circle):
        return self.radius > other_circle.radius
    
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

# Create a list of circles / Créer une liste de cercles
circles = [Circle(radius=5), Circle(radius=3), Circle(radius=4)]

# English: Sort the circles based on their radius using a lambda function
# French: Trier les cercles en fonction de leur rayon en utilisant une fonction lambda
sorted_circles = sorted(circles, key=lambda circle: circle.radius)

# Print sorted circles / Imprimer les cercles triés
for circle in sorted_circles:
    print(circle)