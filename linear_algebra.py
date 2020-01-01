from math import sqrt

class Point:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return 'Point{}'.format(self.coordinates)

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return 'Vector{}'.format(self.components)

    def __add__(self, other):
        return Vector(*map(sum, zip(self.components, other.components)))

    def __sub__(self, other):
        return Vector(*map(lambda x: x[0] - x[1], zip(self.components, other.components)))

    def __mul__(self, other):
        return Vector(*map(lambda x: x * other, self.components))

    def magnitude(self):
        return sqrt(sum(map(lambda x: x**2, self.components)))

    def normalize(self):
        return self * (1 / self.magnitude())

