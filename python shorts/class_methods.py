
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(3)

print(circle.circumference())  # Output: 18.84955592153876

# Call the area method
print(circle.area())  # Output: 28.274333882308138