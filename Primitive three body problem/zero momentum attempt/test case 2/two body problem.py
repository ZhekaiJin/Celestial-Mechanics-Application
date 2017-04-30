from vpython import *
# setting up immaginary constant for zero momentum

R=1
M=1
G=10

#creating the stars
sun1=sphere(pos=vector(5*R,0,0), radius=R, color=color.blue)
sun2=sphere(pos=vector(-5*R,0,0), radius=R/8, color=color.red)
sun1.m=M
sun2.m=M
sun1.p=vector(0,2,0)*sun1.m
#I will set the other star momentum below

#create the planet
planet=sphere(pos=vector(9*R,0,0), radius=0.2*R, color=color.cyan)
planet.m=M/1000
planet.p=vector(0,3,0)*planet.m
#here I set the momentum of sun 2 so that the total momentum is zero
sun2.p=-(planet.p+sun1.p)

attach_trail(sun1)
attach_trail(sun2)
attach_trail(planet)
t=0
dt=0.001

while t<300:
    rate(10000)
    
    #vector from star 1 to 2
    r12=sun2.pos-sun1.pos
    
    #vector from star 1 to planet
    r1p=planet.pos-sun1.pos
    
    #vector from star 2 to planet
    r2p=planet.pos-sun2.pos
    
    #calculate grav force on star 1 due to 2
    F12=-G*sun1.m*sun2.m*norm(r12)/mag(r12)**2
    F21=-F12
    #calculate the force on planet due to star 1
    F1p=-G*sun1.m*planet.m*norm(r1p)/mag(r1p)**2
    #calculate the force on planet due to star 2
    F2p=-G*sun2.m*planet.m*norm(r2p)/mag(r2p)**2
    
    #update momentum (with total vector force)
    sun1.p=sun1.p+(F21-F1p)*dt
    sun2.p=sun2.p+(F12-F2p)*dt
    planet.p=planet.p+(F1p+F2p)*dt
    
    #update position
    sun1.pos=sun1.pos+sun1.p*dt/sun1.m
    sun2.pos=sun2.pos+sun2.p*dt/sun2.m
    planet.pos=planet.pos+planet.p*dt/planet.m
    t=t+dt
