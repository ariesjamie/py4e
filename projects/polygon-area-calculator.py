
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # convert an instance into String type
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width
        #return self.width

    def set_height(self, height):
        self.height = height
        #return self.height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            str_width = "*" * self.width + "\n"
            str_shape = str_width * self.height
            return str_shape

    def get_amount_inside(self, different_shape):
        '''
        input: compare the area of two shapes
        output: area of shape 1 // area of shape 2 - 1
        '''
        num_of_times = Rectangle.get_area(self) // Rectangle.get_area(different_shape)
        return num_of_times

class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
#         self.side = side
#         self.width = side
#         self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

# # shape1 = Rectangle(10, 10)
# # shape2 = Rectangle(4, 2)
# shape3 = Square(10)
# shape3_side = shape3.set_side(11)
# # shape1_area = shape1.get_area()
# # shape2_area = shape2.get_area()
# shape3_area = shape3.get_area()
# # shape1_perimeter = shape1.get_perimeter()
# # shape2_perimeter = shape2.get_perimeter()
# shape3_perimeter = shape3.get_perimeter()
# # shape1_diagonal = shape1.get_diagonal()
# # shape2_diagonal = shape2.get_diagonal()
# shape3_diagonal = shape3.get_diagonal()
# # shape1_picture = shape1.get_picture()
# # shape2_picture = shape2.get_picture()
# shape3_picture = shape3.get_picture()

# # print(shape1)
# # print(shape2)
# print(shape3)
# # print(shape1.get_area())
# # print(shape2.get_area())
# print(shape3.get_area())
# # print(shape1.get_perimeter())
# # print(shape2.get_perimeter())
# print(shape3.get_perimeter())
# # print(shape1.get_diagonal())
# # print(shape2.get_diagonal())
# print(shape3.get_diagonal())
# # print(shape1.get_picture())
# # print(shape2.get_picture())
# print(shape3.get_picture())
# # print(shape1.get_amount_inside(shape3))

# print(shape3.set_side(9))








 








