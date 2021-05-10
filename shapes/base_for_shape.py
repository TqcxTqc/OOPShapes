class BaseShape:
    def __init__(self, name, area, angles, perimeter):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter

    def get_area(self):
        return self.area

    def add_area(self, other_figure):
        if not isinstance(other_figure, BaseShape):
            raise Exception("It's not a figure")
        return self.get_area() + other_figure.get_area()

    def get_angles(self):
        return self.angles

    def get_name(self):
        return self.name
