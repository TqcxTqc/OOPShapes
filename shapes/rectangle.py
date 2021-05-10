from shapes import BaseShape


class Rectangle(BaseShape):
    def __init__(self, area, perimeter):
        super().__init__(name="Rectangle", area=area, angles=4, perimeter=perimeter)