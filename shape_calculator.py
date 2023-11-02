class Rectangle:
    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Methods
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
        line = '*' * self.width
        shape = ''
        for i in range(self.height):
            shape += f'\n{line}'
        return shape
    
    def get_amount_inside(self, shape):
        return (self.height // shape.height) * (self.width // shape.width)



class Square(Rectangle):
    # Constructor
    def __init__(self, sidelength):
        super().__init__(sidelength, sidelength)

    # Methods
    def set_side(self, sidelength):
        self.width = sidelength
        self.height = sidelength
    

# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator