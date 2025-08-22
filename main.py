from ursina import *
from rubiks_cube import rubiks_cube



def rotate00():
    rubiks.rotate_side(0,False,True)
def rotate01():
    rubiks.rotate_side(0,True,True)
def rotate10():
    rubiks.rotate_side(1,False,True)
def rotate11():
    rubiks.rotate_side(1,True,True)
def rotate20():
    rubiks.rotate_side(2,False,True)
def rotate21():
    rubiks.rotate_side(2,True,True)
def rotate30():
    rubiks.rotate_side(3,False,True)
def rotate31():
    rubiks.rotate_side(3,True,True)
def rotate40():
    rubiks.rotate_side(4,False,True)
def rotate41():
    rubiks.rotate_side(4,True,True)
def rotate50():
    rubiks.rotate_side(5,False,True)
def rotate51():
    rubiks.rotate_side(5,True,True)

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
    if key == "c":
        if rubiks.check_solved():
            print("solved")
        else:
            print("not solved")
    if key == "s":
        rubiks.solve()
    if key == "r":
        rubiks.shuffle(10)


rubiks.rotation_arrow[0].on_click=rotate00
rubiks.rotation_arrow[1].on_click=rotate01
rubiks.rotation_arrow[2].on_click=rotate10
rubiks.rotation_arrow[3].on_click=rotate11
rubiks.rotation_arrow[4].on_click=rotate20
rubiks.rotation_arrow[5].on_click=rotate21
rubiks.rotation_arrow[6].on_click=rotate30
rubiks.rotation_arrow[7].on_click=rotate31
rubiks.rotation_arrow[8].on_click=rotate40
rubiks.rotation_arrow[9].on_click=rotate41
rubiks.rotation_arrow[10].on_click=rotate50
rubiks.rotation_arrow[11].on_click=rotate51


app.run()





