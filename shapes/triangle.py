from shapes import BaseShape


class Triangle(BaseShape):
    def __init__(self, area, perimeter):
        super().__init__(name="Triangle", area=area, angles=3, perimeter=perimeter)
