from ursina import *
from rubiks_cube import rubiks_cube

app = Ursina()

cube = Entity()

"""cube = Entity()
faces = [
    [
    Entity(model='quad', color=color.red, position=(0,0, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(1.05,0, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(0,1.05, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(1.05,1.05, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(-1.05,-1.05, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(-1.05,0, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(0,-1.05, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(1.05,-1.05, 1.55),rotation_y=180, parent=cube),
    Entity(model='quad', color=color.red, position=(-1.05,1.05, 1.55),rotation_y=180, parent=cube),

    Entity(model='quad', color=color.black, position=(0, 0.525, 1.55),scale_y=0.05,scale_x=3.1,rotation_y=180, parent=cube),
    Entity(model='quad', color=color.black, position=(0, -0.525, 1.55),scale_y=0.05,scale_x=3.1,rotation_y=180, parent=cube),
    Entity(model='quad', color=color.black, position=(0.525, 0, 1.55),scale_y=3.1,scale_x=0.05,rotation_y=180, parent=cube),
    Entity(model='quad', color=color.black, position=(-0.525, 0, 1.55),scale_y=3.1,scale_x=0.05,rotation_y=180, parent=cube)],


    [
    Entity(model='quad', color=color.orange, position=(0,0,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(1.05,0,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(0,1.05,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(1.05,1.05,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(-1.05,0,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(0,-1.05,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(-1.05,-1.05,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(-1.05,1.05,-1.55), rotation_y=0, parent=cube),
    Entity(model='quad', color=color.orange, position=(1.05,-1.05,-1.55), rotation_y=0, parent=cube),

    Entity(model='quad', color=color.black, position=(0, 0.525, -1.55),scale_y=0.05,scale_x=3.1,rotation_y=0, parent=cube),
    Entity(model='quad', color=color.black, position=(0, -0.525, -1.55),scale_y=0.05,scale_x=3.1,rotation_y=0, parent=cube),
    Entity(model='quad', color=color.black, position=(0.525, 0, -1.55),scale_y=3.1,scale_x=0.05,rotation_y=0, parent=cube),
    Entity(model='quad', color=color.black, position=(-0.525, 0, -1.55),scale_y=3.1,scale_x=0.05,rotation_y=0, parent=cube)],


    [
    Entity(model='quad', color=color.blue, position=(-1.55,0,0), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,1.05,0), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,0,1.05), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,1.05,1.05), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,-1.05,0), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,0,-1.05), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,-1.05,-1.05), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,1.05,-1.05), rotation_y=90,  parent=cube),
    Entity(model='quad', color=color.blue, position=(-1.55,-1.05,1.05), rotation_y=90,  parent=cube),

    Entity(model='quad', color=color.black, position=(-1.55, 0.525, 0),scale_y=0.05,scale_x=3.1,rotation_y=90, parent=cube),
    Entity(model='quad', color=color.black, position=(-1.55, -0.525, 0),scale_y=0.05,scale_x=3.1,rotation_y=90, parent=cube),
    Entity(model='quad', color=color.black, position=(-1.55, 0, 0.525),scale_y=3.1,scale_x=0.05,rotation_y=90, parent=cube),
    Entity(model='quad', color=color.black, position=(-1.55, 0, -0.525),scale_y=3.1,scale_x=0.05,rotation_y=90, parent=cube)],


    [
    Entity(model='quad', color=color.green, position=( 1.55,0,0), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,1.05,0), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,0,1.05), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,1.05,1.05), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,-1.05,0), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,0,-1.05), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,-1.05,-1.05), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,1.05,-1.05), rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.green, position=( 1.55,-1.05,1.05), rotation_y=-90, parent=cube),

    Entity(model='quad', color=color.black, position=(1.55, 0.525, 0),scale_y=0.05,scale_x=3.1,rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.black, position=(1.55, -0.525, 0),scale_y=0.05,scale_x=3.1,rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.black, position=(1.55, 0, 0.525),scale_y=3.1,scale_x=0.05,rotation_y=-90, parent=cube),
    Entity(model='quad', color=color.black, position=(1.55, 0, -0.525),scale_y=3.1,scale_x=0.05,rotation_y=-90, parent=cube)],


    [
    Entity(model='quad', color=color.white, position=(0, 1.55,0), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(1.05, 1.55,0), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(0, 1.55,1.05), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(1.05, 1.55,1.05), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(-1.05, 1.55,0), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(0, 1.55,-1.05), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(-1.05, 1.55,-1.05), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(1.05, 1.55,-1.05), rotation_x=90, parent=cube),
    Entity(model='quad', color=color.white, position=(-1.05, 1.55,1.05), rotation_x=90, parent=cube),

    Entity(model='quad', color=color.black, position=(0, 1.55, 0.525),scale_y=0.05,scale_x=3.1,rotation_x=90, parent=cube),
    Entity(model='quad', color=color.black, position=(0, 1.55, -0.525),scale_y=0.05,scale_x=3.1,rotation_x=90, parent=cube),
    Entity(model='quad', color=color.black, position=(0.525, 1.55, 0),scale_y=3.1,scale_x=0.05,rotation_x=90, parent=cube),
    Entity(model='quad', color=color.black, position=(-0.525, 1.55, 0),scale_y=3.1,scale_x=0.05,rotation_x=90, parent=cube)],


    [
    Entity(model='quad', color=color.yellow, position=(0,-1.55,0), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(1.05,-1.55,0), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(0,-1.55,1.05), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(1.05,-1.55,1.05), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(-1.05,-1.55,0), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(0,-1.55,-1.05), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(-1.05,-1.55,-1.05), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(1.05,-1.55,-1.05), rotation_x=-90,  parent=cube),
    Entity(model='quad', color=color.yellow, position=(-1.05,-1.55,1.05), rotation_x=-90,  parent=cube),

    Entity(model='quad', color=color.black, position=(0, -1.55, 0.525),scale_y=0.05,scale_x=3.1,rotation_x=-90, parent=cube),
    Entity(model='quad', color=color.black, position=(0, -1.55, -0.525),scale_y=0.05,scale_x=3.1,rotation_x=-90, parent=cube),
    Entity(model='quad', color=color.black, position=(0.525, -1.55, 0),scale_y=3.1,scale_x=0.05,rotation_x=-90, parent=cube),
    Entity(model='quad', color=color.black, position=(-0.525, -1.55, 0),scale_y=3.1,scale_x=0.05,rotation_x=-90, parent=cube)]

]
print(len(faces))"""

rubiks = rubiks_cube(cube,3)
camera = EditorCamera()  # <-- This gives mouse/scroll movement

def input(key):
    if key == 'space':
        print("Space pressed")
    if key == 'q':
        quit()
    if key == "r":
        rubiks.rotate_side(0,True)



app.run()

