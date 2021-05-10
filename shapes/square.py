from shapes import BaseShape


class Square(BaseShape):
    def __init__(self, area, perimeter):
        super().__init__(name="Square", area=area, angles=4, perimeter=perimeter)