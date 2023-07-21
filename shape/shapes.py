from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def compute_area(self):
        return self.height * self.width

    def get_width(self):
        return self.width

    def set_width(self, new_width):
        self.width = new_width

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height


class Square(Shape):

    def __init__(self, edge):
        self.edge = edge

    def compute_area(self):
        return self.edge * self.edge
