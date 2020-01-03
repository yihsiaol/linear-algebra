from math import acos, nan, pi, sqrt

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
        if isinstance(other, Vector):
            # dot product
            return sum(map(lambda x: x[0] * x[1], zip(self.components, other.components)))
        else:
            # scalar multiplication
            return Vector(*map(lambda x: x * other, self.components))

    # find magnitude of the vector instance
    def magnitude(self):
        return sqrt(sum(map(lambda x: x**2, self.components)))

    # normalize the vector instance to a unit vector to find its direction
    def normalize(self):
        if self.magnitude() == 0:
            # normalized zero vector does not exist
            return nan
        else:
            return self * (1 / self.magnitude())

    # find the angle between another vector in radians
    def angle_rad(self, other):
        inner_product = self * other
        magnitude_product = self.magnitude() * other.magnitude()
        if magnitude_product == 0:
            # no angle between a zero vector
            return nan
        else:
            return acos(inner_product / magnitude_product)

    # find the angle between another vector in radians
    def angle_deg(self, other):
        return self.angle_rad(other) * 180 / pi

    # project the vector onto another vector
    def project(self, other):
        unit_other = other.normalize()
        return unit_other * (self * unit_other)

    # find the orthogonal component for the vector from another vector
    def orth_comp(self, other):
        return self - self.project(other)

