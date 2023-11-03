class Rectangle:
    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Methods
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        line = '*' * self.width
        shape = ''
        for i in range(self.height):
            shape += f'{line}\n'
        return shape
    
    def get_amount_inside(self, shape):
        return (self.height // shape.height) * (self.width // shape.width)



class Square(Rectangle):
    # Constructor
    def __init__(self, sidelength):
        super().__init__(sidelength, sidelength)

    # Methods
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, sidelength):
        self.width = sidelength
        self.height = sidelength
    
    def set_width(self, sidelength):
        self.width = sidelength
        self.height = sidelength

    def set_height(self, sidelength):
        self.width = sidelength
        self.height = sidelength

# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator