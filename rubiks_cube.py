import enum
import copy
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
        self.cubes = [[[None for _ in range(radius)] for _ in range(radius)] for _ in range(radius)]
        for x in range(radius):
            for y in range(radius):
                for z in range(radius):
                    colors= {}
                    if y == 2:
                        colors[0] = color.white
                    if z == 0:
                        colors[1] = color.red
                    if x == 0:
                        colors[2] = color.green
                    if z == 2:
                        colors[3] = color.orange
                    if x == 2:
                        colors[4] = color.blue
                    if y == 0:
                        colors[5] = color.yellow
                    self.cubes[x][y][z]= cube_piece(cube,(x-1,y-1,z-1),colors)
    

    def rotate_side(self,side,clockwise):
        if side == 0:
            face = []
            for x in range(3):
                for y in range(3):
                    for z in range(3):
                        if self.cubes[x][y][z].coordinates[1] == 1:
                            face.append(self.cubes[x][y][z])
            for x in face:
                print(x.coordinates)
                x.coordinates = (x.coordinates[2],x.coordinates[1],x.coordinates[0]*-1)
                x.rotate_sides({0:0,1:2,2:3,3:4,4:1,5:5})

            print("---------------------")
            for x in face:
                print(x.coordinates)
        if side == 2:
            face = [[self.cubes[x][2][z] for x in range(3)] for z in range(3)]
            rotated = [[self.cubes[x][2][z] for x in range(3)] for z in range(3)]
            for x in range(3):
                for z in range(3):
                    print(self.cubes[x][2][z].coordinates)
                    self.cubes[x][2][z].coordinates=(self.cubes[x][2][z].coordinates[2],self.cubes[x][2][z].coordinates[1],self.cubes[x][2][z].coordinates[0]*-1)
                print("\n")
            if clockwise:
                rotation_matrix = [[0,0,1],
                                   [0,1,0],
                                   [-1,0,0]]
            else:
                rotation_matrix =[[0,0,0],
                                  [0,1,0],
                                  [-1,0,0]]
            
            print("--------------")
            for x in range(3):
                for z in range(3):
                    print(self.cubes[x][2][z].coordinates)
                    #self.cubes[x][2][z] = r
                print("\n")
            
            print(face)
        

        """for z in range(3):
            for x in range(3):
                print(self.cubes[x][2][z].coordinates)
                #self.cubes[x][2][z].coordinates = (self.cubes[x][2][z].coordinates[2]*-1,self.cubes[x][2][z].coordinates[1],self.cubes[x][2][z].coordinates[0])
        face = [[self.cubes[x][2][z] for x in range(3)] for z in range(3)]
        print(" ---------")
        # Rotate clockwise
        rotated = list(zip(*face[::-1]))

        # Put back
        for z in range(3):
            for x in range(3):
                self.cubes[x][2][z] = rotated[z][x]
                print(self.cubes[x][2][z].coordinates)"""


        """
            temp_corner_cube_dict=self.cubes[2][2][0].sides_with_colors.copy()
            temp_border_cube_dict=self.cubes[2][2][1].sides_with_colors.copy()
            self.cubes[2][2][0].sides_with_colors[0]= self.cubes[2][2][2].sides_with_colors[0]
            self.cubes[2][2][0].sides_with_colors[1]= self.cubes[2][2][2].sides_with_colors[4]
            self.cubes[2][2][0].sides_with_colors[4]= self.cubes[2][2][2].sides_with_colors[3]

            self.cubes[2][2][1].sides_with_colors[0]= self.cubes[1][2][2].sides_with_colors[0]
            self.cubes[2][2][1].sides_with_colors[4]= self.cubes[1][2][2].sides_with_colors[3]

            self.cubes[2][2][2].sides_with_colors[4]= self.cubes[0][2][2].sides_with_colors[3]
            self.cubes[2][2][2].sides_with_colors[0]= self.cubes[0][2][2].sides_with_colors[0]
            self.cubes[2][2][2].sides_with_colors[3]= self.cubes[0][2][2].sides_with_colors[2]

            self.cubes[1][2][2].sides_with_colors[0]= self.cubes[0][2][1].sides_with_colors[0]
            self.cubes[1][2][2].sides_with_colors[3]= self.cubes[0][2][1].sides_with_colors[2]

            self.cubes[0][2][2].sides_with_colors[0]= self.cubes[0][2][0].sides_with_colors[0]
            self.cubes[0][2][2].sides_with_colors[3]= self.cubes[0][2][0].sides_with_colors[2]
            self.cubes[0][2][2].sides_with_colors[2]= self.cubes[0][2][0].sides_with_colors[1]

            self.cubes[0][2][1].sides_with_colors[0]= self.cubes[1][2][0].sides_with_colors[0]
            self.cubes[0][2][1].sides_with_colors[2]= self.cubes[1][2][0].sides_with_colors[1]

            self.cubes[0][2][0].sides_with_colors[0]= temp_corner_cube_dict[0]
            self.cubes[0][2][0].sides_with_colors[1]= temp_corner_cube_dict[4]
            self.cubes[0][2][0].sides_with_colors[2]= temp_corner_cube_dict[1]

            self.cubes[1][2][0].sides_with_colors[0]= temp_corner_cube_dict[0]
            self.cubes[1][2][0].sides_with_colors[1]= temp_corner_cube_dict[4]"""


        self.update_visuals()
        
    
    def update_visuals(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube = self.cubes[x][y][z]
                    for i in cube.sides_with_colors:
                        #cube.entities[i].position = ()
                        cube.update_entity_position()
                        cube.entities[i].color = cube.sides_with_colors[i]


        



class cube_piece():

    def __init__(self,cube,coordinates,sides_with_colors):
        self.coordinates = coordinates  # a vec3 like (x,y,z)
        self.sides_with_colors=sides_with_colors
        self.entities={}
        for side in sides_with_colors:
            self.entities[side] = create_entity(cube,coordinates,side,sides_with_colors[side])

    
    def update_entity_position(self):
        for side in self.entities:
            match side:
                case 0:
                    self.entities[side].position=(self.coordinates[0]*1.05,1.55,self.coordinates[2]*1.05)
                    self.entities[side].rotation_x=90
                    self.entities[side].rotation_y=0
                case 1:
                    self.entities[side].position=(self.coordinates[0]*1.05,self.coordinates[1]*1.05,-1.55)
                    self.entities[side].rotation_x=0
                    self.entities[side].rotation_y=0
                case 2:
                    self.entities[side].position=(-1.55,self.coordinates[1]*1.05,self.coordinates[2]*1.05)
                    self.entities[side].rotation_x=0
                    self.entities[side].rotation_y=90
                case 3:
                    self.entities[side].position=(self.coordinates[0]*1.05,self.coordinates[1]*1.05,1.55)
                    self.entities[side].rotation_x=0
                    self.entities[side].rotation_y=180
                case 4:
                    self.entities[side].position=(1.55,self.coordinates[1]*1.05,self.coordinates[2]*1.05)
                    self.entities[side].rotation_x=0
                    self.entities[side].rotation_y=-90
                case 5:
                    self.entities[side].position=(self.coordinates[0]*1.05,-1.55,self.coordinates[2]*1.05)
                    self.entities[side].rotation_x=-90
                    self.entities[side].rotation_y=0
    
    def rotate_sides(self,rotation_dict):
        new_sides_with_colors={}
        new_entities={}
        for x in self.sides_with_colors:
            if x == 0:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==1:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==2:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==3:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==4:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==5:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                new_entities[rotation_dict[x]]=self.entities[x]
        
        print(self.sides_with_colors)
        self.sides_with_colors=new_sides_with_colors.copy()
        self.entities=new_entities.copy()
        print(self.sides_with_colors)
        print("     ")




def create_entity(cube,coordinates,side,color):
        match side:
            case 0:
                return Entity(model='quad', color=color, position=(coordinates[0]*1.05,1.55,coordinates[2]*1.05),rotation_x=90, parent=cube)
            case 1:
                return Entity(model='quad', color=color, position=(coordinates[0]*1.05,coordinates[1]*1.05,-1.55),rotation_y=0, parent=cube)
            case 2:
                return Entity(model='quad', color=color, position=(-1.55,coordinates[1]*1.05,coordinates[2]*1.05),rotation_y=90, parent=cube)
            case 3:
                return Entity(model='quad', color=color, position=(coordinates[0]*1.05,coordinates[1]*1.05,1.55),rotation_y=180, parent=cube)
            case 4:
                return Entity(model='quad', color=color, position=(1.55,coordinates[1]*1.05,coordinates[2]*1.05),rotation_y=-90, parent=cube)
            case 5:
                return Entity(model='quad', color=color, position=(coordinates[0]*1.05,-1.55,coordinates[2]*1.05),rotation_x=-90, parent=cube)
            case _:
                print("Entity with no sides")
                return None
