import json
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sea

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

print(distance_from_sun)

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
y =  velocity
z = []
for i, data in enumerate(x):
    z.append([gravitational_force[i], data])

df2 = pd.DataFrame(z, columns = ['Gravitational_force', 'distance_from_sun'])
df2['Velocity'] = pd.Series(y)
model = smf.ols(formula='Velocity ~ Gravitational_force + distance_from_sun', data = df2)
result = model.fit()
result.params

x_surf, y_surf = np.meshgrid(np.linspace(df2.Gravitational_force.min(), df2.Gravitational_force.max(), 20), np.linspace(df2.distance_from_sun.min(), df2.distance_from_sun.max(), 100))
onlyX = pd.DataFrame({'Gravitational_force': x_surf.ravel(), 'distance_from_sun': y_surf.ravel()})
fittedY = result.predict(exog = onlyX)

fittedY = np.array(fittedY)
fig = plt.figure()
bx = fig.add_subplot(111, projection='3d')
c = ['gray', 'b', 'r', 'orange', 'brown', 'pink', 'yellow', 'cyan']
labels = ['Mercury', 'Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for i, label in enumerate(labels):
    bx.scatter(df2.loc[df2.index == i, 'Gravitational_force'], df2.loc[df2.index == i, 'distance_from_sun'], df2.loc[df2.index == i, 'Velocity'], c = c[i], marker='o', label=label)
bx.plot_surface(x_surf, y_surf, fittedY.reshape(x_surf.shape), alpha=0.3, edgecolors='steelblue', lw=0.1)
plt.legend(bbox_to_anchor=(1.2, 1.0), loc='upper left')
bx.xaxis.gridlines.set_visible(False)
bx.yaxis.gridlines.set_visible(False)
bx.zaxis.gridlines.set_visible(False)
plt.style.use('ggplot')
bx.set_xlabel('Gravitational_force (e-14)')
bx.set_ylabel('distance_from_sun (e6) km')
bx.set_zlabel('Velocity (km/s)')

plt.title("Planet's orbital velocity relationship")
plt.show()


def corr(x, y, **kwargs):
    
    # Calculate the value
    coef = np.corrcoef(x, y)[0][1]
    # Make the label
    label = r'$\rho$ = ' + str(round(coef, 2))
    
    # Add the label to the plot
    ax = plt.gca()
    ax.annotate(label, xy = (0.4, 0.9), size = 10, xycoords = ax.transAxes)
sea.set_palette('colorblind')
grid = sea.pairplot(data=df2, height=3)
grid = grid.map_upper(corr)
grid = grid.map_lower(corr)





#2D
x = gravitational_force
y =  velocity

fig, ax = plt.subplots()
ax.scatter(x, y, c = 'b') 

##for x0, y0, path in zip(x, y,paths):
##    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
##    ax.add_artist(ab)

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
  return slope *x+ intercept

mymodel = list(map(myfunc, x))



plt.scatter(x, y)
plt.plot(x, mymodel, ls = '--', c = 'k')

#plt.title("Relationship between velocity of planets and distance from sun")
plt.title("Relationship between Gravitationational force and distance")
plt.ylabel("Distance from sun (e+6) km")
plt.xlabel("Gravitational force of planets")
plt.show()

# create linear regression for planet data

##slope, intercept, r, p, std_err = stats.linregress(x, y)
##def myfunc(x):
##  return slope * x + intercept
##
##mymodel = list(map(myfunc, x))
##
##
##f = plt.figure("figure 1")
##plt.scatter(x, y)
##plt.plot(x, mymodel, ls='-')
##plt.grid()
##plt.title("Relationship between velocity and distance")
##plt.xlabel("Distance from sun")
##plt.ylabel("Velocity of planets")
##f.show()

#second plot
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
##





