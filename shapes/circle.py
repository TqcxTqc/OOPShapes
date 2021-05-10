from shapes import BaseShape
import math


class Circle(BaseShape):
    def __init__(self, area, perimeter=None):
        self.angles = 0
        self.p = 2 * math.pi * (math.sqrt(area / math.pi)) if perimeter is None else perimeter
        super().__init__(name="Circle", area=area, angles=0, perimeter=self.p)
