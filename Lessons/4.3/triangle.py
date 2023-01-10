from shape import Shape

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self._name = "Triangle"
        self._width = base
        self._height = height

    def calculate_area(self):
        self._area = self._width * self._height * .5