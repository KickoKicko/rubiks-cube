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
        self.rotation_arrow = create_arrows(cube)
        self.update_cubes_array()
    

    def rotate_side(self,side,clockwise):
        face = []
        match side:
            case 0:
                for x in range(3):
                    for y in range(3):
                        for z in range(3):
                            if self.cubes[x][y][z].coordinates[1] == 1:
                                face.append(self.cubes[x][y][z])
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[2],x.coordinates[1],x.coordinates[0]*-1)
                        x.rotate_sides({0:0,1:2,2:3,3:4,4:1,5:5})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[2]*-1,x.coordinates[1],x.coordinates[0])
                        x.rotate_sides({0:0,1:4,2:1,3:2,4:3,5:5})
            case 1:
                for x in range(3):
                    for y in range(3):
                        for z in range(3):
                            if self.cubes[x][y][z].coordinates[2] == -1:
                                face.append(self.cubes[x][y][z])
                """for x in face:
                    print(str(x.coordinates)+"    "+str(x.sides_with_colors))#+"    "+str(x.entities))"""
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[1],x.coordinates[0]*-1,x.coordinates[2])
                        x.rotate_sides({0:4,1:1,2:0,3:3,4:5,5:2})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[1]*-1,x.coordinates[0],x.coordinates[2])
                        x.rotate_sides({0:2,1:1,2:5,3:3,4:0,5:4})
            case 2:
                for x in range(3):
                    for y in range(3):
                        for z in range(3):
                            if self.cubes[x][y][z].coordinates[0] == -1:
                                face.append(self.cubes[x][y][z])
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2],x.coordinates[1]*-1)
                        x.rotate_sides({0:1,1:5,2:2,3:0,4:4,5:3})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2]*-1,x.coordinates[1])
                        x.rotate_sides({0:3,1:0,2:2,3:5,4:4,5:1})
            case 3:
                for x in range(3):
                    for y in range(3):
                        for z in range(3):
                            if self.cubes[x][y][z].coordinates[2] == 1:
                                face.append(self.cubes[x][y][z])
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[1]*-1,x.coordinates[0],x.coordinates[2])
                        x.rotate_sides({0:2,1:1,2:5,3:3,4:0,5:4})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[1],x.coordinates[0]*-1,x.coordinates[2])
                        x.rotate_sides({0:4,1:1,2:0,3:3,4:5,5:2})
            case 4:
                for x in range(3):
                    for y in range(3):
                        for z in range(3):
                            if self.cubes[x][y][z].coordinates[0] == 1:
                                face.append(self.cubes[x][y][z])
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2]*-1,x.coordinates[1])
                        x.rotate_sides({0:3,1:0,2:2,3:5,4:4,5:1})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2],x.coordinates[1]*-1)
                        x.rotate_sides({0:1,1:5,2:2,3:0,4:4,5:3})
            case 5:
                for x in range(3):
                    for y in range(3):
                        for z in range(3):
                            if self.cubes[x][y][z].coordinates[1] == -1:
                                face.append(self.cubes[x][y][z])
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[2]*-1,x.coordinates[1],x.coordinates[0])
                        x.rotate_sides({0:0,1:4,2:1,3:2,4:3,5:5})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[2],x.coordinates[1],x.coordinates[0]*-1)
                        x.rotate_sides({0:0,1:2,2:3,3:4,4:1,5:5})
        self.update_cubes_array()
        """print("")
        for x in face:
            print(str(x.coordinates)+"    "+str(x.sides_with_colors))#+"    "+str(x.entities))
        print("")"""
        #self.update_cubes_array()
        self.update_visuals()
        
    
    def update_visuals(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube = self.cubes[x][y][z]
                    cube.update_entity_position()
                    for i in cube.sides_with_colors:
                        #cube.entities[i].position = ()
                        cube.entities[i].color = cube.sides_with_colors[i]
    
    def update_cubes_array(self):
        new_cubes = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    piece = self.cubes[x][y][z]
                    cx, cy, cz = piece.coordinates
                    if new_cubes[cx+1][cy+1][cz+1] is not None:
                        print(f"Duplicate at {(cx, cy, cz)}")
                    new_cubes[cx+1][cy+1][cz+1] = piece
        self.cubes = new_cubes
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.cubes[x][y][z].coordinates != (x-1,y-1,z-1):
                        print(str(self.cubes[x][y][z].coordinates)+"           "+str((x,y,z)))


        



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
        
        self.sides_with_colors=new_sides_with_colors.copy()
        self.entities=new_entities.copy()




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


def create_arrows(cube):
    arrow_list = []
    arrow_list.append(Entity(model="arrow", color=color.black, position=(0.9,1.7,0.9), rotation_x=90,rotation_y=-135,parent=cube,collider="box"))    
    arrow_list.append(Entity(model="arrow", color=color.black, position=(-0.9,1.7,-0.9), rotation_x=90,rotation_y=-135,parent=cube,collider="box"))   

    arrow_list.append(Entity(model="arrow", color=color.black, position=(0.9,0.9,-1.7), rotation_z=-135,parent=cube,collider="box"))    
    arrow_list.append(Entity(model="arrow", color=color.black, position=(-0.9,-0.9,-1.7), rotation_z=-135,parent=cube,collider="box"))  

    arrow_list.append(Entity(model="arrow", color=color.black, position=(-1.7,0.9,0.9), rotation_y=-90,rotation_z=45,parent=cube,collider="box"))  
    arrow_list.append(Entity(model="arrow", color=color.black, position=(-1.7,-0.9,-0.9), rotation_y=-90,rotation_z=45,parent=cube,collider="box"))  

    arrow_list.append(Entity(model="arrow", color=color.black, position=(0.9,0.9,1.7), rotation_z=45,parent=cube,collider="box"))    
    arrow_list.append(Entity(model="arrow", color=color.black, position=(-0.9,-0.9,1.7), rotation_z=45,parent=cube,collider="box"))  

    arrow_list.append(Entity(model="arrow", color=color.black, position=(1.7,0.9,0.9), rotation_y=-90,rotation_z=-135,parent=cube,collider="box"))  
    arrow_list.append(Entity(model="arrow", color=color.black, position=(1.7,-0.9,-0.9), rotation_y=-90,rotation_z=-135,parent=cube,collider="box"))  

    arrow_list.append(Entity(model="arrow", color=color.black, position=(0.9,-1.7,0.9), rotation_x=90,rotation_y=45,parent=cube,collider="box"))    
    arrow_list.append(Entity(model="arrow", color=color.black, position=(-0.9,-1.7,-0.9), rotation_x=90,rotation_y=45,parent=cube,collider="box"))

    return arrow_list

