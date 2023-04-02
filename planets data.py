import json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image


with open('planets data.json', 'r') as f:
    data = json.load(f)

def gravitational_force_from_sun(mass, distance):
    result = (6.67 * (10**-11)) * (mass * data["Sun"]["mass_10_to_power_24_kg"])/((distance) ** 2)
    return result

planet_name = []
velocity = []
gravity = []
gravitational_force = []
distance_from_sun = []
for planet in data:
    if planet != "Sun":
        planet_name.append(planet)
        gravitational_force.append(data[planet]["Gravitational_force_from_sun_e-14"])
        velocity.append(data[planet]["orbital_velocity_km"])
        distance_from_sun.append(data[planet]["distance_from_sun_10_to_power_6_km"])
        gravity.append(data[planet]["surface_gravity"])

print(planet_name)

#insert images
def getImage(path, zoom=1):
    return OffsetImage(plt.imread(path), zoom=0.2)

im = Image.open("45aa67abc6c36bed9476117dc9cc66df.png")

paths = [
    "mercury.png",
    "earth.png",
    "mars.png",
    "venus.png",
    "jupiter.png",
    "saturn.png",
    "uranus.png",
    "neptune.png"]


x = distance_from_sun
y =  gravitational_force

fig, ax = plt.subplots()
ax.scatter(x, y) 

for x0, y0, path in zip(x, y,paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)

name =  [s.replace(".png", "") for s in paths]

for i, z in enumerate(name):
    if i != 0 and i != 7 and i != 4:
        ax.annotate(z, (x[i], y[i]), (x[i] - 220, y[i] + 2))
    elif i == 0 or i == 4:
        ax.annotate(z, (x[i], y[i]), (x[i] + 220, y[i]))
    elif i == 7:
        ax.annotate(z, (x[i], y[i]), (x[i] - 420, y[i] + 2))


slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope *a+ intercept

mymodel = list(map(myfunc, x))



plt.scatter(x, y)
plt.plot(x, mymodel)
plt.grid()
#plt.title("Relationship between velocity of planets and distance from sun")
plt.title("Relationship between gravitational force of planets and distance from sun")
plt.xlabel("Distance from sun (e+6) km")
plt.ylabel("Gravitational force of planets between the sun")
plt.show()
### create linear regression for planet data
##
##slope, intercept, r, p, std_err = stats.linregress(x, y)
##def myfunc(x):
##  return slope * x + intercept
##
##mymodel = list(map(myfunc, x))
##
##
##f = plt.figure("figure 1")
##plt.scatter(x, y)
##plt.plot(x, mymodel)
##plt.grid()
##plt.title("Relationship between velocity and distance")
##plt.xlabel("Distance from sun")
##plt.ylabel("Velocity of planets")
##f.show()
##
###second plot
##x = distance_from_sun
##y = gravitational_force
##
##slope, intercept, r, p, std_err = stats.linregress(x, y)
##mymodel = list(map(myfunc, x))
##
##
##g = plt.figure("figure 2")
##plt.scatter(x, y)
##plt.plot(x, mymodel)
##plt.grid()
##plt.title("Relationship between Gravitational force from sun and distance")
##plt.xlabel("Distance from sun")
##plt.ylabel("Gravitational force of planets")
##g.show()






