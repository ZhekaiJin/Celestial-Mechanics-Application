from vpython import *
# setting up immaginary constant for zero momentum
R=1
M=1
G=100
#creating the stars
planet1=sphere(pos=vector(4.5*R,0,0), radius=R, color=color.red,make_trail=True)
planet2=sphere(pos=vector(-4.5*R,0,0), radius=R, color=color.blue,make_trail=True)
planet1.m=M
planet2.m=M
planet1.p=vector(0,2,0)*planet1.m
#I will set the other star momentum below
spaceship=sphere(pos=vector(9*R,0,0), radius=0.2*R, color=color.cyan,make_trail=True)
spaceship.m=M/1000
spaceship.p=vector(0,3,0)*spaceship.m # change the speed and momentum of spaceship here!!!
planet2.p=-(spaceship.p+planet1.p)
dt=0.001
while True:
    rate(500)
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


