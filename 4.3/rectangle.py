from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self._name = "Rectangle"
        self._width = width
        self._length = length

    def calculate_area(self):
        self._area = self._width * self._length