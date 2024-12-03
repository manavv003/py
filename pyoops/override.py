class Shape:
    def area(self):
        """This method returns the area of a shape. By default, it's 0."""
        return 0

class Square(Shape):
    def __init__(self, length):
        """Initialize the square with a given side length."""
        self.length = length
    
    def area(self):
        """Override the area method to calculate the area of the square."""
        return self.length * self.length

# Example usage:
shape = Shape()  # Create a general shape object
square = Square(5)  # Create a square object with side length 5

# Print the area of the shape (which is 0 by default)
print(f"Area of shape: {shape.area()}")

# Print the area of the square
print(f"Area of square: {square.area()}")
