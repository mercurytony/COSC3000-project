from ursina import *
import math
import numpy as np
from ursina.shaders import lit_with_shadows_shader 

app = Ursina()
individual = True
p_mer = True
p_ear = True
p_ven = True
p_mar = True
p_jup = True
p_sat = True
p_ura = True
p_nep = True
p_all = True

def pause_all():
    global p_all
    p_all = not p_all
    
def pause_earth():
    global p_ear
    p_ear = not p_ear

def pause_mercury():
    global p_mer
    p_mer = not p_mer

pall_button = Button(text="Pause all", scale=(0.2, 0.05), position=(1, -0.47))
pall_button.on_click = pause_all

earth_button = Button(text="Pause earth", scale=(0.2, 0.05), position=(-0.5, -0.47))
earth_button.on_click = pause_earth

mercury_button = Button(text="Pause mercury", scale=(0.2, 0.05), position=(-1, -0.47))
mercury_button.on_click =pause_mercury

def pause_venus():
    global p_ven
    p_ven = not p_ven

venus_button = Button(text="Pause venus", scale=(0.2, 0.05), position=(-0.75, -0.47))
venus_button.on_click = pause_venus


def pause_mars():
    global p_mar
    p_mar = not p_mar

mars_button = Button(text="Pause mars", scale=(0.2, 0.05), position=(-0.25, -0.47))
mars_button.on_click = pause_mars

def pause_jupiter():
    global p_jup
    p_jup = not p_jup

jupiter_button = Button(text="Pause jupiter", scale=(0.2, 0.05), position=(0, -0.47))
jupiter_button.on_click = pause_jupiter


def pause_saturn():
    global p_sat
    p_sat = not p_sat

saturn_button = Button(text="Pause saturn", scale=(0.2, 0.05), position=(0.25, -0.47))
saturn_button.on_click = pause_saturn


def pause_uranus():
    global p_ura
    p_ura = not p_ura

uranus_button = Button(text="Pause uranus", scale=(0.2, 0.05), position=(0.5, -0.47))
uranus_button.on_click = pause_uranus

def pause_neptune():
    global p_nep
    p_nep = not p_nep

neptune_button = Button(text="Pause neptune", scale=(0.2, 0.05), position=(0.75, -0.47))
neptune_button.on_click = pause_neptune

sun = Entity(model="sphere", texture="sun.jpg",  position=(0, 1, 0), scale=1.5, shader=lit_with_shadows_shader)
mercury = Entity(model="sphere", position=(0, 1, 0), texture="mercury.jpg", scale=.2, shader=lit_with_shadows_shader)
venus = Entity(model="sphere", position=(0, 1, 0), texture="venus.jpg", scale=.3, shader=lit_with_shadows_shader)
earth = Entity(model="sphere", position=(0, 1, 0), texture="earth.jpg", scale=.4, shader=lit_with_shadows_shader)
mars = Entity(model="sphere", position=(0, 1, 0), texture="mars.jpg", scale=.3, shader=lit_with_shadows_shader)
jupiter = Entity(model="sphere", position=(0, 1, 0), texture="jupiter.jpg", scale=.6, shader=lit_with_shadows_shader)
saturn = Entity(model="sphere", position=(0, 1, 0), texture="saturn.jpg", scale=.5, shader=lit_with_shadows_shader)
uranus = Entity(model="sphere", position=(0, 1, 0), texture="uranus.jpg", scale=.5, shader=lit_with_shadows_shader)
neptune = Entity(model="sphere", position=(0, 1, 0), texture="neptune.jpg", scale=.5, shader=lit_with_shadows_shader)




pivot = Entity()
DirectionalLight(parent=pivot, y=3, z=3, shadows=True, rotation=(45, -45, 45))
mercury_orbit = Entity(model='circle', position=(0, -1, 0), scale=2.5, texture="mercury.jpg",  thickness=0.1, rotation_x = 90)
venus_orbit = Entity(model='circle', position=(0, -2, 0), scale=4.65, texture="venus.jpg", thickness=0.1, rotation_x = 90)
earth_orbit = Entity(model='circle', position=(0, -3, 0), scale=6.45, texture="earth color.png", thickness=0.1, rotation_x = 90)
mars_orbit = Entity(model='circle', position=(0, -4, 0), scale=9.825, texture="mars color.jpg", thickness=0.1, rotation_x = 90)
jupiter_orbit = Entity(model='circle', position=(0, -5, 0), scale=33.6, texture="jupiter.jpg", thickness=0.1, rotation_x = 90)
saturn_orbit = Entity(model='circle', position=(0, -6, 0), scale=61.825, texture="saturn color.jpg", thickness=0.1, rotation_x = 90)
uranus_orbit = Entity(model='circle', position=(0, -7, 0), scale=123.775, texture="uranus color.jpg", thickness=0.1, rotation_x = 90)
neptune_orbit = Entity(model='circle', position=(0, -8, 0), scale=194.925, texture="neptune.jpg", thickness=0.1, rotation_x = 90)




def update():
    global p_mer
    global p_ear

    global t
    global a
    global b
    global c
    global d
    global e
    global f
    global g


        
    t=t +.02
    a=a +.01
    b=b +.009
    c=c +.008
    d=d +.007
    e=e +.006
    f=f  + .005
    g=g  + .004
    
    if not p_mer and not p_all:
        mercury.rotation_y += 0.07
        mercury_orbit.rotation_y += 0.05
        radius_1=1
        mercury.x= np.cos(t)*radius_1 
        mercury.z=np.sin(t)*radius_1

    if not p_ear and not p_all:
        earth.rotation_y += 0.07
        earth_orbit.rotation_y += 0.05 
        radius_3=2.58
        earth.x= np.cos(b)*radius_3
        earth.z=np.sin(b)*radius_3

    if not p_ven and not p_all:
        venus_orbit.rotation_y += 0.05
        venus.rotation_y += 0.07
        radius_2=1.86
        venus.x= np.cos(a)*radius_2 
        venus.z=np.sin(a)*radius_2

    if not p_mar and not p_all:
        mars.rotation_y += 0.07
        mars_orbit.rotation_y += 0.05
        radius_4=3.93
        mars.x= np.cos(c)*radius_4
        mars.z=np.sin(c)*radius_4

    if not p_jup and not p_all:
        jupiter.rotation_y += 0.07
        jupiter_orbit.rotation_y += 0.05
        radius_5=13.44
        jupiter.x= np.cos(d)*radius_5
        jupiter.z=np.sin(d)*radius_5

    if not p_sat and not p_all:
        saturn.rotation_y += 0.07
        saturn_orbit.rotation_y += 0.05
        radius_6=24.73
        saturn.x= np.cos(e)*radius_6
        saturn.z=np.sin(e)*radius_6

    if not p_ura and not p_all:
        uranus.rotation_y += 0.07
        uranus_orbit.rotation_y += 0.05
        radius_7=49.51
        uranus.x= np.cos(f)*radius_7
        uranus.z=np.sin(f)*radius_7

    if not p_nep and not p_all:
        neptune.rotation_y += 0.07
        neptune_orbit.rotation_y += 0.05
        radius_8=77.97
        neptune.x= np.cos(g)*radius_8
        neptune.z=np.sin(g)*radius_8
    
    sun.rotation_y += 0.1
    angle=np.pi*40/180   
 
   
    
EditorCamera()
txt=Text(text="Orbital velocity and distance from sun in solar system 3D simulator", color=color.white, x = -0.3, y = 0.4)

sky=Sky(texture="space.jpg", doubled_side = True)
t=-np.pi
dx = .01
h = g = h = f = e = d = c = b = a = t
app.run()
