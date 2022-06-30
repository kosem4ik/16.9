class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y},'\
               f' {self.width}, {self.height}.'

    def get_area(self):
        return self.width * self.height


rect = Rectangle(5, 10, 50, 100)
print(rect)
print(rect.get_area())
