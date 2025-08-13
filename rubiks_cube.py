import enum


class Color(enum.Enum):
    WHITE=0
    RED=1
    BLUE=2
    GREEN=3
    YELLOW=4
    ORANGE=5

class rubiks_cube():


    def __init__(self,radius):
        cubes = [[[None for _ in range(radius)] for _ in range(radius)] for _ in range(radius)]

        for x in range(radius):
            for y in range(radius):
                for z in range(radius):
                    print

        print()



class small_cube():

    def __init__(self,color,coordinates):
        self.up = color
        self.coordinates = coordinates  # a vec3 like (x,y,z)

