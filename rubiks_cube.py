import enum
from ursina import *


"""class Color(enum.Enum):
    #WHITE=0 # UP
    color.white=0 # UP
    RED=1 # FORWARD
    GREED=2 # LEFT
    ORANGE=3 # BACK
    BLUE=4 #RIGHT
    YELLOW=5 #DOWN"""

class rubiks_cube():

    def __init__(self,cube,radius):
        cubes = [[[None for _ in range(radius)] for _ in range(radius)] for _ in range(radius)]
        """for x in range(radius):
            for y in range(radius):
                for z in range(radius):
                    cubes[x][y][z]= cube_piece(cube,(x-1,y-1,z-1),{1:Color.BLUE})
                    print"""

        # All center pieces
        cubes[1][2][1]= cube_piece(cube,(0,1,0),{0:color.white})
        cubes[1][1][0]= cube_piece(cube,(0,0,-1),{1:color.red})
        cubes[0][1][1]= cube_piece(cube,(-1,0,0),{2:color.green})
        cubes[1][1][2]= cube_piece(cube,(0,0,1),{3:color.orange})
        cubes[2][1][1]= cube_piece(cube,(1,0,0),{4:color.blue})
        cubes[1][0][1]= cube_piece(cube,(0,-1,0),{5:color.yellow})


        # All border pieces
        cubes[1][2][0]= cube_piece(cube,(0,1,-1),{0:color.white,1:color.red})
        cubes[0][2][1]= cube_piece(cube,(-1,1,0),{0:color.white,2:color.green})
        cubes[1][2][2]= cube_piece(cube,(0,1,1),{0:color.white,3:color.orange})
        cubes[2][2][1]= cube_piece(cube,(1,1,0),{0:color.white,4:color.blue})


        cubes[1][0][0]= cube_piece(cube,(0,-1,-1),{5:color.yellow,1:color.red})
        cubes[0][0][1]= cube_piece(cube,(-1,-1,0),{5:color.yellow,2:color.green})
        cubes[1][0][2]= cube_piece(cube,(0,-1,1),{5:color.yellow,3:color.orange})
        cubes[2][0][1]= cube_piece(cube,(1,-1,0),{5:color.yellow,4:color.blue})


        cubes[0][1][0]= cube_piece(cube,(-1,0,-1),{2:color.green,1:color.red})
        cubes[0][1][2]= cube_piece(cube,(-1,0,1),{2:color.green,3:color.orange})
        cubes[2][1][2]= cube_piece(cube,(1,0,1),{3:color.orange,4:color.blue})
        cubes[2][1][0]= cube_piece(cube,(1,0,-1),{1:color.red,4:color.blue})


        # All corner pieces
        cubes[2][2][0]= cube_piece(cube,(1,1,-1),{0:color.white,1:color.red,4:color.blue})
        cubes[0][2][0]= cube_piece(cube,(-1,1,-1),{0:color.white,1:color.red,2:color.green})
        cubes[2][2][2]= cube_piece(cube,(1,1,1),{0:color.white,3:color.orange,4:color.blue})
        cubes[0][2][2]= cube_piece(cube,(-1,1,1),{0:color.white,3:color.orange,2:color.green})

        cubes[2][0][0]= cube_piece(cube,(1,-1,-1),{5:color.yellow,1:color.red,4:color.blue})
        cubes[0][0][0]= cube_piece(cube,(-1,-1,-1),{5:color.yellow,1:color.red,2:color.green})
        cubes[2][0][2]= cube_piece(cube,(1,-1,1),{5:color.yellow,3:color.orange,4:color.blue})
        cubes[0][0][2]= cube_piece(cube,(-1,-1,1),{5:color.yellow,3:color.orange,2:color.green})


        



class cube_piece():

    def __init__(self,cube,coordinates,sides_with_colors):
        self.coordinates = coordinates  # a vec3 like (x,y,z)
        self.sides_with_colors=sides_with_colors
        self.entities=[]
        for side in sides_with_colors:
            self.entities.append(create_entity(cube,coordinates,side,sides_with_colors[side]))

"""class center_piece(cube_piece):
    def __init__(self,coordinates,color,size_index):
        self.coordinates = coordinates  # a vec3 like (x,y,z)
        self.color = color
        self.size_index = size_index

class border_piece(cube_piece):
    def __init__(self,coordinates,color,size_index):
        self.coordinates = coordinates  # a vec3 like (x,y,z)
        self.color = color
        self.size_index = size_index

class corner_piece(cube_piece):
    pass"""



def create_entity(cube,coordinates,side,color):
        if side==0:
            Entity(model='quad', color=color, position=(coordinates[0]*1.05,1.55,coordinates[2]*1.05),rotation_x=90, parent=cube)
        elif side==1:
            Entity(model='quad', color=color, position=(coordinates[0]*1.05,coordinates[1]*1.05,-1.55),rotation_y=0, parent=cube)
        elif side==2:
            Entity(model='quad', color=color, position=(-1.55,coordinates[1]*1.05,coordinates[2]*1.05),rotation_y=90, parent=cube)
        elif side==3:
            Entity(model='quad', color=color, position=(coordinates[0]*1.05,coordinates[1]*1.05,1.55),rotation_y=180, parent=cube)
        elif side==4:
            Entity(model='quad', color=color, position=(1.55,coordinates[1]*1.05,coordinates[2]*1.05),rotation_y=-90, parent=cube)
        elif side==5:
            Entity(model='quad', color=color, position=(coordinates[0]*1.05,-1.55,coordinates[2]*1.05),rotation_x=-90, parent=cube)
        else:
            print("Entity with no sides")
            return None
