#author:scott
from vpython import *
scene.forward = vector(0,-.25,-1)
G=6.7e-11  #fake gravitational constant
#create the objects
planet1 = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.red, 
                make_trail=True, interval=10, retain=50)
planet2=sphere(pos=vector(1.5e11,0,0), radius=1e10, color=color.blue,
                make_trail=True, interval=10, retain=50)

spaceship=sphere(pos=vector(8e11,0,0), radius=1e10, color=color.green,
                make_trail=True, trail_type='points', interval=10, retain=50)
#set the masss and momentum of the stars
planet1.m=2e30
planet2.m=1e30
spaceship.m=1e5
spaceship.p=vector(1e2,0,0)*spaceship.m
planet1.p = vector(0,0,-1e4) * planet1.m
planet2.p=-(spaceship.p+planet1.p)
#notice that the total momentum is zero vector
dt= 1e5
while True:
    rate(200)
    #calculate the vector from star 1 to 2
    r12=planet2.pos-planet1.pos
    r1p=spaceship.pos-planet1.pos
    r2p=spaceship.pos-planet2.pos

    #calculate the gravitational force on 1
    F12=-G*planet1.m*planet2.m*norm(r12)/mag2(r12)
    F21=-F12

    F1p=-G*planet1.m*spaceship.m*norm(r1p)/mag2(r1p)
    #calculate the force on spaceship due to star 2
    F2p=-G*planet2.m*spaceship.m*norm(r2p)/mag2(r2p)
    
    #forces come in pairs, so F21 is opposite
    #update the momentum
    planet1.p=planet1.p+(F21-F1p)*dt
    planet2.p=planet2.p+(F12-F2p)*dt
    spaceship.p=spaceship.p+(F1p+F2p)*dt
    
    #update position
    planet1.pos=planet1.pos+planet1.p*dt/planet1.m
    planet2.pos=planet2.pos+planet2.p*dt/planet2.m
    spaceship.pos=spaceship.pos+spaceship.p*dt/spaceship.m
