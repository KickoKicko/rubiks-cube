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
    

    def rotate_side(self,side,clockwise):
        face = []
        match side:
            case 0:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= clockwise,1,1,'y'
            case 1:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= clockwise,2,-1,'z'
            case 2:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= not clockwise,0,-1,'x'
            case 3:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= not clockwise,2,1,'z'
            case 4:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= clockwise,0,1,'x'
            case 5:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= not clockwise,1,-1,'y'

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.cubes[x][y][z].coordinates[max_coordinate] == max_coordinate_value:
                        face.append(self.cubes[x][y][z])
        self.animate_rotation(face,clockwise_animation,axis)

        match side:
            case 0:
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[2],x.coordinates[1],x.coordinates[0]*-1)
                        x.rotate_sides({0:0,1:2,2:3,3:4,4:1,5:5})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[2]*-1,x.coordinates[1],x.coordinates[0])
                        x.rotate_sides({0:0,1:4,2:1,3:2,4:3,5:5})
            case 1:
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[1],x.coordinates[0]*-1,x.coordinates[2])
                        x.rotate_sides({0:4,1:1,2:0,3:3,4:5,5:2})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[1]*-1,x.coordinates[0],x.coordinates[2])
                        x.rotate_sides({0:2,1:1,2:5,3:3,4:0,5:4})
            case 2:
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2],x.coordinates[1]*-1)
                        x.rotate_sides({0:1,1:5,2:2,3:0,4:4,5:3})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2]*-1,x.coordinates[1])
                        x.rotate_sides({0:3,1:0,2:2,3:5,4:4,5:1})
            case 3:
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[1]*-1,x.coordinates[0],x.coordinates[2])
                        x.rotate_sides({0:2,1:1,2:5,3:3,4:0,5:4})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[1],x.coordinates[0]*-1,x.coordinates[2])
                        x.rotate_sides({0:4,1:1,2:0,3:3,4:5,5:2})
            case 4:
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2]*-1,x.coordinates[1])
                        x.rotate_sides({0:3,1:0,2:2,3:5,4:4,5:1})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[0],x.coordinates[2],x.coordinates[1]*-1)
                        x.rotate_sides({0:1,1:5,2:2,3:0,4:4,5:3})
            case 5:
                if clockwise:
                    for x in face:
                        x.coordinates = (x.coordinates[2]*-1,x.coordinates[1],x.coordinates[0])
                        x.rotate_sides({0:0,1:4,2:1,3:2,4:3,5:5})
                else:
                    for x in face:
                        x.coordinates = (x.coordinates[2],x.coordinates[1],x.coordinates[0]*-1)
                        x.rotate_sides({0:0,1:2,2:3,3:4,4:1,5:5})
        #self.update_visuals()
        
    
    def update_visuals(self):
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube = self.cubes[x][y][z]
                    cube.update_entity_position()
                    for i in cube.sides_with_colors:
                        cube.entities[i].color = cube.sides_with_colors[i]

    
    def animate_rotation(self, face, clockwise,axis):
        pivot = Entity()
        for x in face:
            for cubelet in x.entities:
                x.entities[cubelet].parent = pivot
        
        if clockwise: angle = 90
        else: angle = -90
        if axis == 'x':
            pivot.animate_rotation_x(angle, duration=0.3,curve=curve.linear)
        elif axis == 'y':
            pivot.animate_rotation_y(angle, duration=0.3,curve=curve.linear)
        elif axis == 'z':
            pivot.animate_rotation_z(angle, duration=0.3,curve=curve.linear)

        def finalize():
            for x in face:
                for cubelet in x.entities:
                    x.entities[cubelet].world_parent = scene
            destroy(pivot)

        invoke(finalize, delay=0.33)


        



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
                    self.entities[side].position=(self.coordinates[0]*1.05,1.55*self.coordinates[1],self.coordinates[2]*1.05)
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

