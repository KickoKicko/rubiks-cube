from ursina import *
#import time
import copy
import random

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
                    self.cubes[x][y][z]= cube_piece((x-1,y-1,z-1),colors,cube=cube)
        self.rotation_arrow = create_arrows(cube)
    

    def rotate_side(self,side,clockwise,animation):
        match side:
            case 0:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= clockwise,1,1,'y'
                if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:0,1:2,2:3,3:4,4:1,5:5}, (2,1,0), (1,1,-1)
                else: side_mapping, coordinate_indexes, axis_direction = {0:0,1:4,2:1,3:2,4:3,5:5}, (2,1,0),(-1,1,1)
            case 1:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= clockwise,2,-1,'z'
                if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:4,1:1,2:0,3:3,4:5,5:2}, (1,0,2), (1,-1,1)
                else: side_mapping, coordinate_indexes, axis_direction = {0:2,1:1,2:5,3:3,4:0,5:4}, (1,0,2),(-1,1,1)
            case 2:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= not clockwise,0,-1,'x'
                if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:1,1:5,2:2,3:0,4:4,5:3}, (0,2,1), (1,1,-1)
                else: side_mapping, coordinate_indexes, axis_direction = {0:3,1:0,2:2,3:5,4:4,5:1}, (0,2,1),(1,-1,1)
            case 3:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= not clockwise,2,1,'z'
                if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:2,1:1,2:5,3:3,4:0,5:4}, (1,0,2), (-1,1,1)
                else: side_mapping, coordinate_indexes, axis_direction = {0:4,1:1,2:0,3:3,4:5,5:2}, (1,0,2),(1,-1,1)
            case 4:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= clockwise,0,1,'x'
                if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:3,1:0,2:2,3:5,4:4,5:1}, (0,2,1), (1,-1,1)
                else: side_mapping, coordinate_indexes, axis_direction = {0:1,1:5,2:2,3:0,4:4,5:3}, (0,2,1),(1,1,-1)
            case 5:
                clockwise_animation, max_coordinate, max_coordinate_value,axis= not clockwise,1,-1,'y'
                if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:0,1:4,2:1,3:2,4:3,5:5}, (2,1,0), (-1,1,1)
                else: side_mapping, coordinate_indexes, axis_direction = {0:0,1:2,2:3,3:4,4:1,5:5}, (2,1,0),(1,1,-1)
        face = []
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.cubes[x][y][z].coordinates[max_coordinate] == max_coordinate_value:
                        face.append(self.cubes[x][y][z])
        if animation: self.animate_rotation(face,clockwise_animation,axis)
        for x in face:
            x.coordinates = (x.coordinates[coordinate_indexes[0]]*axis_direction[0],x.coordinates[coordinate_indexes[1]]*axis_direction[1],x.coordinates[coordinate_indexes[2]]*axis_direction[2])
            x.rotate_sides(side_mapping,True)

    
    def animate_rotation(self, face, clockwise,axis):
        pivot = Entity()
        for x in face:
            for cubelet in x.entities:
                x.entities[cubelet].parent = pivot
        
        if clockwise: angle = 90
        else: angle = -90
        if axis == 'x':
            pivot.animate_rotation_x(angle, duration=0.15,curve=curve.linear)
        elif axis == 'y':
            pivot.animate_rotation_y(angle, duration=0.15,curve=curve.linear)
        elif axis == 'z':
            pivot.animate_rotation_z(angle, duration=0.15,curve=curve.linear)

        def finalize():
            for x in face:
                for cubelet in x.entities:
                    x.entities[cubelet].world_parent = scene
            destroy(pivot)

        invoke(finalize, delay=0.23)
    
    def solve(self):
        cube_copy= [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube_copy[x][y][z] = cube_piece(self.cubes[x][y][z].coordinates,self.cubes[x][y][z].sides_with_colors)

        moves_queue = []
        self.white_cross(moves_queue,cube_copy)
        self.white_corners(moves_queue,cube_copy)
        self.second_layer(moves_queue,cube_copy)
        self.yellow_cross(moves_queue,cube_copy)
        self.yellow_edges(moves_queue,cube_copy)
        self.play_solution(moves_queue)
    
    def play_solution(self, moves, delay=0.4):
        if not moves:
            return
        move = moves.pop(0)
        self.rotate_side(move[0],move[1],True)
        invoke(self.play_solution, moves, delay=delay)
    
    def white_cross(self,moves_queue,cube_copy):
        if self.cubes[1][2][0].sides_with_colors == {0:color.white,1:color.red} and self.cubes[0][2][1].sides_with_colors == {0:color.white,2:color.green} and self.cubes[1][2][2].sides_with_colors == {0:color.white,3:color.orange} and self.cubes[2][2][1].sides_with_colors == {0:color.white,4:color.blue}:
            return True
        else:
            self.move_white_cross_piece(moves_queue,cube_copy,cube_copy[1][2][0],(0,1,-1))
            self.move_white_cross_piece(moves_queue,cube_copy,cube_copy[0][2][1],(-1,1,0))
            self.move_white_cross_piece(moves_queue,cube_copy,cube_copy[1][2][2],(0,1,1))
            self.move_white_cross_piece(moves_queue,cube_copy,cube_copy[2][2][1],(1,1,0))
            return False
    
    def move_white_cross_piece(self,moves_queue,cube_copy, piece, destination):
        if piece.coordinates == destination and piece.sides_with_colors[0] == color.white:
            return
        if piece.coordinates[1] == 1:
            for side in piece.sides_with_colors:
                if side != 0:
                    solve_rotate(moves_queue,cube_copy,side,True)
                    solve_rotate(moves_queue,cube_copy,side,True)
        elif piece.coordinates[1] == 0:
            if 1 in piece.sides_with_colors and 2 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,2,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,2,False)
            elif 2 in piece.sides_with_colors and 3 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,3,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,3,False)
            elif 3 in piece.sides_with_colors and 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,4,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,4,False)
            elif 1 in piece.sides_with_colors and 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,1,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,1,False)

        # Now the white piece is in the bottom layer

        if piece.coordinates[0] != destination[0] and piece.coordinates[2] != destination[2]:
            if piece.coordinates[0] == destination[2] and piece.coordinates[2] *-1 == destination[0]: solve_rotate(moves_queue,cube_copy,5,True)
            else: solve_rotate(moves_queue,cube_copy,5,False)  
        elif piece.coordinates[0] != destination[0] or piece.coordinates[2] != destination[2]:
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,5,True)
        
        for side in piece.sides_with_colors:
            if side != 5:
                solve_rotate(moves_queue,cube_copy,side,True)
                solve_rotate(moves_queue,cube_copy,side,True)
        
        # Now in the right position

        if piece.sides_with_colors[0] != color.white:
            if 1 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,1,True)
                solve_rotate(moves_queue,cube_copy,0,False)
                solve_rotate(moves_queue,cube_copy,4,True)
                solve_rotate(moves_queue,cube_copy,0,True)
            elif 2 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,2,True)
                solve_rotate(moves_queue,cube_copy,0,False)
                solve_rotate(moves_queue,cube_copy,1,True)
                solve_rotate(moves_queue,cube_copy,0,True)
            elif 3 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,3,True)
                solve_rotate(moves_queue,cube_copy,0,False)
                solve_rotate(moves_queue,cube_copy,2,True)
                solve_rotate(moves_queue,cube_copy,0,True)
            elif 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,4,True)
                solve_rotate(moves_queue,cube_copy,0,False)
                solve_rotate(moves_queue,cube_copy,3,True)
                solve_rotate(moves_queue,cube_copy,0,True)
    
    def white_corners(self,moves_queue,cube_copy):
        print()
        self.move_white_corners_piece(moves_queue,cube_copy,cube_copy[0][2][0],(-1,1,-1))
        self.move_white_corners_piece(moves_queue,cube_copy,cube_copy[0][2][2],(-1,1,1))
        self.move_white_corners_piece(moves_queue,cube_copy,cube_copy[2][2][2],(1,1,1))
        self.move_white_corners_piece(moves_queue,cube_copy,cube_copy[2][2][0],(1,1,-1))


    def move_white_corners_piece(self,moves_queue,cube_copy, piece, destination):
        if piece.coordinates == destination and piece.sides_with_colors[0] == color.white:
            return
        if piece.coordinates[1] == 1:
            if 1 in piece.sides_with_colors and 2 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,2,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,2,False)
            elif 2 in piece.sides_with_colors and 3 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,3,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,3,False)
            elif 3 in piece.sides_with_colors and 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,4,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,4,False)
            elif 1 in piece.sides_with_colors and 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,1,True)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,1,False)
        
        # Now in the bottom layer
            
        if piece.coordinates[0] != destination[0] and piece.coordinates[2] != destination[2]:
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,5,True)
        elif piece.coordinates[0] != destination[0] or piece.coordinates[2] != destination[2]:
            if piece.coordinates[0] == destination[2] and piece.coordinates[2] *-1 == destination[0]: solve_rotate(moves_queue,cube_copy,5,True)
            else: solve_rotate(moves_queue,cube_copy,5,False) 

        # Now in the right corner of the bottom layer
        if 1 in piece.sides_with_colors and 2 in piece.sides_with_colors:right_side=1
        elif 2 in piece.sides_with_colors and 3 in piece.sides_with_colors:right_side=2
        elif 3 in piece.sides_with_colors and 4 in piece.sides_with_colors:right_side=3
        elif 1 in piece.sides_with_colors and 4 in piece.sides_with_colors:right_side=4

        if piece.sides_with_colors[right_side] == color.white:loops = 1
        elif piece.sides_with_colors[5] == color.white:loops =3
        else:loops =5

        for i in range(loops):
            solve_rotate(moves_queue,cube_copy,right_side,False)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,right_side,True)
            solve_rotate(moves_queue,cube_copy,5,True)
        

    def second_layer(self,moves_queue,cube_copy):
        self.move_second_layer_piece(moves_queue,cube_copy,cube_copy[0][1][0],(-1,0,-1))
        self.move_second_layer_piece(moves_queue,cube_copy,cube_copy[0][1][2],(-1,0,1))
        self.move_second_layer_piece(moves_queue,cube_copy,cube_copy[2][1][2],(1,0,1))
        self.move_second_layer_piece(moves_queue,cube_copy,cube_copy[2][1][0],(1,0,-1))

    def move_second_layer_piece(self,moves_queue,cube_copy, piece, destination):
        #if piece.coordinates == destination: # add the return early if already correct here
            #return
        
        if piece.coordinates[1] == 0:
            if 1 in piece.sides_with_colors and 2 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,2,True)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,2,False)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,1,False)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,1,True)
            elif 2 in piece.sides_with_colors and 3 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,3,True)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,3,False)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,2,False)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,2,True)
            elif 3 in piece.sides_with_colors and 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,4,True)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,4,False)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,3,False)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,3,True)
            elif 1 in piece.sides_with_colors and 4 in piece.sides_with_colors:
                solve_rotate(moves_queue,cube_copy,1,True)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,1,False)
                solve_rotate(moves_queue,cube_copy,5,False)
                solve_rotate(moves_queue,cube_copy,4,False)
                solve_rotate(moves_queue,cube_copy,5,True)
                solve_rotate(moves_queue,cube_copy,4,True)
        
        for side in piece.sides_with_colors:
            if side !=5:
                right_color = piece.sides_with_colors[side]
        match right_color:
            case color.red:right_side = 1
            case color.green:right_side = 2
            case color.orange:right_side = 3
            case color.blue:right_side = 4

        while right_side not in piece.sides_with_colors:
            solve_rotate(moves_queue,cube_copy,5,True)
        
        for side in piece.sides_with_colors:
            if side != right_side:
                other_color = piece.sides_with_colors[side]
        match other_color:
            case color.red:other_side = 1
            case color.green:other_side = 2
            case color.orange:other_side = 3
            case color.blue:other_side = 4
        if right_side == 1 and other_side == 4: # Need to implement this "edge case"
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,other_side,False)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,other_side,True)

            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,right_side,True)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,right_side,False)
        elif right_side == 4 and other_side == 1:
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,other_side,True)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,other_side,False)

            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,right_side,False)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,right_side,True)
        elif right_side>other_side:
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,other_side,False)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,other_side,True)

            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,right_side,True)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,right_side,False)
        else:
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,other_side,True)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,other_side,False)

            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,right_side,False)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,right_side,True)


    def yellow_cross(self,moves_queue,cube_copy):
        cubes=[cube_copy[1][0][0],cube_copy[0][0][1],cube_copy[1][0][2],cube_copy[2][0][1]]
        cubes=[cube for cube in cubes if cube.sides_with_colors[5] == color.yellow]
        if len(cubes)==4: # Cross already done
            return
        if len(cubes)==0: # Only one square
            solve_rotate(moves_queue,cube_copy,1,True)
            solve_rotate(moves_queue,cube_copy,2,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,2,False)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,1,False)

            solve_rotate(moves_queue,cube_copy,3,True)
            solve_rotate(moves_queue,cube_copy,4,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,4,False)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,3,False)

            solve_rotate(moves_queue,cube_copy,1,True)
            solve_rotate(moves_queue,cube_copy,2,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,2,False)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,1,False)
        elif cubes[0].coordinates[0] != cubes[1].coordinates[0] and cubes[0].coordinates[2] != cubes[1].coordinates[2]:# L squares
            sides = []
            for cube in cubes:
                for side in cube.sides_with_colors:
                    if side != 5:
                        sides.append(side)
            sides= [opposite_side(x) for x in sides]
            if sides[0]>sides[1] or (sides[0]==1 and sides[1] == 4):
                sides[0],sides[1] = sides[1], sides[0]
            solve_rotate(moves_queue,cube_copy,sides[0],True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,sides[1],True)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,sides[1],False)
            solve_rotate(moves_queue,cube_copy,sides[0],False)
        else: #Line of squares
            for x in cubes[0].sides_with_colors:
                if x != 5:
                    front_side = x
            if front_side == 1: left_side = 4
            else: left_side = front_side-1
            solve_rotate(moves_queue,cube_copy,left_side,True)
            solve_rotate(moves_queue,cube_copy,front_side,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,front_side,False)
            solve_rotate(moves_queue,cube_copy,5,False)
            solve_rotate(moves_queue,cube_copy,left_side,False)

    def yellow_edges(self,moves_queue,cube_copy):
        self.move_yellow_edge_piece(moves_queue,cube_copy,cube_copy[1][0][0],(0,-1,-1))
        self.move_yellow_edge_piece(moves_queue,cube_copy,cube_copy[0][0][1],(-1,-1,0))
        self.move_yellow_edge_piece(moves_queue,cube_copy,cube_copy[1][0][2],(0,-1,1))
        self.move_yellow_edge_piece(moves_queue,cube_copy,cube_copy[2][0][1],(1,-1,0))
    
    def move_yellow_edge_piece(self,moves_queue,cube_copy, piece, destination):
        if piece.coordinates == destination: 
            return
        if piece.coordinates[0] == destination[0] or piece.coordinates[2] == destination[2]: # Across
            for s in piece.sides_with_colors:
                if s != 5: side = s 
            if side == 4: side = 1
            else: side = side+1
            loops=2
        else: # Just one turn
            for s in piece.sides_with_colors:
                if s != 5: side = s 
            if piece.coordinates[0]==destination[2] and piece.coordinates[2]==destination[0]*-1: # Need one clockwise turn
                if side == 4: side = 1
                else: side = side+1
            else:# Need one non-clockwise turn
                if side == 3: side = 1
                elif side == 4: side = 2
                else: side = side+2
            loops = 1
        
        for i in range(loops):
            solve_rotate(moves_queue,cube_copy,side,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,side,False)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,side,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,5,True)
            solve_rotate(moves_queue,cube_copy,side,False)
            solve_rotate(moves_queue,cube_copy,5,True)
            if side == 1: side = 4
            else: side = side-1




    
    def check_solved(self):
        amount = 0
        for x in range(3):
            for y in range(3):
                for z in range(3):
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
                    if self.cubes[x][y][z].sides_with_colors != colors:
                        amount += 1
                        #return False
        if amount != 0:
            print(amount)
            return False
        return True
    
    def shuffle(self, amount):
        list = []
        for i in range(amount):
            list.append((random.randint(0,5),bool(random.randint(0,1))))
        self.play_solution(list)



        



class cube_piece():

    def __init__(self,coordinates,sides_with_colors,cube=None):
        self.coordinates = coordinates  # a vec3 like (x,y,z)
        self.sides_with_colors=sides_with_colors
        self.entities={}
        if cube != None:
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
    
    def rotate_sides(self,rotation_dict,have_entities):
        new_sides_with_colors={}
        if have_entities: new_entities={}
        for x in self.sides_with_colors:
            if x == 0:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                if have_entities: new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==1:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                if have_entities: new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==2:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                if have_entities: new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==3:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                if have_entities: new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==4:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                if have_entities: new_entities[rotation_dict[x]]=self.entities[x]
            elif x ==5:
                new_sides_with_colors[rotation_dict[x]]=self.sides_with_colors[x]
                if have_entities: new_entities[rotation_dict[x]]=self.entities[x]
        
        self.sides_with_colors=new_sides_with_colors.copy()
        if have_entities: self.entities=new_entities.copy()




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


def opposite_side(side):
    match side:
        case 0:
            return 5
        case 1:
            return 3
        case 2:
            return 4
        case 3:
            return 1
        case 4:
            return 2
        case 5:
            return 0
            

def solve_rotate(moves_queue,cube_copy, side, clockwise):
    match side:
        case 0:
            max_coordinate, max_coordinate_value= 1,1
            if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:0,1:2,2:3,3:4,4:1,5:5}, (2,1,0), (1,1,-1)
            else: side_mapping, coordinate_indexes, axis_direction = {0:0,1:4,2:1,3:2,4:3,5:5}, (2,1,0),(-1,1,1)
        case 1:
            max_coordinate, max_coordinate_value= 2,-1
            if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:4,1:1,2:0,3:3,4:5,5:2}, (1,0,2), (1,-1,1)
            else: side_mapping, coordinate_indexes, axis_direction = {0:2,1:1,2:5,3:3,4:0,5:4}, (1,0,2),(-1,1,1)
        case 2:
            max_coordinate, max_coordinate_value= 0,-1
            if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:1,1:5,2:2,3:0,4:4,5:3}, (0,2,1), (1,1,-1)
            else: side_mapping, coordinate_indexes, axis_direction = {0:3,1:0,2:2,3:5,4:4,5:1}, (0,2,1),(1,-1,1)
        case 3:
            max_coordinate, max_coordinate_value= 2,1
            if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:2,1:1,2:5,3:3,4:0,5:4}, (1,0,2), (-1,1,1)
            else: side_mapping, coordinate_indexes, axis_direction = {0:4,1:1,2:0,3:3,4:5,5:2}, (1,0,2),(1,-1,1)
        case 4:
            max_coordinate, max_coordinate_value= 0,1
            if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:3,1:0,2:2,3:5,4:4,5:1}, (0,2,1), (1,-1,1)
            else: side_mapping, coordinate_indexes, axis_direction = {0:1,1:5,2:2,3:0,4:4,5:3}, (0,2,1),(1,1,-1)
        case 5:
            max_coordinate, max_coordinate_value= 1,-1
            if clockwise: side_mapping, coordinate_indexes, axis_direction = {0:0,1:4,2:1,3:2,4:3,5:5}, (2,1,0), (-1,1,1)
            else: side_mapping, coordinate_indexes, axis_direction = {0:0,1:2,2:3,3:4,4:1,5:5}, (2,1,0),(1,1,-1)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if cube_copy[x][y][z].coordinates[max_coordinate] == max_coordinate_value:
                    cube_copy[x][y][z].coordinates = (cube_copy[x][y][z].coordinates[coordinate_indexes[0]]*axis_direction[0],cube_copy[x][y][z].coordinates[coordinate_indexes[1]]*axis_direction[1],cube_copy[x][y][z].coordinates[coordinate_indexes[2]]*axis_direction[2])
                    cube_copy[x][y][z].rotate_sides(side_mapping,False)

    moves_queue.append((side,clockwise))
    