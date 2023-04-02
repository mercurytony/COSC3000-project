from ursina import *
import math
import numpy as np
from ursina.shaders import lit_with_shadows_shader 


def update():
    global j
    sun.rotation_y += 0.5
    
    mercury.rotation_y += 0.5
    if j < 4:
        mercury.x  += dx
        mercury.y   -= 0.005
        j += dx
        
    else:
        global t
        global k
        t=t +.01
        k += .01
        radius_1=4
        mercury.x= np.cos(t)*radius_1 + j
        mercury.z=np.sin(t)*radius_1 

app = Ursina()
sun = Entity(model="sphere", texture="sun.jpg",  position=(5, -1, 0), scale=1.5, shader=lit_with_shadows_shader)
mercury = Entity(model="sphere", position=(0, 1, 0), texture="mercury.jpg", scale=.2, shader=lit_with_shadows_shader)
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))
EditorCamera()
txt=Text(text="Gravitational field in solar system 3D simulator", x = -0.3, y = 0.4)
arrow = Entity(model="arrow", color=color.white, shader=lit_with_shadows_shader,  position=(3, 0, 0))
arrow2 = duplicate(arrow,color=color.white, shader=lit_with_shadows_shader,  position=(4, 0, 0))
arrow2.x += 3
arrow2.rotation_y += 180
e = [None] * 50
e[0] = Entity(model="sphere", scale=.1, color=color.green)
e[0].add_script(SmoothFollow(target=mercury, offset = (0, 2, 0)))
for i in range(1, 50):
    e[i] = Entity(model="sphere", scale=.1, color=color.green)
    e[i].add_script(SmoothFollow(target=e[i - 1], offset = (0, 0, 0)))
   

##camera.position=(0,27,0)
##camera.rotation_x=90
sky=Sky(texture="galaxy.jpg")
t=-np.pi
dx = .01
k = 0
j = 0

degree = 90
app.run()
