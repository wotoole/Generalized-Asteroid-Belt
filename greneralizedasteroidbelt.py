'''asteroidbeltgeneralized.py'''

from visual import*
from visual.graph import*
from random import *
from math import *

ratio = input("Enter the ratio")
masscp = input("Enter the mass of the central planet")
massop = input("Enter the mass of the orbiting planet")
G = 6.67e-11
AU = 1.5e11
year = 365.25*24.*60.*60.
r0 = 5.2*AU*pow(ratio,2./3.)
asteroidpos = []
asteroidvel = []

centralplanet = sphere(pos=(0,0,0), radius = 100*7e8, mass = masscp, color = color.yellow)
orbitingplanet = sphere(pos=(5.2*AU,0,0), radius=8000.*6.4e6, mass = massop, color=color.red)
orbitingplanet.vel = vector(0,sqrt(G*centralplanet.mass/(5.2*AU)),0)

asteroid_list = []
for i in range(0,100):
    angle = i*2*pi/100
    asteroid = ellipsoid(pos=(r0*cos(angle), r0*sin(angle),0), length= 300*6.4E7, width = 200.*6.4e7, height = 200*6.4e7, color = (1,1,0))
    asteroid.vel = vector(-sqrt(G*centralplanet.mass/r0)*sin(angle),sqrt(G*centralplanet.mass/r0)*cos(angle),0.1*sqrt(G*centralplanet.mass/r0))
    asteroid_list.append(asteroid)

plot = gdisplay(x=0, y = 400, height = 400, width = 600, title = "r vs. t", xtitle = 't', ytitle = 'r')
data = gdots(color=color.white)

dt = 1.e6
t = 0.0

while True:
    for asteroid in asteroid_list:
        asteroid.vel = asteroid.vel + (-G*centralplanet.mass*(asteroid.pos - centralplanet.pos)/mag(asteroid.pos - centralplanet.pos)**3 - G*orbitingplanet.mass*(asteroid.pos-orbitingplanet.pos)/mag(asteroid.pos-orbitingplanet.pos)**3)*dt
        asteroid.pos = asteroid.pos + asteroid.vel*dt
    data.plot(pos=(t/year, mag(asteroid.pos/r0)-1))

    orbitingplanet.vel = orbitingplanet.vel + -G*centralplanet.mass*(orbitingplanet.pos-centralplanet.pos)/mag(orbitingplanet.pos-centralplanet.pos)**3*dt
    orbitingplanet.pos = orbitingplanet.pos + orbitingplanet.vel*dt
    t+=dt
    rate(100)
