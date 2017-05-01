from vpython import *
#some constants

R=1  #this is radius of the star
M=1 #mass of star
G=100  #fake gravitational constant

#create the objects
planet1=sphere(pos=vector(4.5*R,0,0), radius=R, color=color.red)
planet2=sphere(pos=vector(-4.5*R,0,0), radius=R, color=color.blue)
#set the masss and momentum of the stars
planet1.m=M
planet2.m=M
planet1.p=vector(0,2,0)*planet1.m
planet2.p=vector(0,-2,0)*planet2.m
#notice that the total momentum is zero vector
attach_trail(planet1)
attach_trail(planet2)

dt=0.001

while True:
    rate(1000)
    #calculate the vector from star 1 to 2
    r12=planet2.pos-planet1.pos

    #calculate the gravitational force on 1
    F12=-G*planet1.m*planet2.m*norm(r12)/mag2(r12)
    #forces come in pairs, so F21 is opposite
    F21=-F12
  
    #update the momentum
    planet1.p=planet1.p+(F21)*dt
    planet2.p=planet2.p+(F12)*dt
    
    #update the position
    planet1.pos=planet1.pos+planet1.p*dt/planet1.m
    planet2.pos=planet2.pos+planet2.p*dt/planet2.m
   
