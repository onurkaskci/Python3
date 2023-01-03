
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(3)

print(f'Circumference: {round(circle.circumference())}')

# Call the area method
print(f'Area: {round(circle.area())}')
