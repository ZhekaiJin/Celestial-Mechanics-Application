#some constants
from vpython import * 



scene.forward = vector(0,-.25,-1)
G=6.7e-11  #fake gravitational constant
#create the objects
planet1 = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.red, 
                make_trail=True, trail_type='points', interval=10, retain=50)
planet2=sphere(pos=vector(1.5e11,0,0), radius=1e10, color=color.blue,
                make_trail=True, interval=10, retain=50)
#set the masss and momentum of the stars
planet1.m=2e30
planet2.m=1e30
planet1.p = vector(0, 0, -1e4) * planet1.m
planet2.p = -planet1.p
#notice that the total momentum is zero vector
dt= 1e5
while True:
    rate(200)
    #calculate the vector from star 1 to 2
    r12=planet2.pos-planet1.pos
    #calculate the gravitational force on 1
    F12=-G*planet1.m*planet2.m*norm(r12)/mag2(r12)
    #forces come in pairs, so F21 is opposite
    #update the momentum
    planet1.p=planet1.p-(F12)*dt
    planet2.p=planet2.p+(F12)*dt
    #update the position
    planet1.pos=planet1.pos+planet1.p*dt/planet1.m
    planet2.pos=planet2.pos+planet2.p*dt/planet2.m


