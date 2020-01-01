class Point:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return 'Point{}'.format(self.coordinates)

class Vector:
    def __init__(self, *components):
        self.components= components

    def __str__(self):
        return 'Vector{}'.format(self.components)
