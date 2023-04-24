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



def pause_earth():
    global p_ear
    p_ear = not p_ear
    global e_text
    global e_distance
    global e_follow

    if p_ear == False:
        e_distance = Entity(model = "arrow", color = color.red, position = (1.2, -2.5, 0), scale= (2.5, 4, 4), shader=lit_with_shadows_shader)
        e_text = Text(text = "radius: 6378 km", x = -0.6, y = -0.4, color = color.white)
        e_follow = [None] * 9
        e_follow[0] = Entity(model = "sphere", scale=.08)
        e_follow[0].add_script(SmoothFollow(target=earth, offset=(0,-0.3,0)))
        for i in range(1, 9):
            e_follow[i] = Entity(model = "sphere", scale=.06)
            e_follow[i].add_script(SmoothFollow(target=e_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 9):
            destroy(e_follow[i])
        destroy(e_text)
        destroy(e_distance)

        
def pause_mercury():
    global p_mer
    global m_text
    global m_distance
    global m_follow
    p_mer = not p_mer
    if p_mer == False:
        m_distance = Entity(model = "arrow", color = color.red, position = (0.5, 0, 0), scale= (1, 4, 2), shader=lit_with_shadows_shader)
        m_text = Text(text = "radius: 2439.5 km", x = -1.1, y = -0.4, color = color.white)
        m_follow = [None] * 5
        m_follow[0] = Entity(model = "sphere", scale=.08)
        m_follow[0].add_script(SmoothFollow(target=mercury, offset=(0,-0.3,0)))
        for i in range(1, 5):
            m_follow[i] = Entity(model = "sphere", scale=.06)
            m_follow[i].add_script(SmoothFollow(target=m_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 5):
            destroy(m_follow[i])
        destroy(m_text)
        destroy(m_distance)
    


earth_button = Button(text="Earth", scale=(0.2, 0.05), position=(-0.5, -0.47))
earth_button.on_click = pause_earth

mercury_button = Button(text="Mercury", scale=(0.2, 0.05), position=(-1, -0.47))
mercury_button.on_click =pause_mercury

def pause_venus():
    global p_ven
    p_ven = not p_ven
    global v_text
    global v_distance
    global v_follow
    if p_ven == False:
        v_distance = Entity(model = "arrow", color = color.red, position = (0.8, -1.5, 0), scale= (1.8, 4, 3), shader=lit_with_shadows_shader)
        v_text = Text(text = "radius: 6025 km", x = -0.84, y = -0.4, color = color.white)
        v_follow = [None] * 7
        v_follow[0] = Entity(model = "sphere", scale=.08)
        v_follow[0].add_script(SmoothFollow(target=venus, offset=(0,-0.3,0)))
        for i in range(1, 7):
            v_follow[i] = Entity(model = "sphere", scale=.06)
            v_follow[i].add_script(SmoothFollow(target=v_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 7):
            destroy(v_follow[i])
        destroy(v_text)
        destroy(v_distance)

venus_button = Button(text="Venus", scale=(0.2, 0.05), position=(-0.75, -0.47))
venus_button.on_click = pause_venus


def pause_mars():
    global p_mar
    global mar_text
    global mar_distance
    global mar_follow

    p_mar = not p_mar
    if p_mar == False:
        mar_distance = Entity(model = "arrow", color = color.red, position = (1.8, -3.5, 0), scale= (3.8, 4, 5), shader=lit_with_shadows_shader)
        mar_text = Text(text = "radius: 3396 km", x = -0.35, y = -0.4, color = color.white)
        mar_follow = [None] * 12
        mar_follow[0] = Entity(model = "sphere", scale=.08)
        mar_follow[0].add_script(SmoothFollow(target=mars, offset=(0,-0.3,0)))
        for i in range(1, 12):
            mar_follow[i] = Entity(model = "sphere", scale=.06)
            mar_follow[i].add_script(SmoothFollow(target=mar_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 12):
            destroy(mar_follow[i])
        destroy(mar_text)
        destroy(mar_distance)

mars_button = Button(text="Mars", scale=(0.2, 0.05), position=(-0.25, -0.47))
mars_button.on_click = pause_mars

def pause_jupiter():
    global p_jup
    p_jup = not p_jup
    global j_text
    global j_distance
    global j_follow

    if p_jup == False:
        j_distance = Entity(model = "arrow", color = color.red, position = (6.5, -4.5, 0), scale= (13, 4, 8), shader=lit_with_shadows_shader)
        j_text = Text(text = "radius: 71492 km", x = -0.1, y = -0.4, color = color.white)
        j_follow = [None] * 15
        j_follow[0] = Entity(model = "sphere", scale=.2)
        j_follow[0].add_script(SmoothFollow(target=jupiter, offset=(0,-0.3,0)))
        for i in range(1, 15):
            j_follow[i] = Entity(model = "sphere", scale=.2)
            j_follow[i].add_script(SmoothFollow(target=j_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 15):
            destroy(j_follow[i])
        destroy(j_text)
        destroy(j_distance)

jupiter_button = Button(text="Jupiter", scale=(0.2, 0.05), position=(0, -0.47))
jupiter_button.on_click = pause_jupiter


def pause_saturn():
    global p_sat
    p_sat = not p_sat
    global s_text
    global s_distance
    global s_follow

    if p_sat == False:
        s_distance = Entity(model = "arrow", color = color.red, position = (12.5, -9.5, 0), scale= (25, 10, 12), shader=lit_with_shadows_shader)
        s_text = Text(text = "radius: 60268 km", x = 0.15, y = -0.4, color = color.white)
        s_follow = [None] * 23
        s_follow[0] = Entity(model = "sphere", scale=.4)
        s_follow[0].add_script(SmoothFollow(target=saturn, offset=(0,-0.3,0)))
        for i in range(1, 23):
            s_follow[i] = Entity(model = "sphere", scale=.4)
            s_follow[i].add_script(SmoothFollow(target=s_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 23):
            destroy(s_follow[i])
        destroy(s_text)
        destroy(s_distance)

saturn_button = Button(text="Saturn", scale=(0.2, 0.05), position=(0.25, -0.47))
saturn_button.on_click = pause_saturn


def pause_uranus():
    global p_ura
    p_ura = not p_ura
    global u_text
    global u_distance
    global u_follow
    global u_speed
    
    if p_ura == False:
        u_distance = Entity(model = "arrow", color = color.red, position = (25, -13.5, 0), scale= (50, 16, 40), shader=lit_with_shadows_shader)
        u_speed = Text(text = "velocity:  6.8 km/s", x = 0.40, y = -0.35, color = color.white)
        u_text = Text(text = "radius:  25559 km", x = 0.40, y = -0.4, color = color.white)
        u_follow = [None] * 45
        u_follow[0] = Entity(model = "sphere", scale=.8)
        u_follow[0].add_script(SmoothFollow(target=uranus, offset=(0,-0.3,0)))
        for i in range(1, 45):
            u_follow[i] = Entity(model = "sphere", scale=.8)
            u_follow[i].add_script(SmoothFollow(target=u_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 45):
            destroy(u_follow[i])
        destroy(u_text)
        destroy(u_speed)
        destroy(u_distance)
uranus_button = Button(text="Uranus", scale=(0.2, 0.05), position=(0.5, -0.47))
uranus_button.on_click = pause_uranus

def pause_neptune():
    global p_nep
    p_nep = not p_nep
    global nep_text
    global nep_distance
    global nep_follow
    global nep_speed
    
    if p_nep == False:
        nep_distance = Entity(model = "arrow", color = color.red, position = (40, -23.5, 0), scale= (80, 30, 60), shader=lit_with_shadows_shader)
        nep_speed = Text(text = "velocity:  5.6 km/s", x = 0.65, y = -0.35, color = color.white)
        nep_text = Text(text = "radius: 24764 km", x = 0.65, y = -0.4, color = color.white)
        nep_follow = [None] * 55
        nep_follow[0] = Entity(model = "sphere", scale=0.8)
        nep_follow[0].add_script(SmoothFollow(target=neptune, offset=(0,-0.3,0)))
        for i in range(1, 55):
            nep_follow[i] = Entity(model = "sphere", scale=0.8)
            nep_follow[i].add_script(SmoothFollow(target=nep_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 55):
            destroy(nep_follow[i])
        destroy(nep_text)
        destroy(nep_speed)
        destroy(nep_distance)

neptune_button = Button(text="Neptune", scale=(0.2, 0.05), position=(0.75, -0.47))
neptune_button.on_click = pause_neptune



sun = Entity(model="sphere", texture="sun.jpg", position=(0, 1, 0), scale=1.5, shader=lit_with_shadows_shader)
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
jupiter_orbit = Entity(model='circle', position=(0, -7, 0), scale=33.6, texture="jupiter.jpg", thickness=0.1, rotation_x = 90)
saturn_orbit = Entity(model='circle', position=(0, -11, 0), scale=61.825, texture="saturn color.jpg", thickness=0.1, rotation_x = 90)
uranus_orbit = Entity(model='circle', position=(0, -19, 0), scale=123.775, texture="uranus color.jpg", thickness=0.1, rotation_x = 90)
neptune_orbit = Entity(model='circle', position=(0, -27, 0), scale=194.925, texture="neptune.jpg", thickness=0.1, rotation_x = 90)




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
    
    if not p_mer:
        mercury.rotation_y += 0.07
        mercury_orbit.rotation_y += 0.05
        radius_1=1.2
        mercury.x= np.cos(t)*radius_1 
        mercury.z=np.sin(t)*radius_1

    if not p_ear:
        earth.rotation_y += 0.07
        earth_orbit.rotation_y += 0.05 
        radius_3=2.78
        earth.x= np.cos(b)*radius_3
        earth.z=np.sin(b)*radius_3

    if not p_ven:
        venus_orbit.rotation_y += 0.05
        venus.rotation_y += 0.07
        radius_2=2.16
        venus.x= np.cos(a)*radius_2 
        venus.z=np.sin(a)*radius_2

    if not p_mar:
        mars.rotation_y += 0.07
        mars_orbit.rotation_y += 0.05
        radius_4=4.53
        mars.x= np.cos(c)*radius_4
        mars.z=np.sin(c)*radius_4

    if not p_jup:
        jupiter.rotation_y += 0.07
        jupiter_orbit.rotation_y += 0.05
        radius_5=15.24
        jupiter.x= np.cos(d)*radius_5
        jupiter.z=np.sin(d)*radius_5

    if not p_sat:
        saturn.rotation_y += 0.07
        saturn_orbit.rotation_y += 0.05
        radius_6=29.93
        saturn.x= np.cos(e)*radius_6
        saturn.z=np.sin(e)*radius_6

    if not p_ura:
        uranus.rotation_y += 0.07
        uranus_orbit.rotation_y += 0.05
        radius_7=59.71
        uranus.x= np.cos(f)*radius_7
        uranus.z=np.sin(f)*radius_7

    if not p_nep:
        neptune.rotation_y += 0.07
        neptune_orbit.rotation_y += 0.05
        radius_8=93.17
        neptune.x= np.cos(g)*radius_8
        neptune.z=np.sin(g)*radius_8
    
    sun.rotation_y += 0.1
    angle=np.pi*40/180   
 
   
    
EditorCamera()
txt=Text(text="Orbital velocity and distance from sun in solar system 3D simulator", color=color.white, x = -0.5, y = 0.4)

sky=Sky(texture="space.jpg", doubled_side = True)
t=-np.pi
dx = .01
h = g = h = f = e = d = c = b = a = t
app.run()
