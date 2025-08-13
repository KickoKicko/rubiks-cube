from ursina import *

app = Ursina()
"""cube = Entity(model='cube',position=(0,0,0),color=color.azure)
cube = Entity(model='cube',position=(1,1,1),color=color.red)
cube = Entity(model='cube',position=(-1,-1,-1),color=color.green)
cube = Entity(model='cube',position=(1,-1,1),color=color.white)
cube = Entity(model='cube',position=(1,1,-1),color=color.pink)
cube = Entity(model='cube',position=(-1,1,1))"""


cube = Entity()

#cube = Entity(model='cube',color=color.red)
size = 1

faces = [
    Entity(model='quad', color=color.red,   position=(0,0, size/2),rotation_y=180, parent=cube),   # front
    #Entity(model='quad', color=color.pink,   position=(1,0, size/2),rotation_y=180, parent=cube),   # front
    Entity(model='quad', color=color.orange,position=(0,0,-size/2), rotation_y=0, parent=cube), # back
    Entity(model='quad', color=color.blue,  position=(-size/2,0,0), rotation_y=90,  parent=cube), # left
    Entity(model='quad', color=color.green, position=( size/2,0,0), rotation_y=-90, parent=cube), # right
    Entity(model='quad', color=color.white, position=(0, size/2,0), rotation_x=90, parent=cube), # top
    Entity(model='quad', color=color.yellow,position=(0,-size/2,0), rotation_x=-90,  parent=cube)  # bottom
]

camera = EditorCamera()  # <-- This gives mouse/scroll movement

app.run()