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

e_dist = True
e_speed = True

enable_all = True


ear_speed = None
ven_speed = None
martxt_speed = None
juptxt_speed = None
mer_speed = None
neptxt_speed = None
sattxt_speed = None
uratxt_speed = None

e_text = None
m_text = None
v_text = None
mar_text = None
jup_text = None
nep_text = None
sat_text = None
ura_text = None

def hide_buttons():
    global enable_all
    global ear_speed
    global ven_speed
    global martxt_speed
    global juptxt_speed
    global mer_speed
    global neptxt_speed
    global sattxt_speed
    global uratxt_speed

    global e_text
    global m_text
    global v_text
    global mar_text
    global jup_text
    global nep_text
    global sat_text
    global ura_text
  
    
    enable_all = not enable_all
    if enable_all == False:
        if ear_speed:
            destroy(ear_speed)
        if ven_speed:
            destroy(ven_speed)
        if martxt_speed:
            destroy(martxt_speed)
        if juptxt_speed:
            destroy(juptxt_speed)
        if neptxt_speed:
            destroy(neptxt_speed)
        if mer_speed:
            destroy(mer_speed)
        if sattxt_speed:
            destroy(sattxt_speed)
        if uratxt_speed:
            destroy(uratxt_speed)

        if e_text:
            destroy(e_text)
        if m_text:
            destroy(m_text)
        if v_text:
            destroy(v_text)
        if mar_text:
            destroy(mar_text)
        if jup_text:
            destroy(jup_text)
        if nep_text:
            destroy(nep_text)
        if sat_text:
            destroy(sat_text)
        if ura_text:
            destroy(ura_text)

        earth_button.enabled = False
        mars_button.enabled = False
        venus_button.enabled = False
        jupiter_button.enabled = False
        uranus_button.enabled = False
        mercury_button.enabled = False
        saturn_button.enabled = False
        neptune_button.enabled = False
        earthDist_button.enabled = False
        marsDist_button.enabled = False
        venusDist_button.enabled = False
        jupiterDist_button.enabled = False
        uranusDist_button.enabled = False
        mercuryDist_button.enabled = False
        saturnDist_button.enabled = False
        neptuneDist_button.enabled = False

        earthSpeed_button.enabled = False
        marsSpeed_button.enabled = False
        venusSpeed_button.enabled = False
        jupiterSpeed_button.enabled = False
        uranusSpeed_button.enabled = False
        mercurySpeed_button.enabled = False
        saturnSpeed_button.enabled = False
        neptuneSpeed_button.enabled = False
    else:
        earth_button.enabled = True
        mars_button.enabled = True
        venus_button.enabled = True
        jupiter_button.enabled = True
        uranus_button.enabled = True
        mercury_button.enabled = True
        saturn_button.enabled = True
        neptune_button.enabled = True

        earthDist_button.enabled = True
        marsDist_button.enabled = True
        venusDist_button.enabled = True
        jupiterDist_button.enabled = True
        uranusDist_button.enabled = True
        mercuryDist_button.enabled = True
        saturnDist_button.enabled = True
        neptuneDist_button.enabled = True

        earthSpeed_button.enabled = True
        marsSpeed_button.enabled = True
        venusSpeed_button.enabled = True
        jupiterSpeed_button.enabled = True
        uranusSpeed_button.enabled = True
        mercurySpeed_button.enabled = True
        saturnSpeed_button.enabled = True
        neptuneSpeed_button.enabled = True

def earth_speed():
    global ear_speed
    global e_speed
    global e_dist
    global e_follow
    
    e_speed = not e_speed
    
    
    if e_speed == False:
        ear_speed = Text(text = "29.8 km/s", x = -0.55, y = -0.29, color = color.white)
        e_follow = [None] * 9
        e_follow[0] = Entity(model = "sphere", scale=.08)
        e_follow[0].add_script(SmoothFollow(target=earth, offset=(0,-0.3,0)))
        for i in range(1, 9):
            e_follow[i] = Entity(model = "sphere", scale=.06)
            e_follow[i].add_script(SmoothFollow(target=e_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 9):
            destroy(e_follow[i])
        destroy(ear_speed)

def earth_distance():
    global e_dist
    global e_text
    global e_distance
    e_dist = not e_dist
    if e_dist == False:
        e_distance = Entity(model = "arrow", color = color.red, position = (1.9, -2.5, 0), scale= (1.8, 4, 4), shader=lit_with_shadows_shader)
        e_text = Text(text = "149.6 km (e6)", x = -0.6, y = -0.4, color = color.white)
    else:
        destroy(e_text)
        destroy(e_distance)

def pause_earth():
    global p_ear
    p_ear = not p_ear


m_dist = True
m_speed = True


def mercury_speed():
    global m_speed
    global m_dist
    global m_follow
    global mer_speed
    m_speed = not m_speed
    
    
    if m_speed == False:
        mer_speed = Text(text = "47.4 km/s", x = -1.05, y = -0.29, color = color.white)
        m_follow = [None] * 5
        m_follow[0] = Entity(model = "sphere", scale=.08)
        m_follow[0].add_script(SmoothFollow(target=mercury, offset=(0,-0.3,0)))
        for i in range(1, 5):
            m_follow[i] = Entity(model = "sphere", scale=.06)
            m_follow[i].add_script(SmoothFollow(target=m_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 5):
            destroy(m_follow[i])
        destroy(mer_speed)
        



def mercury_distance():
    global m_dist
    global m_text
    global m_distance
    m_dist = not m_dist
    if m_dist == False:
        m_distance = Entity(model = "arrow", color = color.red, position = (1, 0, 0), scale= (0.3, 2, 2), shader=lit_with_shadows_shader)
        m_text = Text(text = "57.9 km (e6)", x = -1.1, y = -0.4, color = color.white)
    else:
        destroy(m_text)
        destroy(m_distance)
        
def pause_mercury():
    global p_mer

    p_mer = not p_mer
    
    

hide_button = Button(text="Hide options", scale=(0.2, 0.05), position=(1, -0.47))
hide_button.on_click = hide_buttons

earth_button = Button(text="Earth", scale=(0.2, 0.05), position=(-0.5, -0.47))
earth_button.on_click = pause_earth

earthDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(-0.5, -0.35))
earthDist_button.on_click = earth_distance

earthSpeed_button = Button(text="Earth Velocity", scale=(0.2, 0.05), position=(-0.5, -0.25))
earthSpeed_button.on_click = earth_speed

mercury_button = Button(text="Mercury", scale=(0.2, 0.05), position=(-1, -0.47))
mercury_button.on_click =pause_mercury

mercuryDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(-1, -0.35))
mercuryDist_button.on_click = mercury_distance

mercurySpeed_button = Button(text="Mercury Velocity", scale=(0.2, 0.05), position=(-1, -0.25))
mercurySpeed_button.on_click = mercury_speed

v_dist = True
v_speed = True

def venus_speed():
    global v_speed
    global v_dist
    global v_follow
    global ven_speed
    v_speed = not v_speed
    
    
    if v_speed == False:
        ven_speed = Text(text = "35 km/s", x = -0.8, y = -0.29, color = color.white)
        v_follow = [None] * 7
        v_follow[0] = Entity(model = "sphere", scale=.08)
        v_follow[0].add_script(SmoothFollow(target=venus, offset=(0,-0.3,0)))
        for i in range(1, 7):
            v_follow[i] = Entity(model = "sphere", scale=.06)
            v_follow[i].add_script(SmoothFollow(target=v_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 7):
            destroy(v_follow[i])
        destroy(ven_speed)
       
        



def venus_distance():
    global v_dist
    global v_text
    global v_distance
    v_dist = not v_dist
    if v_dist == False:
        v_distance = Entity(model = "arrow", color = color.red, position = (1.5, -1.5, 0), scale= (1, 4, 3), shader=lit_with_shadows_shader)
        v_text = Text(text = "108.2 km (e6)", x = -0.85, y = -0.4, color = color.white)
    else:
        destroy(v_text)
        destroy(v_distance)

def pause_venus():
    global p_ven
    p_ven = not p_ven
    

venus_button = Button(text="Venus", scale=(0.2, 0.05), position=(-0.75, -0.47))
venus_button.on_click = pause_venus

venusDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(-0.75, -0.35))
venusDist_button.on_click = venus_distance

venusSpeed_button = Button(text="Venus Velocity", scale=(0.2, 0.05), position=(-0.75, -0.25))
venusSpeed_button.on_click = venus_speed

mar_dist = True
mar_speed = True

def mars_speed():
    global mar_speed
    global mar_dist
    global mar_follow
    global martxt_speed
    mar_speed = not mar_speed
    
    
    if mar_speed == False:
        martxt_speed = Text(text = "24.1 km/s", x = -0.30, y = -0.29, color = color.white)
        mar_follow = [None] * 12
        mar_follow[0] = Entity(model = "sphere", scale=.08)
        mar_follow[0].add_script(SmoothFollow(target=mars, offset=(0,-0.3,0)))
        for i in range(1, 12):
            mar_follow[i] = Entity(model = "sphere", scale=.06)
            mar_follow[i].add_script(SmoothFollow(target=mar_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 12):
            destroy(mar_follow[i])
        destroy(martxt_speed)
       
        



def mars_distance():
    global mar_dist
    global mar_text
    global mar_distance
    mar_dist = not mar_dist
    if mar_dist == False:
        mar_distance = Entity(model = "arrow", color = color.red, position = (2.5, -3.5, 0), scale= (3, 4, 5), shader=lit_with_shadows_shader)
        mar_text = Text(text = "228 km (e6)", x = -0.35, y = -0.4, color = color.white)
    else:
        destroy(mar_text)
        destroy(mar_distance)

def pause_mars():
    global p_mar
    p_mar = not p_mar
   
        

mars_button = Button(text="Mars", scale=(0.2, 0.05), position=(-0.25, -0.47))
mars_button.on_click = pause_mars

marsDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(-0.25, -0.35))
marsDist_button.on_click = mars_distance

marsSpeed_button = Button(text="Mars Velocity", scale=(0.2, 0.05), position=(-0.25, -0.25))
marsSpeed_button.on_click = mars_speed

jup_dist = True
jup_speed = True

def jupiter_speed():
    global jup_speed
    global jup_dist
    global jup_follow
    global juptxt_speed
    jup_speed = not jup_speed
    
    
    if jup_speed == False:
        juptxt_speed = Text(text = "41.53 km/s", x = -0.05, y = -0.29, color = color.white)
        jup_follow = [None] * 15
        jup_follow[0] = Entity(model = "sphere", scale=.2)
        jup_follow[0].add_script(SmoothFollow(target=jupiter, offset=(0,-0.3,0)))
        for i in range(1, 15):
            jup_follow[i] = Entity(model = "sphere", scale=.2)
            jup_follow[i].add_script(SmoothFollow(target=jup_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 15):
            destroy(jup_follow[i])
        destroy(juptxt_speed)


def jupiter_distance():
    global jup_dist
    global jup_text
    global jup_distance
    jup_dist = not jup_dist
    if jup_dist == False:
        jup_distance = Entity(model = "arrow", color = color.red, position = (7, -4.5, 0), scale= (12, 4, 8), shader=lit_with_shadows_shader)
        jup_text = Text(text = "778.5 km (e6)", x = -0.1, y = -0.4, color = color.white)
    else:
        destroy(jup_text)
        destroy(jup_distance)

def pause_jupiter():
    global p_jup
    p_jup = not p_jup
  
        
        

jupiter_button = Button(text="Jupiter", scale=(0.2, 0.05), position=(0, -0.47))
jupiter_button.on_click = pause_jupiter

jupiterDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(0, -0.35))
jupiterDist_button.on_click = jupiter_distance

jupiterSpeed_button = Button(text="Jupiter Velocity", scale=(0.2, 0.05), position=(0, -0.25))
jupiterSpeed_button.on_click = jupiter_speed

sat_dist = True
sat_speed = True

def saturn_speed():
    global sat_speed
    global sat_dist
    global sat_follow
    global sattxt_speed
    sat_speed = not sat_speed
    
    
    if sat_speed == False:
        sattxt_speed = Text(text = "9.7 km/s",  x = 0.2, y = -0.29, color = color.white)
        sat_follow = [None] * 23
        sat_follow[0] = Entity(model = "sphere", scale=.4)
        sat_follow[0].add_script(SmoothFollow(target=saturn, offset=(0,-0.3,0)))
        for i in range(1, 23):
            sat_follow[i] = Entity(model = "sphere", scale=.4)
            sat_follow[i].add_script(SmoothFollow(target=sat_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 23):
            destroy(sat_follow[i])
        destroy(sattxt_speed)


def saturn_distance():
    global sat_dist
    global sat_text
    global sat_distance
    sat_dist = not sat_dist
    if sat_dist == False:
        sat_distance = Entity(model = "arrow", color = color.red, position = (13, -9.5, 0), scale= (24, 10, 12), shader=lit_with_shadows_shader)
        sat_text = Text(text = "1432 km (e6)", x = 0.15, y = -0.4, color = color.white)
    else:
        destroy(sat_text)
        destroy(sat_distance)

def pause_saturn():
    global p_sat
    p_sat = not p_sat

 
        

saturn_button = Button(text="Saturn", scale=(0.2, 0.05), position=(0.25, -0.47))
saturn_button.on_click = pause_saturn

saturnDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(0.25, -0.35))
saturnDist_button.on_click = saturn_distance

saturnSpeed_button = Button(text="Saturn Velocity", scale=(0.2, 0.05), position=(0.25, -0.25))
saturnSpeed_button.on_click = saturn_speed

ura_dist = True
ura_speed = True

def uranus_speed():
    global ura_speed
    global ura_dist
    global ura_follow
    global uratxt_speed
    ura_speed = not ura_speed
    
    
    if ura_speed == False:
        uratxt_speed = Text(text = "6.8 km/s",  x = 0.45, y = -0.29, color = color.white)
        ura_follow = [None] * 45
        ura_follow[0] = Entity(model = "sphere", scale=.8)
        ura_follow[0].add_script(SmoothFollow(target=uranus, offset=(0,-0.3,0)))
        for i in range(1, 45):
            ura_follow[i] = Entity(model = "sphere", scale=.8)
            ura_follow[i].add_script(SmoothFollow(target=ura_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 45):
            destroy(ura_follow[i])
        destroy(uratxt_speed)


def uranus_distance():
    global ura_dist
    global ura_text
    global ura_distance
    ura_dist = not ura_dist
    if ura_dist == False:
        ura_distance = Entity(model = "arrow", color = color.red, position = (26, -13.5, 0), scale= (50, 16, 40), shader=lit_with_shadows_shader)
        ura_text = Text(text = "2867 km (e6)", x = 0.4, y = -0.4, color = color.white)
    else:
        destroy(ura_text)
        destroy(ura_distance)


def pause_uranus():
    global p_ura
    p_ura = not p_ura
    
        
        
uranus_button = Button(text="Uranus", scale=(0.2, 0.05), position=(0.5, -0.47))
uranus_button.on_click = pause_uranus

uranusDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(0.5, -0.35))
uranusDist_button.on_click = uranus_distance

uranusSpeed_button = Button(text="Uranus Velocity", scale=(0.2, 0.05), position=(0.5, -0.25))
uranusSpeed_button.on_click = uranus_speed

nep_dist = True
nep_speed = True

def neptune_speed():
    global nep_speed
    global nep_dist
    global nep_follow
    global neptxt_speed
    nep_speed = not nep_speed
    
    
    if nep_speed == False:
        neptxt_speed = Text(text = "5.6 km/s",  x = 0.7, y = -0.29, color = color.white)
        nep_follow = [None] * 55
        nep_follow[0] = Entity(model = "sphere", scale=0.8)
        nep_follow[0].add_script(SmoothFollow(target=neptune, offset=(0,-0.3,0)))
        for i in range(1, 55):
            nep_follow[i] = Entity(model = "sphere", scale=0.8)
            nep_follow[i].add_script(SmoothFollow(target=nep_follow[i - 1], offset=(0, -0.4,0)))
    else:
        for i in range(0, 55):
            destroy(nep_follow[i])
        destroy(neptxt_speed)



def neptune_distance():
    global nep_dist
    global nep_text
    global nep_distance
    nep_dist = not nep_dist
    if nep_dist == False:
        nep_distance = Entity(model = "arrow", color = color.red, position = (40, -23.5, 0), scale= (78, 30, 60), shader=lit_with_shadows_shader)
        nep_text = Text(text = "4515 km (e6)", x = 0.65, y = -0.4, color = color.white)
    else:
        destroy(nep_text)
        destroy(nep_distance)

def pause_neptune():
    global p_nep
    p_nep = not p_nep

    

        
        

neptune_button = Button(text="Neptune", scale=(0.2, 0.05), position=(0.75, -0.47))
neptune_button.on_click = pause_neptune

neptuneDist_button = Button(text="Distance from sun", scale=(0.22, 0.05), position=(0.75, -0.35))
neptuneDist_button.on_click = neptune_distance

neptuneSpeed_button = Button(text="Neptune Velocity", scale=(0.2, 0.05), position=(0.75, -0.25))
neptuneSpeed_button.on_click = neptune_speed


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
txt=Text(text="Orbital velocity and distance from sun in solar system 3D simulator", color=color.white, x = -0.45, y = 0.4)

sky=Sky(texture="space.jpg", doubled_side = True)
t=-np.pi
dx = .01
h = g = h = f = e = d = c = b = a = t
app.run()
