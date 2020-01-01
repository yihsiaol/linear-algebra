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

    # add vectors
    def __add__(self, other):
        return Vector(*map(sum, zip(self.components, other.components)))

    # subtract vectors
    def __sub__(self, other):
        return Vector(*map(lambda x: x[0] - x[1], zip(self.components, other.components)))

    # scalar multiplication
    def __mul__(self, other):
        return Vector(*map(lambda x: x * other, self.components))

    # find magnitude of the vector instance
    def magnitude(self):
        return sqrt(sum(map(lambda x: x**2, self.components)))

    # normalize the vector instance to a unit vector to find its direction
    def normalize(self):
        return self * (1 / self.magnitude())

